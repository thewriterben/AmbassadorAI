package com.digitalgold.ticker.ui

import android.content.ActivityNotFoundException
import android.content.ClipData
import android.content.ClipboardManager
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.provider.Settings
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.slideInVertically
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.imePadding
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.Check
import androidx.compose.material.icons.outlined.ContentCopy
import androidx.compose.material.icons.outlined.Info
import androidx.compose.material.icons.outlined.Visibility
import androidx.compose.material.icons.outlined.VisibilityOff
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.focus.FocusRequester
import androidx.compose.ui.focus.focusRequester
import androidx.compose.ui.graphics.FilterQuality
import androidx.compose.ui.graphics.SolidColor
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalFocusManager
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.LinkAnnotation
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.TextLinkStyles
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardCapitalization
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.text.input.VisualTransformation
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.text.withStyle
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.em
import androidx.compose.ui.unit.sp
import com.digitalgold.ticker.DigitalGoldSite
import com.digitalgold.ticker.persistence.SignupPreferences
import kotlinx.coroutines.delay

private const val INVITE_REVEAL_LAST_STEP = 6

private enum class InviteCopyKind { Username, Link }

private enum class CredentialsFocus { Username, Email, Password, Friend, Verification }

/**
 * Rich 3-step preview of the member path on digitalgold.co.
 * Does not create accounts, take payment, or award DGD.
 * Finish dismisses to the ticker and does not open the browser.
 */
