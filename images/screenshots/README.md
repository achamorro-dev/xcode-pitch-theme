# Screenshot provenance

The following images were captured from real macOS application windows on **2026-10-20**:

| Image | Application / theme | Resolution |
| --- | --- | --- |
| `xcode-pitch-light-eventoswiki.png` | VSCode 1.140.0 / Xcode Pitch Light | 2880 × 1800 |
| `neovim-ghostty-dark-eventoswiki.png` | Neovim 0.12.5 inside Ghostty 1.3.1 / Xcode Pitch Dark | 2352 × 2212 |
| `neovim-ghostty-light-eventoswiki.png` | Neovim 0.12.5 inside Ghostty 1.3.1 / Xcode Pitch Light | 2352 × 2212 |

## Source project

- **Project:** [EventosWiki](https://github.com/achamorro-dev/eventoswiki), Alberto Chamorro's public event-directory project.
- **Commit:** [`57c98be4e4d315169517a7ad1b89f98a564f87fc`](https://github.com/achamorro-dev/eventoswiki/tree/57c98be4e4d315169517a7ad1b89f98a564f87fc).
- **File:** [`src/modules/shared/domain/datetime/datetime.ts`](https://github.com/achamorro-dev/eventoswiki/blob/57c98be4e4d315169517a7ad1b89f98a564f87fc/src/modules/shared/domain/datetime/datetime.ts#L83-L118), around lines 83–118 (the visible range varies with the viewport).
- **Source-code license:** MIT, copyright (c) 2024 Alberto Chamorro. The original notice is included in [`eventoswiki-LICENSE.txt`](eventoswiki-LICENSE.txt).

## Capture setup

- Theme source: Xcode Pitch Theme revision [`d5a156a`](https://github.com/achamorro-dev/xcode-pitch-theme/tree/d5a156a292242effe136074fa293c2f39b720126).
- VSCode ran with a separate user-data directory and extension directory. The theme was loaded from this repository, with TypeScript's built-in TextMate grammar; semantic highlighting and rainbow-bracket colorization were disabled to show the theme's own token colors.
- Neovim used an isolated init file, the standalone `extras/neovim` runtime and the TypeScript Treesitter grammar. Each Ghostty instance loaded only the matching `extras/ghostty` palette and temporary presentation settings.
- Typeface: JetBrainsMono Nerd Font, `editor.fontSize = 18` (CSS px) in VSCode and `font-size = 17` (pt) in Ghostty. Viewport chrome and spacing differ between applications; palette colors were not overridden.
- The source file was exported from the specified Git commit into a read-only editor session or an isolated source snapshot. The working project, its environment files and the author's normal editor configuration were not changed.
- Images were captured as native, per-window PNGs with no desktop background or window shadow. No synthetic editor mockups, recoloring, compositing or generated replacement code were used.

The two older VSCode Dark / Dark Bordered screenshots predate this capture session and are preserved unchanged.
