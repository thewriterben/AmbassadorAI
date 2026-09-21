package com.digitalgold.ticker.ui

import android.content.Context
import android.os.Build
import android.os.VibrationEffect
import android.os.Vibrator
import android.os.VibratorManager
import android.provider.Settings
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.CubicBezierEasing
import androidx.compose.animation.core.EaseOut
import androidx.compose.animation.core.spring
import androidx.compose.animation.core.tween
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.safeDrawingPadding
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.rememberModalBottomSheetState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.drawBehind
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import androidx.lifecycle.compose.LocalLifecycleOwner
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.digitalgold.ticker.animation.DisplayedStats
import com.digitalgold.ticker.animation.PriceExplosion
import com.digitalgold.ticker.audio.TickerSoundPlayer
import com.digitalgold.ticker.model.StatsSnapshot
import com.digitalgold.ticker.persistence.SignupPreferences
import com.digitalgold.ticker.viewmodel.TickerViewModel
import kotlinx.coroutines.delay
import kotlinx.coroutines.isActive
import java.time.ZoneId
import java.time.format.DateTimeFormatter
import java.time.format.FormatStyle
import java.util.Locale
import kotlin.math.pow

/** One-screen ticker. Owns animation progress; talks to the view model only. */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun TickerScreen(
    model: TickerViewModel,
    signupPrefs: SignupPreferences,
    inviteGeneration: Int = 0,
) {
    val ui by model.ui.collectAsStateWithLifecycle()
    val context = LocalContext.current
    val reduceMotion = remember { context.isReduceMotionEnabled() }
    val progress = remember { Animatable(0f) }
    val punch = remember { Animatable(1f) }
    var explosionAt by remember { mutableStateOf<Long?>(null) }
    var priceWaveStartedAt by remember { mutableStateOf<Long?>(null) }
    var showSignupPreview by remember { mutableStateOf(false) }
    var showLoginPreview by remember { mutableStateOf(false) }
    var presentSignupAfterLogin by remember { mutableStateOf(false) }
    var statsExpanded by remember { mutableStateOf(false) }
    val loggedIn = signupPrefs.membershipPreviewCompleted
    val lifecycleOwner = LocalLifecycleOwner.current
    val soundPlayer = remember { TickerSoundPlayer.shared(context) }

    // Soft coin once per process on first home appearance.
    // Not on foreground return, sheet dismiss, or the price burst.
    LaunchedEffect(Unit) {
        soundPlayer.playOpenIfNeeded()
        model.load()
        while (isActive) {
            delay(TickerViewModel.pollIntervalMs)
            model.load()
        }
    }

    // Only refetch when returning from background. A launch ON_START
    // would set origin = live and skip the count-up / explosion.
    var resumeGeneration by remember { mutableStateOf(0) }
    DisposableEffect(lifecycleOwner) {
        var wasStopped = false
        val observer = LifecycleEventObserver { _, event ->
            when (event) {
                Lifecycle.Event.ON_STOP -> wasStopped = true
                Lifecycle.Event.ON_START -> if (wasStopped) {
                    wasStopped = false
                    resumeGeneration += 1
                }
                else -> Unit
            }
        }
        lifecycleOwner.lifecycle.addObserver(observer)
        onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
    }
    LaunchedEffect(resumeGeneration) {
        if (resumeGeneration > 0) model.load()
    }

    LaunchedEffect(ui.loadState) {
        if (ui.loadState is TickerViewModel.LoadState.Loading) {
            progress.snapTo(0f)
            punch.snapTo(1f)
            explosionAt = null
            priceWaveStartedAt = null
        }
    }

    LaunchedEffect(ui.fetchGeneration) {
        explosionAt = null
        priceWaveStartedAt = null
        punch.snapTo(1f)
        when (val state = ui.loadState) {
            is TickerViewModel.LoadState.Ready -> {
                val live = ui.liveSnapshot ?: return@LaunchedEffect
                val origin = ui.originSnapshot
                val first = ui.isFirstLaunch
                val unchanged = origin?.hasSameNumbers(live) == true
                if (reduceMotion || unchanged) {
                    progress.snapTo(1f)
                    return@LaunchedEffect
                }
                if (first) {
                    progress.snapTo(0f)
                    progress.animateTo(1f, tween(durationMillis = 850, easing = EaseOut))
                    return@LaunchedEffect
                }
                progress.snapTo(0f)
                progress.animateTo(
                    1f,
                    tween(
                        durationMillis = 2550,
                        easing = CubicBezierEasing(0.90f, 0.00f, 0.95f, 0.18f),
                    ),
                )
                // fireExplosion: burst even if Reduce Motion skips the visual.
                // Not reached on first-launch fade, unchanged snap, or chart fireworks.
                soundPlayer.playBurst()
                if (!reduceMotion) {
                    val now = System.currentTimeMillis()
                    explosionAt = now
                    priceWaveStartedAt = now
                    punch.snapTo(1.28f)
                    punch.animateTo(
                        1f,
                        spring(dampingRatio = 0.34f, stiffness = 273f),
                    )
                    context.fireSuccessHaptic()
                }
            }
            else -> {
                if (state !is TickerViewModel.LoadState.Loading) {
                    progress.snapTo(1f)
                }
            }
        }
    }

    Box(
        Modifier
            .fillMaxSize()
            .drawBehind {
                drawRect(brush = GoldTheme.background)
            },
    ) {
        // MainActivity calls enableEdgeToEdge(), and on targetSdk 35 Android 15
        // enforces it whether you ask or not — so without this every child
        // draws under the status and navigation bars. On a Pixel that put
        // "Log in" behind the battery icon and the LIVE footer behind the
        // gesture bar.
        //
        // The inset goes here, not on the outer Box: the gradient above should
        // still run edge to edge behind the system bars, which is the whole
        // point of drawing edge to edge. Only the content is inset — including
        // the hairline frame, which should border the usable area rather than
        // the glass.
        Box(Modifier.fillMaxSize().safeDrawingPadding()) {
        Box(
            Modifier
                .fillMaxSize()
                .padding(14.dp)
                .border(0.6.dp, GoldTheme.hairline, RectangleShape),
        )

        TickerBody(
            ui = ui,
            progress = progress.value.toDouble(),
            punch = punch.value,
            homeCta = LockedCopy.homeCtaLabel(loggedIn),
            isStatsExpanded = statsExpanded,
            priceWaveStartedAtMillis = priceWaveStartedAt,
            reduceMotion = reduceMotion,
            onGetDigitalGold = { showSignupPreview = true },
            onShowStats = { statsExpanded = true },
            onCloseStats = { statsExpanded = false },
        )

        if (!loggedIn) {
            TextButton(
                onClick = { showLoginPreview = true },
                modifier = Modifier
                    .align(Alignment.TopEnd)
                    .padding(top = 16.dp, end = 16.dp),
            ) {
                Text(
                    text = LockedCopy.LOG_IN,
                    color = GoldTheme.gold,
                    fontSize = 14.sp,
                    fontWeight = FontWeight.SemiBold,
                )
            }
        }

        val burstAt = explosionAt
        if (burstAt != null && !reduceMotion && !statsExpanded) {
            PriceExplosion(
                startedAtMillis = burstAt,
                modifier = Modifier
                    .fillMaxSize()
                    .offset(y = (-8).dp),
            )
        }
        }
    }

    if (showSignupPreview) {
        val sheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true)
        ModalBottomSheet(
            onDismissRequest = { showSignupPreview = false },
            sheetState = sheetState,
            containerColor = GoldTheme.backgroundBottom,
            contentColor = GoldTheme.ivory,
        ) {
            SignupPreviewScreen(
                prefs = signupPrefs,
                inviteGeneration = inviteGeneration,
                onClose = { showSignupPreview = false },
            )
        }
    }

    if (showLoginPreview && !loggedIn) {
        val loginSheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true)
        ModalBottomSheet(
            onDismissRequest = { showLoginPreview = false },
            sheetState = loginSheetState,
            containerColor = GoldTheme.backgroundBottom,
            contentColor = GoldTheme.ivory,
        ) {
            LoginPreviewScreen(
                prefs = signupPrefs,
                onClose = { showLoginPreview = false },
                onJoinNetwork = {
                    showLoginPreview = false
                    presentSignupAfterLogin = true
                },
            )
        }
    }

    LaunchedEffect(showLoginPreview, presentSignupAfterLogin) {
        if (!showLoginPreview && presentSignupAfterLogin) {
            presentSignupAfterLogin = false
            showSignupPreview = true
        }
    }
}

