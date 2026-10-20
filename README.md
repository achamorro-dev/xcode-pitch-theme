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

Xcode-inspired colors for **VSCode, Cursor, Ghostty, OpenCode, Herdr and Neovim**. One shared Dark/Light palette, with generated adaptations for each tool.

## Supported tools

| Tool | Dark / Light | Files |
| --- | --- | --- |
| VSCode / Cursor | Dark, Dark Bordered, Light | [`themes/`](themes/) — one extension, three variants |
| Ghostty | Dark, Light | [`extras/ghostty/`](extras/ghostty/) — foreground, background and 16 ANSI colors |
| OpenCode **V2** | Both modes in one theme | [`extras/opencode/xcode-pitch.json`](extras/opencode/xcode-pitch.json) |
| Herdr **0.9.5+** | Auto, forced Dark, forced Light | [`extras/herdr/`](extras/herdr/) — theme-only TOML fragments |
| Neovim **0.10+** | Dark, Light | [`extras/neovim/`](extras/neovim/) — classic, Treesitter and LSP highlights |

The color roles are shared, but each tool has its own syntax engine and UI. Adaptations are not expected to be pixel-identical. Dark Bordered remains an editor-only variant. Classic Vim is not supported by the Neovim Lua port.

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

All generated themes are committed, so using the terminal themes does **not** require npm or a build step. Clone or download this repository:

```sh
git clone https://github.com/achamorro-dev/xcode-pitch-theme.git
cd xcode-pitch-theme
```

The examples below assume you are in that checkout. Back up your existing configurations before editing them. Theme files do not contain personal keybindings, shell commands, absolute paths or synchronization services.

### VSCode / Cursor

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

Cursor uses the same extension and settings. You can install a locally built VSIX with **Extensions: Install from VSIX** in either editor.

### Ghostty

```sh
mkdir -p "${XDG_CONFIG_HOME:-$HOME/.config}/ghostty/themes"
cp extras/ghostty/xcode-dark extras/ghostty/xcode-light "${XDG_CONFIG_HOME:-$HOME/.config}/ghostty/themes/"
```

Set this in your Ghostty config to follow the desktop appearance:

```ini
theme = dark:xcode-dark,light:xcode-light
```

Or use `theme = xcode-dark` / `theme = xcode-light` to force a variant. Reload Ghostty's configuration after changing it.

### OpenCode V2

```sh
mkdir -p "${XDG_CONFIG_HOME:-$HOME/.config}/opencode/themes"
cp extras/opencode/xcode-pitch.json "${XDG_CONFIG_HOME:-$HOME/.config}/opencode/themes/"
```

Merge this into `~/.config/opencode/cli.json` (under `$XDG_CONFIG_HOME` if set), **not** `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/v2/cli.json",
  "theme": {
    "name": "xcode-pitch",
    "mode": "system"
  }
}
```

Restart OpenCode once to discover a newly added theme. `system` follows the terminal appearance; use `dark` or `light` to lock the mode. The theme uses the V2 `base` / `dark` / `light` format, not the legacy V1 format.

### Herdr

Merge the `[theme]` table and its children from one fragment into `~/.config/herdr/config.toml`:

- [`extras/herdr/auto.toml`](extras/herdr/auto.toml): follow the terminal appearance, with separate Dark/Light overrides.
- [`extras/herdr/dark.toml`](extras/herdr/dark.toml): force Dark.
- [`extras/herdr/light.toml`](extras/herdr/light.toml): force Light.

**Do not replace your whole config or append a second `[theme]` table.** Herdr does not provide a TOML include directive. Preserve your other tables, including keybindings and workspaces. Then run `herdr server reload-config`; if the client does not refresh, choose **reload config** from its global menu.

### Neovim

Add `extras/neovim` to your runtime path, then select the theme:

```lua
vim.opt.rtp:append(vim.fn.expand("~/path/to/xcode-pitch-theme/extras/neovim"))
vim.o.background = "dark" -- or "light"
vim.cmd.colorscheme("xcode_pitch")
```

With **lazy.nvim**:

```lua
{
  "achamorro-dev/xcode-pitch-theme",
  lazy = false,
  priority = 1000,
  config = function(plugin)
    vim.opt.rtp:append(plugin.dir .. "/extras/neovim")
    vim.cmd.colorscheme("xcode_pitch") -- uses vim.o.background
  end,
}
```

The port works without the author's dotfiles. It provides both modes, terminal colors, diagnostics, diff colors and classic/Treesitter/LSP highlights. It intentionally does not change macOS appearance, watch a personal state file or install a background service.

## Shared palettes and synchronization

`palettes/dark.json` and `palettes/light.json` are the color sources. Editor scope templates live in `templates/vscode/`; tool-specific generators translate the same roles into each format. Generated outputs should not be edited manually.

This repository distributes **themes**, not personal settings. Switching all applications together belongs in your own configuration or theme switcher. For example, the author's [dotfiles](https://github.com/achamorro-dev/dotfiles-alberto-chamorro) consume a pinned revision of these exports and manage `theme auto|dark|light` separately. Other palettes, such as Ayu, are not bundled into Xcode Pitch Theme.

## Compatibility

The repository and display name changed from **Xcode Pitch Dark Theme** to **Xcode Pitch Theme** to reflect the new Light variant. The published package name and publisher remain unchanged:

`albertochamorro.xcode-pitch-dark-theme`

Existing users will receive updates through the same extension. Both existing Dark selection names are unchanged, so their settings continue working. GitHub redirects the previous repository URL to the new one.

## Development

Building the editor VSIX requires **Node.js 22+**, npm and **Python 3.11+** (for the test suite). Generating themes alone uses Python 3.9+ and the standard library.

```sh
npm ci
npm run build
code --install-extension xcode-pitch-dark-theme-1.2.0.vsix --force
```

The VSIX filename retains the historical package name intentionally. Building does not publish anything.

- Edit `palettes/dark.json` or `palettes/light.json` to adjust a palette.
- Run `npm run generate` (or `python3 scripts/build_themes.py`) to regenerate **all** tool exports and editor themes.
- Run `npm run check` to detect stale generated files without rewriting them.
- Run `npm test` for compatibility, reproducibility, contrast, cross-tool propagation and OpenCode token-reference checks.
- To smoke-test the standalone Neovim port: `nvim --headless -u NONE --cmd 'set rtp+=./extras/neovim' -l tests/test_neovim.lua`.
- Press **F5** in VSCode to open an Extension Development Host and inspect all three themes.

At the default palette both original Dark editor files remain byte-for-byte unchanged. Commit all generated files under `themes/` and `extras/` so consumers do not need build tools. The editor VSIX includes only editor assets, not the other tools' configurations.

```text
palettes/            Shared Dark/Light color roles
templates/vscode/   Original editor scope/UI templates
themes/             Generated editor themes
extras/ghostty/     Generated terminal palettes
extras/opencode/    Generated dual-mode V2 theme
extras/herdr/       Generated theme-only fragments
extras/neovim/      Standalone Lua renderer and generated palettes
scripts/            Generators, no third-party Python dependencies
tests/              Compatibility, generation and standalone-port checks
```

See [CHANGELOG.md](CHANGELOG.md) for the release history. Licensed under [MIT](LICENSE).