@Composable
fun SignupPreviewScreen(
    prefs: SignupPreferences,
    inviteGeneration: Int = 0,
    onClose: () -> Unit,
) {
    val context = LocalContext.current
    val focusManager = LocalFocusManager.current
    val reduceMotion = remember { context.isReduceMotionEnabled() }
    var step by remember { mutableIntStateOf(1) }
    var username by remember {
        mutableStateOf(DigitalGoldSite.prefilledCredential(prefs.username, prefs.membershipPreviewCompleted))
    }
    var receivingAddress by remember { mutableStateOf(prefs.receivingAddress) }
    var receivingAddressLocked by remember { mutableStateOf(prefs.receivingAddressLocked) }
    var friendCode by remember { mutableStateOf(prefs.friendCode) }
    var copiedReceivingAddress by remember { mutableStateOf(false) }
    var showInviteOptions by remember { mutableStateOf(false) }
    var showInviteQR by remember { mutableStateOf(false) }
    var inviteRevealStep by remember { mutableIntStateOf(0) }
    var copiedInvite by remember { mutableStateOf<InviteCopyKind?>(null) }
    var mailFallbackVisible by remember { mutableStateOf(false) }
    var password by remember {
        mutableStateOf(DigitalGoldSite.prefilledCredential(prefs.password, prefs.membershipPreviewCompleted))
    }
    var showPassword by remember { mutableStateOf(false) }
    var email by remember {
        mutableStateOf(DigitalGoldSite.prefilledCredential(prefs.email, prefs.membershipPreviewCompleted))
    }
    var awaitingEmailVerification by remember { mutableStateOf(false) }
    var verificationCode by remember { mutableStateOf("") }
    var resentFlash by remember { mutableStateOf(false) }
    var showCredentialsErrors by remember { mutableStateOf(false) }
    var showReceiveHelp by remember { mutableStateOf(false) }
    val scroll = rememberScrollState()
    val usernameFocus = remember { FocusRequester() }
    val emailFocus = remember { FocusRequester() }
    val passwordFocus = remember { FocusRequester() }
    val friendFocus = remember { FocusRequester() }
    val verificationFocus = remember { FocusRequester() }

    fun persistUsername(value: String) {
        username = value
        prefs.username = value
        if (value.trim().length < 3) showInviteQR = false
    }

    fun persistAddress(value: String) {
        receivingAddress = value
        prefs.receivingAddress = value
    }

    fun persistLocked(value: Boolean) {
        receivingAddressLocked = value
        prefs.receivingAddressLocked = value
    }

    fun persistEmail(value: String) {
        email = value
        prefs.email = value
    }

    fun persistPassword(value: String) {
        password = value
        prefs.password = value
    }

    fun persistFriend(value: String) {
        friendCode = value
        prefs.friendCode = value
    }

    LaunchedEffect(inviteGeneration) {
        friendCode = prefs.friendCode
    }

    // Apple 2 create flow: username / email / password stay blank until Finish or Log in.
    // Password is not restored from encrypted storage on the create path.
    LaunchedEffect(Unit) {
        if (prefs.membershipPreviewCompleted) {
            prefs.signupMaxReached = DigitalGoldSite.signupMaxReached(
                visiting = DigitalGoldSite.LAST_SIGNUP_STEP,
                currentMax = prefs.signupMaxReached,
                completed = true,
            )
        }
        val completed = prefs.membershipPreviewCompleted
        persistUsername(DigitalGoldSite.prefilledCredential(username, completed))
        persistEmail(DigitalGoldSite.prefilledCredential(email, completed))
        password = DigitalGoldSite.prefilledCredential(
            if (password.isEmpty()) prefs.password else password,
            completed,
        )
    }

    DisposableEffect(Unit) {
        onDispose {
            showInviteOptions = false
            showInviteQR = false
            inviteRevealStep = 0
            showPassword = false
            awaitingEmailVerification = false
            verificationCode = ""
            resentFlash = false
            showCredentialsErrors = false
            showReceiveHelp = false
            mailFallbackVisible = false
        }
    }

    LaunchedEffect(inviteRevealStep) {
        if (inviteRevealStep >= INVITE_REVEAL_LAST_STEP) {
            delay(50)
            scroll.animateScrollTo(scroll.maxValue)
        }
    }

    val trimmedUsername = username.trim()
    val canShareInvite = trimmedUsername.length >= 3
    val isUsernameFilled = trimmedUsername.isNotEmpty()
    val isEmailFilled = email.trim().isNotEmpty()
    val isPasswordFilled = password.trim().isNotEmpty()
    val credentialsComplete = isUsernameFilled && isEmailFilled && isPasswordFilled
    val returningMember = prefs.membershipPreviewCompleted
    val showCredentialsFieldError =
        showCredentialsErrors && step == 1 && !awaitingEmailVerification && !credentialsComplete
    val primaryEnabled = if (awaitingEmailVerification && step == 1) {
        verificationCode.trim().isNotEmpty()
    } else {
        true
    }

    fun moveToStep(n: Int) {
        if (!DigitalGoldSite.isSignupStepUnlocked(n, prefs.signupMaxReached, prefs.membershipPreviewCompleted)) {
            return
        }
        step = n
        prefs.signupMaxReached = DigitalGoldSite.signupMaxReached(
            visiting = n,
            currentMax = prefs.signupMaxReached,
            completed = prefs.membershipPreviewCompleted,
        )
    }

    fun handlePrimary() {
        if (step == 1 && !awaitingEmailVerification) {
            if (returningMember) {
                moveToStep(2)
                return
            }
            if (!credentialsComplete) {
                showCredentialsErrors = true
                return
            }
            showCredentialsErrors = false
            awaitingEmailVerification = true
            return
        }
        if (step == 1 && awaitingEmailVerification) {
            if (verificationCode.trim().isEmpty()) return
            awaitingEmailVerification = false
            verificationCode = ""
            resentFlash = false
            focusManager.clearFocus()
            moveToStep(2)
            return
        }
        if (step < 3) {
            moveToStep(step + 1)
        } else {
            prefs.membershipPreviewCompleted = true
            prefs.signupMaxReached = DigitalGoldSite.LAST_SIGNUP_STEP
            onClose()
        }
    }

    Column(Modifier.fillMaxWidth()) {
        Row(
            Modifier
                .fillMaxWidth()
                .padding(horizontal = 8.dp),
            horizontalArrangement = Arrangement.End,
        ) {
            TextButton(onClick = onClose) {
                Text(LockedCopy.CLOSE, color = GoldTheme.gold, fontWeight = FontWeight.SemiBold)
            }
        }
        Column(
            modifier = Modifier
                .verticalScroll(scroll)
                // imePadding first, then the navigation bar: when the keyboard
                // is up it replaces the nav bar, and applying them in this
                // order stops the two being added together.
                //
                // imePadding matters more than it looks. This is a form with
                // three text fields; without it the soft keyboard covers the
                // field being typed into, which on the password field means
                // typing blind. navigationBarsPadding is what was cutting the
                // password field off at the bottom of the sheet.
                .imePadding()
                .navigationBarsPadding()
                .padding(22.dp),
            verticalArrangement = Arrangement.spacedBy(if (step == 2) 12.dp else 20.dp),
        ) {
            Text(
                text = LockedCopy.PREVIEW_BANNER,
                fontSize = 13.sp,
                fontWeight = FontWeight.SemiBold,
                letterSpacing = 0.16.em,
                color = GoldTheme.gold,
            )
            val showsCredentialsCreateHeaderLock =
                step == 1 && !returningMember && !awaitingEmailVerification
            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                Text(
                    text = if (step == 3) LockedCopy.WELCOME_HEADER else LockedCopy.JOIN_HEADER,
                    fontSize = 26.sp,
                    fontWeight = FontWeight.Medium,
                    fontFamily = FontFamily.Serif,
                    color = GoldTheme.ivory,
                    maxLines = 2,
                )
                if (showsCredentialsCreateHeaderLock) {
                    Text(
                        text = LockedCopy.CREDENTIALS_INTRO,
                        fontSize = 16.sp,
                        fontFamily = FontFamily.Serif,
                        color = GoldTheme.muted,
                    )
                    WaitlistLine(onOpenWaitlist = { context.openWebsite(DigitalGoldSite.WAITLIST) })
                } else {
                    Text(
                        text = when (step) {
                            1 -> LockedCopy.STEP1_SUBTITLE
                            2 -> LockedCopy.STEP2_SUBTITLE
                            else -> LockedCopy.STEP3_SUBTITLE
                        },
                        fontSize = 16.sp,
                        fontFamily = FontFamily.Serif,
                        color = GoldTheme.muted,
                    )
                }
            }
            StepPills(
                step = step,
                maxReached = prefs.signupMaxReached,
                completed = returningMember,
                onSelect = { target ->
                    awaitingEmailVerification = false
                    showInviteOptions = false
                    showInviteQR = false
                    inviteRevealStep = 0
                    moveToStep(target)
                },
            )
            when {
                step == 1 && awaitingEmailVerification -> EmailVerificationStep(
                    email = email,
                    verificationCode = verificationCode,
                    onCode = { verificationCode = it },
                    resentFlash = resentFlash,
                    onResend = { resentFlash = true },
                    focusRequester = verificationFocus,
                    onSubmit = { handlePrimary() },
                )
                step == 1 -> CredentialsStep(
                    username = username,
                    onUsername = ::persistUsername,
                    email = email,
                    onEmail = ::persistEmail,
                    password = password,
                    onPassword = ::persistPassword,
                    showPassword = showPassword,
                    onTogglePassword = { showPassword = !showPassword },
                    friendCode = friendCode,
                    onFriendCode = ::persistFriend,
                    readOnly = returningMember,
                    showError = showCredentialsFieldError,
                    usernameFilled = isUsernameFilled,
                    emailFilled = isEmailFilled,
                    passwordFilled = isPasswordFilled,
                    usernameFocus = usernameFocus,
                    emailFocus = emailFocus,
                    passwordFocus = passwordFocus,
                    friendFocus = friendFocus,
                    onAdvance = { target ->
                        when (target) {
                            CredentialsFocus.Email -> emailFocus.requestFocus()
                            CredentialsFocus.Password -> passwordFocus.requestFocus()
                            else -> focusManager.clearFocus()
                        }
                    },
                    onOpenSite = { context.openWebsite(DigitalGoldSite.HOME) },
                )
                step == 2 -> WalletStep(onOpenSite = { context.openWebsite(DigitalGoldSite.HOME) })
                else -> ReceiveStep(
                    receivingAddress = receivingAddress,
                    locked = receivingAddressLocked,
                    copied = copiedReceivingAddress,
                    showHelp = showReceiveHelp,
                    onToggleHelp = { showReceiveHelp = !showReceiveHelp },
                    onAddressChange = ::persistAddress,
                    onSave = {
                        val trimmed = receivingAddress.trim()
                        if (trimmed.isNotEmpty()) {
                            persistAddress(trimmed)
                            persistLocked(true)
                            focusManager.clearFocus()
                        }
                    },
                    onEdit = { persistLocked(false) },
                    onClear = {
                        persistAddress("")
                        persistLocked(false)
                    },
                    onCopy = {
                        val value = receivingAddress.trim()
                        if (value.isNotEmpty()) {
                            context.copyToClipboard(value)
                            copiedReceivingAddress = true
                        }
                    },
                    onOpenSite = { context.openWebsite(DigitalGoldSite.HOME) },
                )
            }
            if (copiedReceivingAddress) {
                LaunchedEffect(copiedReceivingAddress) {
                    delay(1_400)
                    copiedReceivingAddress = false
                }
            }
            if (resentFlash) {
                LaunchedEffect(resentFlash) {
                    delay(1_400)
                    resentFlash = false
                }
            }
            Column(verticalArrangement = Arrangement.spacedBy(10.dp)) {
                if (step == 3) {
                    InviteFriendsSection(
                        canShareInvite = canShareInvite,
                        showInviteOptions = showInviteOptions,
                        showInviteQR = showInviteQR,
                        inviteRevealStep = inviteRevealStep,
                        copiedInvite = copiedInvite,
                        inviteUrl = DigitalGoldSite.appInviteURL(trimmedUsername),
                        onToggle = {
                            if (showInviteOptions) {
                                showInviteOptions = false
                                showInviteQR = false
                                inviteRevealStep = 0
                            } else {
                                showInviteOptions = true
                                if (reduceMotion) {
                                    inviteRevealStep = INVITE_REVEAL_LAST_STEP
                                }
                            }
                        },
                        onToggleQR = { showInviteQR = !showInviteQR },
                        onGoToCredentials = {
                            awaitingEmailVerification = false
                            showInviteOptions = false
                            showInviteQR = false
                            inviteRevealStep = 0
                            moveToStep(1)
                        },
                        onCopy = { kind ->
                            val value = when (kind) {
                                InviteCopyKind.Username -> if (canShareInvite) trimmedUsername else return@InviteFriendsSection
                                InviteCopyKind.Link -> DigitalGoldSite.inviteLinkURL(trimmedUsername)
                                    ?: return@InviteFriendsSection
                            }
                            context.copyToClipboard(value)
                            copiedInvite = kind
                        },
                        onEmail = {
                            val route = InviteSharePresenter.presentEmail(context, trimmedUsername)
                            if (route == InviteEmailFallback.Route.COPY_AND_ALERT) {
                                mailFallbackVisible = true
                            }
                        },
                        onSocial = { network ->
                            InviteSharePresenter.presentSocial(context, network, trimmedUsername)
                        },
                        onOpenSite = { context.openWebsite(DigitalGoldSite.HOME) },
                    )
                }
                if (showCredentialsFieldError) {
                    Text(
                        text = LockedCopy.CREDENTIALS_ERROR,
                        fontSize = 14.sp,
                        fontFamily = FontFamily.Serif,
                        color = GoldTheme.danger,
                    )
                }
                if (returningMember && step == 1 && !awaitingEmailVerification) {
                    TextButton(
                        onClick = {
                            prefs.clearLoggedInSession()
                            onClose()
                        },
                        modifier = Modifier.fillMaxWidth(),
                    ) {
                        Text(
                            LockedCopy.LOG_OUT,
                            color = GoldTheme.gold,
                            fontWeight = FontWeight.SemiBold,
                            fontSize = 16.sp,
                        )
                    }
                }
                Button(
                    onClick = { handlePrimary() },
                    enabled = primaryEnabled,
                    modifier = Modifier
                        .fillMaxWidth()
                        .alpha(if (primaryEnabled) 1f else 0.55f),
                    shape = RoundedCornerShape(8.dp),
                    colors = ButtonDefaults.buttonColors(
                        containerColor = GoldTheme.gold,
                        contentColor = GoldTheme.backgroundBottom,
                        disabledContainerColor = GoldTheme.gold,
                        disabledContentColor = GoldTheme.backgroundBottom,
                    ),
                ) {
                    Text(
                        text = LockedCopy.previewPrimaryLabel(step, awaitingEmailVerification),
                        fontSize = 18.sp,
                        fontWeight = FontWeight.SemiBold,
                        modifier = Modifier.padding(vertical = 4.dp),
                    )
                }
            }
        }
    }

    if (showInviteOptions && !reduceMotion && inviteRevealStep < INVITE_REVEAL_LAST_STEP) {
        LaunchedEffect(showInviteOptions) {
            inviteRevealStep = 1
            for (next in 2..INVITE_REVEAL_LAST_STEP) {
                delay(if (next == 2) 180 else 200)
                if (!showInviteOptions) return@LaunchedEffect
                inviteRevealStep = next
            }
        }
    }
    if (mailFallbackVisible) {
        AlertDialog(
            onDismissRequest = { mailFallbackVisible = false },
            confirmButton = {
                TextButton(onClick = { mailFallbackVisible = false }) {
                    Text("OK", color = GoldTheme.gold)
                }
            },
            text = {
                Text(
                    text = InviteEmailFallback.UNAVAILABLE_ALERT,
                    fontFamily = FontFamily.Serif,
                    color = GoldTheme.ivory,
                )
            },
            containerColor = GoldTheme.backgroundBottom,
        )
    }
    if (copiedInvite != null) {
        LaunchedEffect(copiedInvite) {
            delay(1_400)
            copiedInvite = null
        }
    }
}