@Composable
private fun TickerBody(
    ui: TickerViewModel.UiState,
    progress: Double,
    punch: Float,
    homeCta: String,
    isStatsExpanded: Boolean,
    priceWaveStartedAtMillis: Long?,
    reduceMotion: Boolean,
    onGetDigitalGold: () -> Unit,
    onShowStats: () -> Unit,
    onCloseStats: () -> Unit,
) {
    val statsEndCap = when (ui.loadState) {
        TickerViewModel.LoadState.Ready -> ui.liveSnapshot
        TickerViewModel.LoadState.Idle, TickerViewModel.LoadState.Loading -> ui.originSnapshot
        is TickerViewModel.LoadState.Failed -> ui.originSnapshot ?: ui.liveSnapshot
    }
    when (val state = ui.loadState) {
        TickerViewModel.LoadState.Idle, TickerViewModel.LoadState.Loading -> {
            val origin = ui.originSnapshot
            if (origin != null) {
                SnapshotTicker(
                    snapshot = origin,
                    opacity = 1f,
                    punch = 1f,
                    statusTitle = "UPDATING",
                    statusDetail = null,
                    isError = false,
                    isUpdating = true,
                    homeCta = homeCta,
                    isStatsExpanded = isStatsExpanded,
                    statsEndCap = statsEndCap,
                    priceWaveStartedAtMillis = priceWaveStartedAtMillis,
                    reduceMotion = reduceMotion,
                    onGetDigitalGold = onGetDigitalGold,
                    onShowStats = onShowStats,
                    onCloseStats = onCloseStats,
                )
            } else {
                EmptyLoading()
            }
        }
        TickerViewModel.LoadState.Ready -> {
            val live = ui.liveSnapshot
            if (live != null) {
                AnimatedTickerNumbers(
                    progress = progress,
                    from = ui.originSnapshot,
                    to = live,
                    firstLaunch = ui.isFirstLaunch,
                    punch = punch,
                    statusTitle = "LIVE",
                    statusDetail = live.fetchedAt.toShortTime(),
                    isError = false,
                    isUpdating = false,
                    homeCta = homeCta,
                    isStatsExpanded = isStatsExpanded,
                    statsEndCap = statsEndCap,
                    priceWaveStartedAtMillis = priceWaveStartedAtMillis,
                    reduceMotion = reduceMotion,
                    onGetDigitalGold = onGetDigitalGold,
                    onShowStats = onShowStats,
                    onCloseStats = onCloseStats,
                )
            } else {
                EmptyLoading()
            }
        }
        is TickerViewModel.LoadState.Failed -> {
            val stale = ui.originSnapshot ?: ui.liveSnapshot
            if (stale != null) {
                SnapshotTicker(
                    snapshot = stale,
                    opacity = 1f,
                    punch = 1f,
                    statusTitle = "LAST SEEN · UNAVAILABLE",
                    statusDetail = "${state.error.tickerMessage} · ${stale.fetchedAt.toAbbreviatedDateTime()}",
                    isError = true,
                    isUpdating = false,
                    homeCta = homeCta,
                    isStatsExpanded = isStatsExpanded,
                    statsEndCap = statsEndCap,
                    priceWaveStartedAtMillis = priceWaveStartedAtMillis,
                    reduceMotion = reduceMotion,
                    onGetDigitalGold = onGetDigitalGold,
                    onShowStats = onShowStats,
                    onCloseStats = onCloseStats,
                )
            } else {
                FailedEmpty(state.error.tickerMessage)
            }
        }
    }
}

