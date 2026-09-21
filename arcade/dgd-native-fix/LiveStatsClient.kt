package com.digitalgold.ticker.networking

import com.digitalgold.ticker.model.StatsEndpoint
import com.digitalgold.ticker.model.StatsSnapshot
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import okhttp3.CacheControl
import okhttp3.OkHttpClient
import okhttp3.Request
import java.time.Instant
import java.util.concurrent.TimeUnit

/**
 * The single live network implementation. All HTTP lives here.
 *
 * SWAP POINT: re-point [endpoint] (via [StatsEndpoint] / bundled
 * `stats-source.json`) or replace this type with another [StatsClient].
 * Do not add fetch code in views.
 *
 * Flow (DATA_SOURCE.md):
 * 1. GET `https://digitalgold.co/api/forms/stats` — no `Origin` header.
 * 2. Read `count` as accounts. Do **not** use `userLevel.price` / `userLevel.marketCap`.
 * 3. Derive 5-decimal price and market cap with [com.digitalgold.ticker.model.ContinuousCFV].
 */
class LiveStatsClient(
    val endpoint: StatsEndpoint = StatsEndpoint.published,
    private val http: OkHttpClient = recommendedClient(),
    private val now: () -> Instant = { Instant.now() },
) : StatsClient {

    // THE FIX: OkHttp's execute() is blocking. This is a suspend function, but
    // a suspend function runs on whatever dispatcher its caller used — and the
    // caller is a Compose LaunchedEffect, which is the main thread. Android's
    // StrictMode kills main-thread network I/O, so every fetch threw
    // NetworkOnMainThreadException, was swallowed by the catch below, and the
    // ticker showed "Stats unavailable" forever.
    override suspend fun fetchSnapshot(): StatsSnapshot = withContext(Dispatchers.IO) {
        val request = Request.Builder()
            .url(endpoint.url)
            .get()
            .header("Accept", "application/json")
            .cacheControl(CacheControl.FORCE_NETWORK)
            .build()
        // Do not set Origin — foreign Origin values 500 this API (DATA_SOURCE.md).

        val response = try {
            http.newCall(request).execute()
        } catch (e: Exception) {
            // Was `catch (_: Exception)`. Discarding this is what made the
            // failure invisible: the ticker showed its empty state and the
            // cause never reached logcat, so a source review concluded the
            // networking was fine. Keep the log even though the error type
            // stays the same.
            android.util.Log.w("LiveStatsClient", "stats fetch failed", e)
            throw StatsClientError.Unavailable
        }

        response.use { body ->
            if (body.code !in 200..299) {
                android.util.Log.w("LiveStatsClient", "stats fetch HTTP ${body.code}")
                throw StatsClientError.Unavailable
            }
            val bytes = body.body?.bytes() ?: throw StatsClientError.InvalidResponse
            endpoint.parse(bytes, now())
        }
    }

    companion object {
        /** Official site polls every 45s. Stay at or below that. */
        const val recommendedPollIntervalMs: Long = 45_000

        fun recommendedClient(): OkHttpClient =
            OkHttpClient.Builder()
                .connectTimeout(15, TimeUnit.SECONDS)
                .readTimeout(15, TimeUnit.SECONDS)
                .writeTimeout(15, TimeUnit.SECONDS)
                .cache(null)
                .build()
    }
}