/**
 * Compact local-only log-in. Same membership flag + credential persistence as Finish.
 * Does not run Wallet, Receive, or email-verify. Banner keeps this from looking live.
 */
@Composable
fun LoginPreviewScreen(
    prefs: SignupPreferences,
    onClose: () -> Unit,
    onJoinNetwork: () -> Unit = {},
) {
    val focusManager = LocalFocusManager.current
    var identifier by remember { mutableStateOf("") }
    var password by remember { mutableStateOf("") }
    var showPassword by remember { mutableStateOf(false) }
    var showError by remember { mutableStateOf(false) }
    val identifierFocus = remember { FocusRequester() }
    val passwordFocus = remember { FocusRequester() }
    val identifierFilled = identifier.trim().isNotEmpty()
    val passwordFilled = password.trim().isNotEmpty()
    val canContinue = identifierFilled && passwordFilled

    fun handleContinue() {
        if (!canContinue) {
            showError = true
            return
        }
        if (!prefs.persistLoginIdentifier(identifier, password)) {
            showError = true
            return
        }
        focusManager.clearFocus()
        onClose()
    }

    DisposableEffect(Unit) {
        onDispose {
            showPassword = false
            showError = false
        }
    }

    Column(Modifier.fillMaxWidth()) {
        Row(
            Modifier
                .fillMaxWidth()
                .padding(horizontal = 8.dp),
            horizontalArrangement = Arrangement.End,
        ) {
            TextButton(onClick = onClose) {
                Text(LockedCopy.CLOSE, color = GoldTheme.gold, fontWeight = FontWeight.SemiBold)
            }
        }
        Column(
            modifier = Modifier.padding(22.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp),
        ) {
            Text(
                text = LockedCopy.PREVIEW_BANNER,
                fontSize = 13.sp,
                fontWeight = FontWeight.SemiBold,
                letterSpacing = 0.16.em,
                color = GoldTheme.gold,
            )
            Text(
                text = LockedCopy.LOGIN_TITLE,
                fontSize = 26.sp,
                fontWeight = FontWeight.Medium,
                fontFamily = FontFamily.Serif,
                color = GoldTheme.ivory,
            )
            LiveField(
                title = LockedCopy.LOGIN_IDENTIFIER_LABEL,
                value = identifier,
                onValueChange = { identifier = it },
                placeholder = LockedCopy.LOGIN_IDENTIFIER_PLACEHOLDER,
                footnote = null,
                showError = showError && !identifierFilled,
                focusRequester = identifierFocus,
                keyboardType = KeyboardType.Email,
                imeAction = ImeAction.Next,
                onIme = { passwordFocus.requestFocus() },
            )
            PasswordField(
                title = LockedCopy.PASSWORD_LABEL,
                value = password,
                onValueChange = { password = it },
                visible = showPassword,
                onToggle = { showPassword = !showPassword },
                showError = showError && !passwordFilled,
                focusRequester = passwordFocus,
                onIme = { handleContinue() },
            )
            Row(verticalAlignment = Alignment.Bottom) {
                Text(
                    text = LockedCopy.DONT_HAVE_ACCOUNT,
                    fontSize = 15.sp,
                    fontFamily = FontFamily.Serif,
                    color = GoldTheme.muted,
                )
                TextButton(onClick = onJoinNetwork) {
                    Text(
                        text = LockedCopy.JOIN_THE_NETWORK,
                        fontSize = 15.sp,
                        fontFamily = FontFamily.Serif,
                        color = GoldTheme.gold,
                    )
                }
            }
            if (showError && !canContinue) {
                Text(
                    text = LockedCopy.LOGIN_ERROR,
                    fontSize = 14.sp,
                    fontFamily = FontFamily.Serif,
                    color = GoldTheme.danger,
                )
            }
            Button(
                onClick = { handleContinue() },
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(8.dp),
                colors = ButtonDefaults.buttonColors(
                    containerColor = GoldTheme.gold,
                    contentColor = GoldTheme.backgroundBottom,
                ),
            ) {
                Text(
                    text = LockedCopy.CONTINUE,
                    fontSize = 18.sp,
                    fontWeight = FontWeight.SemiBold,
                    modifier = Modifier.padding(vertical = 4.dp),
                )
            }
        }
    }
}