@Composable
private fun SnapshotTicker(
    snapshot: StatsSnapshot,
    opacity: Float,
    punch: Float,
    statusTitle: String,
    statusDetail: String?,
    isError: Boolean,
    isUpdating: Boolean,
    homeCta: String,
    isStatsExpanded: Boolean,
    statsEndCap: StatsSnapshot?,
    priceWaveStartedAtMillis: Long?,
    reduceMotion: Boolean,
    onGetDigitalGold: () -> Unit,
    onShowStats: () -> Unit,
    onCloseStats: () -> Unit,
) {
    TickerContent(
        accounts = snapshot.accounts,
        price = snapshot.price,
        marketCap = snapshot.marketCap,
        accessibilityPrice = snapshot.price,
        accessibilityAccounts = snapshot.accounts,
        accessibilityMarketCap = snapshot.marketCap,
        opacity = opacity,
        punch = punch,
        statusTitle = statusTitle,
        statusDetail = statusDetail,
        isError = isError,
        isUpdating = isUpdating,
        onGetDigitalGold = onGetDigitalGold,
        homeCta = homeCta,
        isStatsExpanded = isStatsExpanded,
        statsEndCap = statsEndCap,
        priceWaveStartedAtMillis = priceWaveStartedAtMillis,
        reduceMotion = reduceMotion,
        onShowStats = onShowStats,
        onCloseStats = onCloseStats,
    )
}

