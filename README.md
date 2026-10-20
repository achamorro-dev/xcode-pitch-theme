# Xcode Pitch Theme

<p align="center">
  <img src="images/icon.png" alt="Xcode Pitch Theme icon" height="128" width="128">
</p>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=albertochamorro.xcode-pitch-dark-theme"><img src="https://img.shields.io/visual-studio-marketplace/v/albertochamorro.xcode-pitch-dark-theme" alt="Marketplace version"></a>
  <a href="https://github.com/achamorro-dev/xcode-pitch-theme/issues"><img src="https://img.shields.io/github/issues/achamorro-dev/xcode-pitch-theme" alt="Issues"></a>
  <a href="https://github.com/achamorro-dev/xcode-pitch-theme/stargazers"><img src="https://img.shields.io/github/stars/achamorro-dev/xcode-pitch-theme" alt="Stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/achamorro-dev/xcode-pitch-theme" alt="MIT license"></a>
</p>

Xcode-inspired syntax highlighting for Visual Studio Code, with pitch-black Dark themes and a crisp, white Light theme.

## Themes

| Theme | Appearance |
| --- | --- |
| **Xcode Pitch Dark Theme** | Original Xcode syntax colors on a fully black background |
| **Xcode Pitch Dark Bordered Theme** | The original dark palette with visible panel borders |
| **Xcode Pitch Light** | White background, green comments, red strings, magenta keywords and cyan/violet accents |

Light keeps the original TextMate scopes and font styles, with colors adjusted for a white background rather than simply inverted. Its main text and every syntax rule have at least 4.5:1 contrast against white.

### Dark

![Xcode Pitch Dark Theme](images/screenshots/xcode-pitch-dark-theme.png)

### Dark Bordered

![Xcode Pitch Dark Bordered Theme](images/screenshots/xcode-pitch-dark-bordered-theme.png)

## Installation

Search for **Xcode Pitch Theme** in Extensions, or use the stable extension ID:

```sh
code --install-extension albertochamorro.xcode-pitch-dark-theme
```

Choose a variant with **Preferences: Color Theme**. Light is included in version **1.2.0**, currently prepared for release; until that version is published, install the locally built VSIX below.

### Follow the system appearance

```json
{
  "window.autoDetectColorScheme": true,
  "workbench.preferredDarkColorTheme": "Xcode Pitch Dark Theme",
  "workbench.preferredLightColorTheme": "Xcode Pitch Light"
}
```

## Compatibility

The repository and display name changed from **Xcode Pitch Dark Theme** to **Xcode Pitch Theme** to reflect the new Light variant. The published package name and publisher remain unchanged:

`albertochamorro.xcode-pitch-dark-theme`

Existing users will receive updates through the same extension. Both existing Dark selection names are unchanged, so their settings continue working. GitHub redirects the previous repository URL to the new one.

## Development

Requires **Node.js 22+**, npm and **Python 3.9+**.

```sh
npm ci
npm run build
code --install-extension xcode-pitch-dark-theme-1.2.0.vsix --force
```

The VSIX filename retains the historical package name intentionally. Building does not publish anything.

- Edit `palettes/light.json` to adjust the Light palette.
- Run `npm run generate` to regenerate `themes/Xcode Pitch Light-color-theme.json`.
- Run `npm test` for compatibility, reproducibility and contrast checks.
- Run `python3 scripts/build_light.py --check` to check that the generated theme is current.
- Press **F5** in VSCode to open an Extension Development Host and inspect all three themes.

The generator reads the original Dark theme without modifying either existing Dark theme. Commit the generated Light JSON so the extension works without build tools at runtime.

See [CHANGELOG.md](CHANGELOG.md) for the release history. Licensed under [MIT](LICENSE).