@Composable
private fun StepPills(
    step: Int,
    maxReached: Int,
    completed: Boolean,
    onSelect: (Int) -> Unit,
) {
    Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
        Pill(1, LockedCopy.PILL_CREDENTIALS, step == 1, maxReached, completed, onSelect, Modifier.weight(1f))
        Pill(2, LockedCopy.PILL_WALLET, step == 2, maxReached, completed, onSelect, Modifier.weight(1f))
        Pill(3, LockedCopy.PILL_RECEIVE, step == 3, maxReached, completed, onSelect, Modifier.weight(1f))
    }
}

@Composable
private fun Pill(
    n: Int,
    title: String,
    on: Boolean,
    maxReached: Int,
    completed: Boolean,
    onSelect: (Int) -> Unit,
    modifier: Modifier = Modifier,
) {
    val unlocked = DigitalGoldSite.isSignupStepUnlocked(n, maxReached, completed)
    Row(
        modifier = modifier
            .alpha(if (on || unlocked) 1f else 0.62f)
            .background(
                if (on) GoldTheme.gold else GoldTheme.gold.copy(alpha = 0.12f),
                RoundedCornerShape(8.dp),
            )
            .then(
                if (unlocked) Modifier.clickable(onClick = { onSelect(n) }) else Modifier,
            )
            .padding(horizontal = 6.dp, vertical = 7.dp)
            .semantics {
                contentDescription = if (unlocked) {
                    "Shows the $title preview step"
                } else {
                    "Locked until you reach this step"
                }
            },
        horizontalArrangement = Arrangement.Center,
        verticalAlignment = Alignment.CenterVertically,
    ) {
        // The three pills are equal thirds, so the widest label decides the
        // budget. "1 Credentials" at 14sp did not fit in a third of a 411dp
        // screen, and with maxLines = 1 and the default Clip overflow it was
        // cut down to a bare "1" — while "2 Wallet" and "3 Receive" rendered
        // fine, which is what made it look deliberate rather than broken.
        //
        // Smaller type and tighter padding make it fit; Ellipsis is the
        // backstop so a narrower phone degrades to "1 Creden…" rather than
        // silently losing the word.
        Text(
            text = "$n $title",
            fontSize = 12.sp,
            fontWeight = FontWeight.SemiBold,
            color = if (on) GoldTheme.backgroundBottom else GoldTheme.muted,
            maxLines = 1,
            overflow = TextOverflow.Ellipsis,
        )
    }
}

@Composable
private fun CredentialsStep(
    username: String,
    onUsername: (String) -> Unit,
    email: String,
    onEmail: (String) -> Unit,
    password: String,
    onPassword: (String) -> Unit,
    showPassword: Boolean,
    onTogglePassword: () -> Unit,
    friendCode: String,
    onFriendCode: (String) -> Unit,
    readOnly: Boolean,
    showError: Boolean,
    usernameFilled: Boolean,
    emailFilled: Boolean,
    passwordFilled: Boolean,
    usernameFocus: FocusRequester,
    emailFocus: FocusRequester,
    passwordFocus: FocusRequester,
    friendFocus: FocusRequester,
    onAdvance: (CredentialsFocus?) -> Unit,
    onOpenSite: () -> Unit,
) {
    Column(verticalArrangement = Arrangement.spacedBy(16.dp)) {
        Text(
            text = if (readOnly) LockedCopy.YOUR_CREDENTIALS else LockedCopy.CREDENTIALS_TITLE,
            fontSize = 20.sp,
            fontWeight = FontWeight.Medium,
            fontFamily = FontFamily.Serif,
            color = GoldTheme.ivory,
        )
        Text(
            text = LockedCopy.CREDENTIALS_BODY,
            fontSize = 15.sp,
            fontFamily = FontFamily.Serif,
            color = GoldTheme.muted,
        )
        LiveField(
            title = LockedCopy.USERNAME_LABEL,
            value = username,
            onValueChange = onUsername,
            placeholder = LockedCopy.USERNAME_PLACEHOLDER,
            footnote = LockedCopy.USERNAME_FOOTNOTE,
            showError = showError && !usernameFilled,
            readOnly = readOnly,
            focusRequester = usernameFocus,
            imeAction = ImeAction.Next,
            onIme = { onAdvance(CredentialsFocus.Email) },
        )
        LiveField(
            title = LockedCopy.EMAIL_LABEL,
            value = email,
            onValueChange = onEmail,
            placeholder = LockedCopy.EMAIL_PLACEHOLDER,
            footnote = LockedCopy.EMAIL_FOOTNOTE,
            placeholderColor = GoldTheme.gold,
            showError = showError && !emailFilled,
            readOnly = readOnly,
            focusRequester = emailFocus,
            keyboardType = KeyboardType.Email,
            imeAction = ImeAction.Next,
            onIme = { onAdvance(CredentialsFocus.Password) },
        )
        PasswordField(
            title = LockedCopy.PASSWORD_LABEL,
            value = password,
            onValueChange = onPassword,
            visible = showPassword,
            onToggle = onTogglePassword,
            showError = showError && !passwordFilled,
            readOnly = readOnly,
            focusRequester = passwordFocus,
            onIme = { onAdvance(null) },
        )
        if (!readOnly || friendCode.trim().isNotEmpty()) {
            Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
                FieldLabel(LockedCopy.FRIEND_LABEL)
                Box(
                    Modifier
                        .fillMaxWidth()
                        .background(GoldTheme.gold.copy(alpha = 0.08f), RoundedCornerShape(8.dp))
                        .padding(12.dp),
                ) {
                    GoldTextField(
                        value = friendCode,
                        onValueChange = onFriendCode,
                        placeholder = LockedCopy.FRIEND_PLACEHOLDER,
                        modifier = Modifier
                            .fillMaxWidth()
                            .focusRequester(friendFocus),
                        readOnly = readOnly,
                        imeAction = ImeAction.Done,
                        onIme = { onAdvance(null) },
                    )
                }
                if (!readOnly) {
                    SiteLinkLine(
                        prefix = LockedCopy.FRIEND_LEARN_PREFIX,
                        prefixColor = GoldTheme.muted,
                        onClick = onOpenSite,
                    )
                }
            }
        }
    }
}

