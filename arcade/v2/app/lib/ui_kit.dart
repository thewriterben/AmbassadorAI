import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'theme.dart';

/// The pieces the 2026-09-30 design return builds every arcade screen from:
/// tinted Hugeicons, the rounded-square icon button, the row card and the
/// information notice. One place, so a screen that follows the design reads
/// like the others without restating its numbers.

/// A Hugeicons line icon (assets/images/icons/, MIT). The files are single
/// colour exports; this tints them, so any colour the design asks for works.
class HugeIcon extends StatelessWidget {
  final String name;
  final double size;
  final Color color;
  final String? semanticLabel;
  const HugeIcon(this.name, {super.key, this.size = 20, this.color = AppTheme.body, this.semanticLabel});

  @override
  Widget build(BuildContext context) {
    return Image.asset(
      'assets/images/icons/$name.png',
      width: size,
      height: size,
      color: color,
      colorBlendMode: BlendMode.srcIn,
      filterQuality: FilterQuality.medium,
      semanticLabel: semanticLabel,
      excludeFromSemantics: semanticLabel == null,
    );
  }
}

/// The 44 dp rounded-square button in every screen header: back, sound,
/// music, settings. Surface fill, hairline edge.
class SquareIconButton extends StatelessWidget {
  final String icon;
  final String label;
  final VoidCallback? onTap;
  final Color iconColor;
  final bool selected;
  const SquareIconButton({
    super.key,
    required this.icon,
    required this.label,
    required this.onTap,
    this.iconColor = AppTheme.body,
    this.selected = false,
  });

  @override
  Widget build(BuildContext context) {
    return Semantics(
      button: true,
      label: label,
      toggled: selected,
      excludeSemantics: true,
      child: Material(
        color: AppTheme.surface,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
          side: const BorderSide(color: AppTheme.border),
        ),
        child: InkWell(
          borderRadius: BorderRadius.circular(16),
          onTap: onTap,
          child: SizedBox(width: 44, height: 44, child: Center(child: HugeIcon(icon, size: 20, color: iconColor))),
        ),
      ),
    );
  }
}

/// A screen's title block: an optional back button, the title, and a
/// secondary line under it; trailing buttons sit to the right of the title.
class ScreenHeader extends StatelessWidget {
  final String title;
  final String? subtitle;
  final VoidCallback? onBack;
  final List<Widget> actions;

  /// Set the subtitle under the title rather than at the screen's edge, as
  /// the level map does; the other screens start it at the edge.
  final bool subtitleUnderTitle;
  const ScreenHeader({
    super.key,
    required this.title,
    this.subtitle,
    this.onBack,
    this.actions = const [],
    this.subtitleUnderTitle = false,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            if (onBack != null) ...[
              SquareIconButton(icon: 'arrow_left1', label: 'Back', onTap: onBack),
              const SizedBox(width: 16),
            ],
            Expanded(
              child: Text(
                title,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(fontSize: 26, fontWeight: FontWeight.w600, letterSpacing: -0.6, color: AppTheme.text),
              ),
            ),
            for (var i = 0; i < actions.length; i++) ...[
              if (i > 0) const SizedBox(width: 12),
              actions[i],
            ],
          ],
        ),
        if (subtitle != null) ...[
          const SizedBox(height: 10),
          Padding(
            padding: EdgeInsets.only(left: subtitleUnderTitle && onBack != null ? 60 : 0),
            child: Text(subtitle!, style: const TextStyle(fontSize: 14, color: AppTheme.body)),
          ),
        ],
      ],
    );
  }
}

/// A tappable row: an optional leading widget in an inset well, a title and
/// an optional line under it, and a chevron. Surface fill, hairline edge.
class RowCard extends StatelessWidget {
  final Widget? leading;
  final String title;
  final String? subtitle;
  final Widget? trailing;
  final VoidCallback? onTap;
  final Color fill;
  const RowCard({
    super.key,
    this.leading,
    required this.title,
    this.subtitle,
    this.trailing,
    this.onTap,
    this.fill = AppTheme.surface,
  });

  @override
  Widget build(BuildContext context) {
    return Material(
      color: fill,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20), side: const BorderSide(color: AppTheme.border)),
      child: InkWell(
        borderRadius: BorderRadius.circular(20),
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.fromLTRB(16, 14, 16, 14),
          child: Row(
            children: [
              if (leading != null) ...[
                Container(
                  width: 40,
                  height: 40,
                  decoration: BoxDecoration(color: AppTheme.card, borderRadius: BorderRadius.circular(12)),
                  alignment: Alignment.center,
                  child: leading,
                ),
                const SizedBox(width: 14),
              ],
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(title, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w500, color: AppTheme.text)),
                    if (subtitle != null) ...[
                      const SizedBox(height: 3),
                      Text(subtitle!, style: const TextStyle(fontSize: 13, height: 1.35, color: AppTheme.body)),
                    ],
                  ],
                ),
              ),
              const SizedBox(width: 10),
              trailing ?? const HugeIcon('arrow_right1', size: 18, color: AppTheme.body),
            ],
          ),
        ),
      ),
    );
  }
}

/// The information line: a circled "i" and a sentence of secondary text.
class InfoNotice extends StatelessWidget {
  final String text;
  const InfoNotice(this.text, {super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Padding(
          padding: EdgeInsets.only(top: 1),
          child: HugeIcon('information_circle', size: 17, color: AppTheme.body),
        ),
        const SizedBox(width: 13),
        Expanded(child: Text(text, style: const TextStyle(fontSize: 13, height: 1.4, color: AppTheme.body))),
      ],
    );
  }
}

/// The fonts' and icons' licences, so they show in the licence page and
/// travel with the binary (SIL OFL 1.1 asks for it; so does MIT).
void registerDesignLicences() {
  LicenseRegistry.addLicense(() async* {
    for (final (pkg, path) in [
      ('Inter', 'assets/fonts/Inter-OFL.txt'),
      ('Geist Mono', 'assets/fonts/GeistMono-OFL.txt'),
      ('Hugeicons', 'assets/images/icons/LICENSE-hugeicons.md'),
    ]) {
      yield LicenseEntryWithLineBreaks([pkg], await rootBundle.loadString(path));
    }
  });
}
