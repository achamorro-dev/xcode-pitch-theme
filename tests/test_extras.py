import copy
import json
from pathlib import Path
import sys
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_themes as themes


class ExtrasTests(unittest.TestCase):
    def test_every_generated_file_is_current(self):
        themes.build(check=True)

    def test_dark_editors_are_unchanged_at_default_palette(self):
        for template, name in (("dark", "Xcode Pitch Dark Theme"), ("bordered", "Xcode Pitch Dark Bordered Theme")):
            self.assertEqual((ROOT / "templates/vscode" / f"{template}.jsonc").read_text().rstrip("\n"),
                             (ROOT / "themes" / f"{name}-color-theme.json").read_text())

    def test_no_personal_settings_or_external_theme_in_distribution(self):
        for path in (ROOT / "extras").rglob("*"):
            if not path.is_file():
                continue
            text = path.read_text().lower()
            self.assertNotIn("/users/", text, path)
            self.assertNotIn("dotfiles-theme", text, path)
            self.assertNotIn("ayu", text, path)
        for path in (ROOT / "extras/herdr").glob("*.toml"):
            import tomllib
            self.assertEqual(set(tomllib.loads(path.read_text())), {"theme"})

    def test_open_code_v2_token_references_resolve(self):
        theme = json.loads((ROOT / "extras/opencode/xcode-pitch.json").read_text())
        self.assertEqual(set(theme), {"base", "dark", "light"})
        for mode in ("dark", "light"):
            resolved = {**theme["base"], **theme[mode]}

            def resolve(value, stack=()):
                if isinstance(value, dict):
                    return {k: resolve(v, stack) for k, v in value.items()}
                if isinstance(value, list):
                    return [resolve(v, stack) for v in value]
                if not value.startswith("$"):
                    return value
                self.assertNotIn(value, stack)
                target = resolved
                for part in value[1:].split("."):
                    target = target[part]
                return resolve(target, (*stack, value))

            resolve(resolved)
            self.assertEqual(resolved["syntax"]["keyword"], themes.palettes()[mode]["keyword"])

    def test_herdr_sidebar_titles_follow_the_mode_foreground(self):
        palettes = themes.palettes()
        for mode in ("auto", "dark", "light"):
            config = tomllib.loads(themes.herdr_theme(palettes["dark"], palettes["light"], mode))
            custom = config["theme"]["custom"]
            for current in (("dark", "light") if mode == "auto" else (mode,)):
                colors = custom[current] if mode == "auto" else custom
                for role in ("text", "overlay0", "subtext0"):
                    self.assertEqual(colors[role], palettes[current]["foreground"])
                self.assertEqual(colors["overlay1"], palettes[current]["muted"])
                self.assertNotEqual(colors["overlay0"], palettes[current]["border"])

    def test_one_palette_change_reaches_all_ports(self):
        for mode, editor in (("dark", "Xcode Pitch Dark Theme"), ("light", "Xcode Pitch Light")):
            changed = copy.deepcopy(themes.palettes())
            changed[mode]["keyword"] = "#abcdef"
            changed[mode]["red"] = "#abcdef"
            with patch.object(themes, "palettes", return_value=changed):
                files = themes.render()
            for relative in (f"themes/{editor}-color-theme.json", f"extras/ghostty/xcode-{mode}",
                             "extras/opencode/xcode-pitch.json", "extras/herdr/auto.toml",
                             "extras/neovim/lua/xcode_pitch/palettes.lua"):
                self.assertIn("#abcdef", files[relative], relative)


if __name__ == "__main__":
    unittest.main()