@Composable
private fun EmailVerificationStep(
    email: String,
    verificationCode: String,
    onCode: (String) -> Unit,
    resentFlash: Boolean,
    onResend: () -> Unit,
    focusRequester: FocusRequester,
    onSubmit: () -> Unit,
) {
    val displayed = email.trim().ifEmpty { LockedCopy.VERIFY_FALLBACK_EMAIL }
    LaunchedEffect(Unit) {
        runCatching { focusRequester.requestFocus() }
    }
    Column(verticalArrangement = Arrangement.spacedBy(16.dp)) {
        Text(
            text = LockedCopy.VERIFY_TITLE,
            fontSize = 20.sp,
            fontWeight = FontWeight.Medium,
            fontFamily = FontFamily.Serif,
            color = GoldTheme.ivory,
        )
        Text(
            text = LockedCopy.VERIFY_PREFIX + displayed + LockedCopy.VERIFY_SUFFIX,
            fontSize = 15.sp,
            fontFamily = FontFamily.Serif,
            color = GoldTheme.muted,
        )
        LiveField(
            title = LockedCopy.VERIFY_CODE_LABEL,
            value = verificationCode,
            onValueChange = onCode,
            placeholder = LockedCopy.VERIFY_CODE_PLACEHOLDER,
            footnote = null,
            focusRequester = focusRequester,
            imeAction = ImeAction.Go,
            onIme = onSubmit,
        )
        Text(
            text = LockedCopy.VERIFY_SPAM,
            fontSize = 14.sp,
            fontFamily = FontFamily.Serif,
            color = GoldTheme.muted,
        )
        Text(
            text = if (resentFlash) LockedCopy.SENT_AGAIN else LockedCopy.RESEND,
            fontSize = 16.sp,
            fontWeight = FontWeight.SemiBold,
            color = GoldTheme.gold,
            modifier = Modifier
                .clickable(onClick = onResend)
                .semantics {
                    contentDescription = "Demo only. This app does not send email."
                },
        )
    }
}

@Composable
private fun WalletStep(onOpenSite: () -> Unit) {
    Column(verticalArrangement = Arrangement.spacedBy(10.dp)) {
        Text(
            text = LockedCopy.WALLET_TITLE,
            fontSize = 20.sp,
            fontWeight = FontWeight.Medium,
            fontFamily = FontFamily.Serif,
            color = GoldTheme.ivory,
        )
        Text(
            text = LockedCopy.WALLET_BODY,
            fontSize = 15.sp,
            fontFamily = FontFamily.Serif,
            color = GoldTheme.muted,
        )
        OsRow(LockedCopy.OS_WINDOWS, LockedCopy.OS_WINDOWS_DETAIL)
        OsRow(LockedCopy.OS_MAC, LockedCopy.OS_MAC_DETAIL)
        OsRow(LockedCopy.OS_LINUX, LockedCopy.OS_LINUX_DETAIL)
        Text(
            text = LockedCopy.WALLET_DOWNLOAD,
            fontSize = 20.sp,
            fontWeight = FontWeight.SemiBold,
            fontFamily = FontFamily.Serif,
            color = GoldTheme.gold,
            modifier = Modifier
                .fillMaxWidth()
                .clickable(onClick = onOpenSite),
        )
    }
}