@Composable
private fun AnimatedTickerNumbers(
    progress: Double,
    from: StatsSnapshot?,
    to: StatsSnapshot,
    firstLaunch: Boolean,
    punch: Float,
    statusTitle: String,
    statusDetail: String?,
    isError: Boolean,
    isUpdating: Boolean,
    homeCta: String,
    isStatsExpanded: Boolean,
    statsEndCap: StatsSnapshot?,
    priceWaveStartedAtMillis: Long?,
    reduceMotion: Boolean,
    onGetDigitalGold: () -> Unit,
    onShowStats: () -> Unit,
    onCloseStats: () -> Unit,
) {
    val shown = DisplayedStats.resolve(from, to, progress, firstLaunch)
    val fadeOpacity = if (firstLaunch) {
        val t = progress.coerceIn(0.0, 1.0)
        (1.0 - (1.0 - t).pow(2.0)).toFloat()
    } else {
        1f
    }
    TickerContent(
        accounts = shown.accounts,
        price = shown.price,
        marketCap = shown.marketCap,
        accessibilityPrice = to.price,
        accessibilityAccounts = to.accounts,
        accessibilityMarketCap = to.marketCap,
        opacity = fadeOpacity,
        punch = punch,
        statusTitle = statusTitle,
        statusDetail = statusDetail,
        isError = isError,
        isUpdating = isUpdating,
        onGetDigitalGold = onGetDigitalGold,
        homeCta = homeCta,
        isStatsExpanded = isStatsExpanded,
        statsEndCap = statsEndCap,
        priceWaveStartedAtMillis = priceWaveStartedAtMillis,
        reduceMotion = reduceMotion,
        onShowStats = onShowStats,
        onCloseStats = onCloseStats,
    )
}

private fun java.time.Instant.toShortTime(): String =
    DateTimeFormatter.ofLocalizedTime(FormatStyle.SHORT)
        .withLocale(Locale.getDefault())
        .withZone(ZoneId.systemDefault())
        .format(this)

private fun java.time.Instant.toAbbreviatedDateTime(): String =
    DateTimeFormatter.ofLocalizedDateTime(FormatStyle.MEDIUM, FormatStyle.SHORT)
        .withLocale(Locale.getDefault())
        .withZone(ZoneId.systemDefault())
        .format(this)

private fun Context.isReduceMotionEnabled(): Boolean {
    val animator = Settings.Global.getFloat(contentResolver, Settings.Global.ANIMATOR_DURATION_SCALE, 1f)
    val transition = Settings.Global.getFloat(contentResolver, Settings.Global.TRANSITION_ANIMATION_SCALE, 1f)
    return animator == 0f || transition == 0f
}

private fun Context.fireSuccessHaptic() {
    val vibrator = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        getSystemService(VibratorManager::class.java)?.defaultVibrator
    } else {
        @Suppress("DEPRECATION")
        getSystemService(Vibrator::class.java)
    } ?: return
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        vibrator.vibrate(VibrationEffect.createPredefined(VibrationEffect.EFFECT_CLICK))
    } else {
        @Suppress("DEPRECATION")
        vibrator.vibrate(40)
    }
}
