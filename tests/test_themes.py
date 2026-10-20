import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_light


def luminance(color):
    channels = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in channels]
    return sum(v * weight for v, weight in zip(linear, (.2126, .7152, .0722)))


class ThemeTests(unittest.TestCase):
    def test_published_identity_and_existing_theme_names_are_preserved(self):
        package = json.loads((ROOT / "package.json").read_text())
        self.assertEqual(package["publisher"], "albertochamorro")
        self.assertEqual(package["name"], "xcode-pitch-dark-theme")
        self.assertEqual(package["displayName"], "Xcode Pitch Theme")
        self.assertEqual([t["label"] for t in package["contributes"]["themes"]], [
            "Xcode Pitch Dark Theme", "Xcode Pitch Dark Bordered Theme", "Xcode Pitch Light"])
        for entry in package["contributes"]["themes"]:
            path = ROOT / entry["path"]
            theme = build_light.load_jsonc(path.read_text())
            self.assertTrue(theme["colors"])
            self.assertTrue(theme["tokenColors"])
            self.assertEqual(theme["type"], "light" if entry["uiTheme"] == "vs" else "dark")

    def test_light_is_reproducible_and_keeps_scopes_and_styles(self):
        generated = build_light.generate()
        self.assertEqual(build_light.TARGET.read_text(), json.dumps(generated, indent=2, ensure_ascii=False) + "\n")
        dark = build_light.load_jsonc(build_light.SOURCE.read_text())
        self.assertEqual([r["scope"] for r in dark["tokenColors"]], [r["scope"] for r in generated["tokenColors"]])
        self.assertEqual([r["settings"].get("fontStyle") for r in dark["tokenColors"]],
                         [r["settings"].get("fontStyle") for r in generated["tokenColors"]])

    def test_light_text_and_every_syntax_rule_have_readable_contrast(self):
        theme = build_light.generate()
        self.assertEqual(theme["colors"]["editor.background"], "#ffffff")
        colors = [theme["colors"]["editor.foreground"], theme["colors"]["editorLineNumber.foreground"]]
        colors += [rule["settings"]["foreground"] for rule in theme["tokenColors"]]
        for color in colors:
            self.assertRegex(color, r"^#[\da-fA-F]{6}$")
            self.assertGreaterEqual(1.05 / (luminance(color) + .05), 4.5, color)

    def test_jsonc_strings_are_not_treated_as_comments(self):
        self.assertEqual(build_light.load_jsonc('{"url":"https://example.com/*keep*/", // comment\n}'),
                         {"url": "https://example.com/*keep*/"})


if __name__ == "__main__":
    unittest.main()