@Composable
private fun ReceiveStep(
    receivingAddress: String,
    locked: Boolean,
    copied: Boolean,
    showHelp: Boolean,
    onToggleHelp: () -> Unit,
    onAddressChange: (String) -> Unit,
    onSave: () -> Unit,
    onEdit: () -> Unit,
    onClear: () -> Unit,
    onCopy: () -> Unit,
    onOpenSite: () -> Unit,
) {
    Column(verticalArrangement = Arrangement.spacedBy(16.dp)) {
        Text(
            text = LockedCopy.RECEIVE_TITLE,
            fontSize = 20.sp,
            fontWeight = FontWeight.Medium,
            fontFamily = FontFamily.Serif,
            color = GoldTheme.ivory,
        )
        SiteLinkLine(
            prefix = LockedCopy.RECEIVE_PREFIX,
            suffix = LockedCopy.RECEIVE_SUFFIX,
            prefixColor = GoldTheme.ivory.copy(alpha = 0.9f),
            suffixColor = GoldTheme.ivory.copy(alpha = 0.9f),
            fontSize = 16.sp,
            onClick = onOpenSite,
        )
        Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(
                    text = LockedCopy.QT_ADDRESS_LABEL,
                    fontSize = 16.sp,
                    fontWeight = FontWeight.SemiBold,
                    color = GoldTheme.gold,
                )
                IconButton(onClick = onToggleHelp, modifier = Modifier.size(28.dp)) {
                    Icon(
                        imageVector = Icons.Outlined.Info,
                        contentDescription = if (showHelp) {
                            "Hide receiving address help"
                        } else {
                            "Show receiving address help"
                        },
                        tint = GoldTheme.gold,
                    )
                }
            }
            Text(
                text = LockedCopy.QT_ADDRESS_NOTE,
                fontSize = 14.sp,
                fontFamily = FontFamily.Serif,
                color = GoldTheme.muted,
            )
            if (showHelp) {
                Text(
                    text = buildAnnotatedString {
                        append(LockedCopy.QT_HELP_BEFORE)
                        withStyle(SpanStyle(fontWeight = FontWeight.Bold)) {
                            append(LockedCopy.QT_HELP_RECEIVE)
                        }
                        append(LockedCopy.QT_HELP_MID)
                        withStyle(SpanStyle(fontWeight = FontWeight.Bold)) {
                            append(LockedCopy.QT_HELP_CREATE)
                        }
                        append(LockedCopy.QT_HELP_AFTER)
                    },
                    fontSize = 14.sp,
                    fontFamily = FontFamily.Serif,
                    color = GoldTheme.muted,
                )
            }
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(GoldTheme.gold.copy(alpha = 0.08f), RoundedCornerShape(8.dp))
                    .padding(12.dp),
                verticalAlignment = Alignment.Top,
            ) {
                if (locked) {
                    Text(
                        text = receivingAddress,
                        fontSize = 16.sp,
                        fontFamily = FontFamily.Serif,
                        color = GoldTheme.ivory,
                        modifier = Modifier.weight(1f),
                    )
                } else {
                    GoldTextField(
                        value = receivingAddress,
                        onValueChange = onAddressChange,
                        placeholder = LockedCopy.ADDRESS_PLACEHOLDER,
                        modifier = Modifier.weight(1f),
                        singleLine = false,
                        fontSize = 16.sp,
                    )
                }
                if (receivingAddress.trim().isNotEmpty()) {
                    IconButton(onClick = onCopy, modifier = Modifier.size(28.dp)) {
                        Icon(
                            imageVector = if (copied) Icons.Outlined.Check else Icons.Outlined.ContentCopy,
                            contentDescription = if (copied) LockedCopy.COPIED else "Copy receiving address",
                            tint = GoldTheme.gold,
                        )
                    }
                }
            }
            if (receivingAddress.trim().isNotEmpty() && !locked) {
                Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    AddressAction(LockedCopy.SAVE, filled = true, onClick = onSave)
                    AddressAction(LockedCopy.CLEAR, filled = false, onClick = onClear)
                }
            } else if (locked) {
                AddressAction(LockedCopy.EDIT, filled = true, onClick = onEdit)
            }
        }
    }
}

@Composable
private fun InviteFriendsSection(
    canShareInvite: Boolean,
    showInviteOptions: Boolean,
    showInviteQR: Boolean,
    inviteRevealStep: Int,
    copiedInvite: InviteCopyKind?,
    inviteUrl: String?,
    onToggle: () -> Unit,
    onToggleQR: () -> Unit,
    onGoToCredentials: () -> Unit,
    onCopy: (InviteCopyKind) -> Unit,
    onEmail: () -> Unit,
    onSocial: (InviteSocialNetwork) -> Unit,
    onOpenSite: () -> Unit,
) {
    Column(verticalArrangement = Arrangement.spacedBy(10.dp)) {
        SiteLinkLine(
            prefix = LockedCopy.INVITE_LEAD_PREFIX,
            prefixColor = GoldTheme.gold,
            fontSize = 18.sp,
            fontWeight = FontWeight.SemiBold,
            onClick = onOpenSite,
        )
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .background(GoldTheme.backgroundBottom, RoundedCornerShape(8.dp))
                .border(1.5.dp, GoldTheme.gold, RoundedCornerShape(8.dp))
                .clickable(onClick = onToggle)
                .padding(vertical = 14.dp),
            contentAlignment = Alignment.Center,
        ) {
            Text(
                text = LockedCopy.INVITE_FRIENDS,
                fontSize = 18.sp,
                fontWeight = FontWeight.SemiBold,
                color = GoldTheme.gold,
            )
        }
        if (showInviteOptions) {
            AnimatedVisibility(
                visible = inviteRevealStep >= 1,
                enter = fadeIn() + slideInVertically { it / 6 },
                exit = fadeOut(),
            ) {
                if (canShareInvite) {
                    Text(
                        text = LockedCopy.INVITE_HINT,
                        fontSize = 14.sp,
                        fontFamily = FontFamily.Serif,
                        color = GoldTheme.muted,
                    )
                } else {
                    Column(verticalArrangement = Arrangement.spacedBy(10.dp)) {
                        Text(
                            text = LockedCopy.INVITE_NEED_USERNAME,
                            fontSize = 14.sp,
                            fontFamily = FontFamily.Serif,
                            color = GoldTheme.muted,
                        )
                        Text(
                            text = LockedCopy.GO_TO_CREDENTIALS,
                            fontSize = 16.sp,
                            fontWeight = FontWeight.SemiBold,
                            color = GoldTheme.gold,
                            modifier = Modifier.clickable(onClick = onGoToCredentials),
                        )
                    }
                }
            }
            AnimatedVisibility(
                visible = inviteRevealStep >= 2,
                enter = fadeIn() + slideInVertically { it / 6 },
                exit = fadeOut(),
            ) {
                InviteSocialsRow(
                    enabled = canShareInvite,
                    onSocial = onSocial,
                )
            }
            AnimatedVisibility(
                visible = inviteRevealStep >= 3,
                enter = fadeIn() + slideInVertically { it / 6 },
                exit = fadeOut(),
            ) {
                DisplayQRSection(
                    enabled = canShareInvite,
                    showing = showInviteQR,
                    url = inviteUrl,
                    onToggle = onToggleQR,
                )
            }
            AnimatedVisibility(
                visible = inviteRevealStep >= 4,
                enter = fadeIn() + slideInVertically { it / 6 },
                exit = fadeOut(),
            ) {
                InviteShareButton(
                    title = LockedCopy.INVITE_EMAIL,
                    enabled = canShareInvite,
                    onClick = onEmail,
                )
            }
            AnimatedVisibility(
                visible = inviteRevealStep >= 5,
                enter = fadeIn() + slideInVertically { it / 6 },
                exit = fadeOut(),
            ) {
                InviteCopyButton(
                    title = LockedCopy.COPY_INVITE_LINK,
                    copied = copiedInvite == InviteCopyKind.Link,
                    enabled = canShareInvite,
                    onClick = { onCopy(InviteCopyKind.Link) },
                )
            }
            AnimatedVisibility(
                visible = inviteRevealStep >= 6,
                enter = fadeIn() + slideInVertically { it / 6 },
                exit = fadeOut(),
            ) {
                InviteCopyButton(
                    title = LockedCopy.COPY_INVITE_CODE,
                    copied = copiedInvite == InviteCopyKind.Username,
                    enabled = canShareInvite,
                    onClick = { onCopy(InviteCopyKind.Username) },
                )
            }
        }
    }
}

@Composable
private fun InviteSocialsRow(
    enabled: Boolean,
    onSocial: (InviteSocialNetwork) -> Unit,
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp),
        horizontalArrangement = Arrangement.spacedBy(36.dp, Alignment.CenterHorizontally),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        InviteSocialNetwork.entries.forEach { network ->
            Box(
                modifier = Modifier
                    .size(44.dp)
                    .alpha(if (enabled) 1f else 0.55f)
                    .clickable(enabled = enabled, onClick = { onSocial(network) })
                    .semantics { contentDescription = network.title },
                contentAlignment = Alignment.Center,
            ) {
                InviteSocialMark(
                    network = network,
                    modifier = Modifier.size(28.dp),
                )
            }
        }
    }
}

@Composable
private fun InviteShareButton(
    title: String,
    enabled: Boolean,
    onClick: () -> Unit,
) {
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .alpha(if (enabled) 1f else 0.55f)
            .background(GoldTheme.backgroundBottom, RoundedCornerShape(8.dp))
            .border(1.5.dp, GoldTheme.gold, RoundedCornerShape(8.dp))
            .clickable(enabled = enabled, onClick = onClick)
            .padding(vertical = 12.dp),
        contentAlignment = Alignment.Center,
    ) {
        Text(
            text = title,
            fontSize = 16.sp,
            fontWeight = FontWeight.SemiBold,
            color = GoldTheme.gold,
        )
    }
}

@Composable
private fun DisplayQRSection(
    enabled: Boolean,
    showing: Boolean,
    url: String?,
    onToggle: () -> Unit,
) {
    Column(verticalArrangement = Arrangement.spacedBy(10.dp)) {
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .alpha(if (enabled) 1f else 0.55f)
                .background(GoldTheme.backgroundBottom, RoundedCornerShape(8.dp))
                .border(1.5.dp, GoldTheme.gold, RoundedCornerShape(8.dp))
                .clickable(enabled = enabled, onClick = onToggle)
                .padding(vertical = 12.dp),
            contentAlignment = Alignment.Center,
        ) {
            Text(
                text = LockedCopy.DISPLAY_QR,
                fontSize = 16.sp,
                fontWeight = FontWeight.SemiBold,
                color = GoldTheme.gold,
            )
        }
        if (showing && enabled && url != null) {
            val qr = remember(url) { InviteQRCode.bitmap(url) }
            if (qr != null) {
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(GoldTheme.backgroundBottom, RoundedCornerShape(8.dp))
                        .border(1.dp, GoldTheme.gold.copy(alpha = 0.35f), RoundedCornerShape(8.dp))
                        .padding(16.dp),
                    contentAlignment = Alignment.Center,
                ) {
                    Image(
                        bitmap = qr.asImageBitmap(),
                        contentDescription = "QR code",
                        modifier = Modifier.size(196.dp),
                        contentScale = ContentScale.Fit,
                        // Draw the already-colorized bitmap as-is (Apple 2 interpolation(.none)).
                        // Do not ColorFilter.tint — both module colors are opaque.
                        filterQuality = FilterQuality.None,
                        colorFilter = null,
                    )
                }
            }
        }
    }
}

@Composable
private fun InviteCopyButton(
    title: String,
    copied: Boolean,
    enabled: Boolean,
    onClick: () -> Unit,
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .alpha(if (enabled) 1f else 0.55f)
            .background(GoldTheme.backgroundBottom, RoundedCornerShape(8.dp))
            .border(1.5.dp, GoldTheme.gold, RoundedCornerShape(8.dp))
            .clickable(enabled = enabled, onClick = onClick)
            .padding(vertical = 12.dp),
        horizontalArrangement = Arrangement.Center,
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Text(
            text = if (copied) LockedCopy.COPIED else title,
            fontSize = 16.sp,
            fontWeight = FontWeight.SemiBold,
            color = GoldTheme.gold,
        )
        Icon(
            imageVector = if (copied) Icons.Outlined.Check else Icons.Outlined.ContentCopy,
            contentDescription = null,
            tint = GoldTheme.gold,
            modifier = Modifier
                .padding(start = 8.dp)
                .size(18.dp),
        )
    }
}

@Composable
private fun AddressAction(title: String, filled: Boolean, onClick: () -> Unit) {
    Box(
        modifier = Modifier
            .background(
                if (filled) GoldTheme.gold else GoldTheme.gold.copy(alpha = 0.12f),
                RoundedCornerShape(6.dp),
            )
            .then(
                if (filled) Modifier else Modifier.border(1.dp, GoldTheme.gold, RoundedCornerShape(6.dp)),
            )
            .clickable(onClick = onClick)
            .padding(horizontal = 12.dp, vertical = 6.dp),
    ) {
        Text(
            text = title,
            fontSize = 14.sp,
            fontWeight = FontWeight.SemiBold,
            color = if (filled) GoldTheme.backgroundBottom else GoldTheme.gold,
        )
    }
}

@Composable
private fun OsRow(name: String, detail: String) {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .background(GoldTheme.gold.copy(alpha = 0.08f), RoundedCornerShape(8.dp))
            .padding(12.dp),
    ) {
        Text(
            text = name,
            fontSize = 18.sp,
            fontWeight = FontWeight.Medium,
            fontFamily = FontFamily.Serif,
            color = GoldTheme.ivory,
        )
        Text(
            text = detail,
            fontSize = 14.sp,
            color = GoldTheme.muted,
        )
    }
}

@Composable
private fun LiveField(
    title: String,
    value: String,
    onValueChange: (String) -> Unit,
    placeholder: String,
    footnote: String?,
    placeholderColor: androidx.compose.ui.graphics.Color = GoldTheme.muted,
    showError: Boolean = false,
    readOnly: Boolean = false,
    focusRequester: FocusRequester? = null,
    keyboardType: KeyboardType = KeyboardType.Text,
    imeAction: ImeAction = ImeAction.Next,
    onIme: (() -> Unit)? = null,
) {
    Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
        FieldLabel(title)
        Box(
            Modifier
                .fillMaxWidth()
                .background(GoldTheme.gold.copy(alpha = 0.08f), RoundedCornerShape(8.dp))
                .then(
                    if (showError) Modifier.border(1.5.dp, GoldTheme.danger, RoundedCornerShape(8.dp))
                    else Modifier,
                )
                .padding(12.dp),
        ) {
            GoldTextField(
                value = value,
                onValueChange = onValueChange,
                placeholder = placeholder,
                placeholderColor = placeholderColor,
                modifier = Modifier
                    .fillMaxWidth()
                    .then(if (focusRequester != null) Modifier.focusRequester(focusRequester) else Modifier),
                readOnly = readOnly,
                keyboardType = keyboardType,
                imeAction = imeAction,
                onIme = onIme,
            )
        }
        if (footnote != null) {
            Text(
                text = footnote,
                fontSize = 14.sp,
                fontFamily = FontFamily.Serif,
                color = GoldTheme.muted,
                // Was maxLines = 1, which silently cut the username footnote
                // to "Username is your invite code. 3+ characters," — losing
                // "no spaces.", which is the half that states a rule. A
                // footnote should wrap.
            )
        }
    }
}

@Composable
private fun PasswordField(
    title: String,
    value: String,
    onValueChange: (String) -> Unit,
    visible: Boolean,
    onToggle: () -> Unit,
    showError: Boolean,
    readOnly: Boolean = false,
    focusRequester: FocusRequester,
    onIme: () -> Unit,
) {
    Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
        FieldLabel(title)
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .background(GoldTheme.gold.copy(alpha = 0.08f), RoundedCornerShape(8.dp))
                .then(
                    if (showError) Modifier.border(1.5.dp, GoldTheme.danger, RoundedCornerShape(8.dp))
                    else Modifier,
                )
                .padding(12.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            GoldTextField(
                value = value,
                onValueChange = onValueChange,
                placeholder = LockedCopy.PASSWORD_PLACEHOLDER,
                modifier = Modifier
                    .weight(1f)
                    .focusRequester(focusRequester),
                readOnly = readOnly,
                visualTransformation = if (visible) VisualTransformation.None else PasswordVisualTransformation(),
                keyboardType = KeyboardType.Password,
                imeAction = ImeAction.Go,
                onIme = onIme,
            )
            IconButton(onClick = onToggle, modifier = Modifier.size(28.dp)) {
                Icon(
                    imageVector = if (visible) Icons.Outlined.VisibilityOff else Icons.Outlined.Visibility,
                    contentDescription = if (visible) "Hide ${title.lowercase()}" else "Show ${title.lowercase()}",
                    tint = GoldTheme.gold,
                )
            }
        }
    }
}

@Composable
private fun FieldLabel(text: String) {
    Text(
        text = text,
        fontSize = 14.sp,
        fontWeight = FontWeight.SemiBold,
        color = GoldTheme.gold,
    )
}

@Composable
private fun GoldTextField(
    value: String,
    onValueChange: (String) -> Unit,
    placeholder: String,
    modifier: Modifier = Modifier,
    singleLine: Boolean = true,
    readOnly: Boolean = false,
    placeholderColor: androidx.compose.ui.graphics.Color = GoldTheme.muted,
    visualTransformation: VisualTransformation = VisualTransformation.None,
    keyboardType: KeyboardType = KeyboardType.Text,
    imeAction: ImeAction = ImeAction.Next,
    onIme: (() -> Unit)? = null,
    fontSize: androidx.compose.ui.unit.TextUnit = 18.sp,
) {
    BasicTextField(
        value = value,
        onValueChange = if (readOnly) { {} } else onValueChange,
        modifier = modifier,
        readOnly = readOnly,
        singleLine = singleLine,
        textStyle = androidx.compose.ui.text.TextStyle(
            color = GoldTheme.ivory,
            fontSize = fontSize,
            fontFamily = FontFamily.Serif,
        ),
        cursorBrush = SolidColor(GoldTheme.gold),
        visualTransformation = visualTransformation,
        keyboardOptions = KeyboardOptions(
            capitalization = KeyboardCapitalization.None,
            autoCorrectEnabled = false,
            keyboardType = keyboardType,
            imeAction = imeAction,
        ),
        keyboardActions = KeyboardActions(
            onNext = { onIme?.invoke() },
            onGo = { onIme?.invoke() },
            onDone = { onIme?.invoke() },
        ),
        decorationBox = { inner ->
            Box {
                if (value.isEmpty()) {
                    Text(
                        text = placeholder,
                        color = placeholderColor,
                        fontSize = fontSize,
                        fontFamily = FontFamily.Serif,
                    )
                }
                inner()
            }
        },
    )
}

@Composable
private fun SiteLinkLine(
    prefix: String,
    suffix: String = "",
    prefixColor: androidx.compose.ui.graphics.Color,
    suffixColor: androidx.compose.ui.graphics.Color = prefixColor,
    fontSize: androidx.compose.ui.unit.TextUnit = 14.sp,
    fontWeight: FontWeight = FontWeight.Normal,
    onClick: () -> Unit,
) {
    Text(
        text = buildAnnotatedString {
            withStyle(SpanStyle(color = prefixColor, fontWeight = fontWeight)) { append(prefix) }
            withStyle(
                SpanStyle(
                    color = GoldTheme.gold,
                    fontWeight = fontWeight,
                    textDecoration = TextDecoration.Underline,
                ),
            ) { append(LockedCopy.SITE_HOST) }
            if (suffix.isNotEmpty()) {
                withStyle(SpanStyle(color = suffixColor, fontWeight = fontWeight)) { append(suffix) }
            }
        },
        fontSize = fontSize,
        fontFamily = FontFamily.Serif,
        modifier = Modifier
            .fillMaxWidth()
            .clickable(onClick = onClick),
    )
}

@Composable
private fun WaitlistLine(onOpenWaitlist: () -> Unit) {
    val text = buildAnnotatedString {
        append(LockedCopy.WAITLIST_PREFIX)
        pushLink(
            LinkAnnotation.Clickable(
                tag = LockedCopy.WAITLIST_LINK_WORD,
                styles = TextLinkStyles(
                    style = SpanStyle(
                        color = GoldTheme.gold,
                        textDecoration = TextDecoration.Underline,
                    ),
                ),
                linkInteractionListener = { onOpenWaitlist() },
            ),
        )
        append(LockedCopy.WAITLIST_LINK_WORD)
        pop()
        append(LockedCopy.WAITLIST_SUFFIX)
    }
    Text(
        text = text,
        fontSize = 16.sp,
        fontFamily = FontFamily.Serif,
        color = GoldTheme.muted,
        modifier = Modifier.semantics {
            contentDescription = LockedCopy.waitlistParagraph
        },
    )
}

private fun Context.copyToClipboard(value: String) {
    val clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
    clipboard.setPrimaryClip(ClipData.newPlainText("Digital Gold", value))
}

private fun Context.openWebsite(url: String) {
    try {
        startActivity(
            Intent(Intent.ACTION_VIEW, Uri.parse(url)).addCategory(Intent.CATEGORY_BROWSABLE),
        )
    } catch (_: ActivityNotFoundException) {
        // Placeholder / emulator without a browser — site open is best-effort.
    }
}

private fun Context.isReduceMotionEnabled(): Boolean {
    val animator = Settings.Global.getFloat(contentResolver, Settings.Global.ANIMATOR_DURATION_SCALE, 1f)
    return animator == 0f
}
