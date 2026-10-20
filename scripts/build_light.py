#!/usr/bin/env python3
"""Generate Light from the original TextMate scopes and a contrast-adjusted palette."""

import argparse
import colorsys
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "templates" / "vscode" / "dark.jsonc"
TARGET = ROOT / "themes" / "Xcode Pitch Light-color-theme.json"
SOURCE_ROLES = {
    "#000000": "background", "#dfdfdf": "foreground", "#9a9c9d": "muted",
    "#646e83": "selection", "#6699ff": "accent", "#a0d07d": "comment",
    "#fc6a5d": "string", "#d0bf69": "number", "#ff7ab2": "keyword",
    "#ffa14f": "orange", "#5dd8ff": "function", "#49b7d7": "variable",
    "#e5cfff": "type", "#a167e6": "operator", "#d0a8ff": "purple",
    "#dfdfe0": "punctuation", "#ffffff": "foreground", "#dcdddd": "foreground",
    "#007aff": "accent", "#acf2e4": "property", "#72bfae": "property",
    "#83c9bc": "property", "#48b7db": "variable", "#d6c455": "number",
    "#cda1ff": "purple", "#9c9c9c": "muted", "#e21514": "red",
    "#f5c443": "yellow", "#fffb00": "findMatch",
}


def load_jsonc(text):
    # Keep quoted strings intact, including strings containing comment markers.
    pattern = r'"(?:[^"\\]|\\.)*"|//[^\n]*|/\*[\s\S]*?\*/'
    clean = re.sub(pattern, lambda m: m.group() if m.group().startswith('"') else " ", text)
    clean = re.sub(r'"(?:[^"\\]|\\.)*"|,\s*(?=[}\]])',
                   lambda m: m.group() if m.group().startswith('"') else "", clean)
    return json.loads(clean)


def generate(palette=None):
    source = load_jsonc(SOURCE.read_text())
    palette = palette or json.loads((ROOT / "palettes" / "light.json").read_text())
    mapping = {color: palette[role] for color, role in SOURCE_ROLES.items()}

    def convert(value):
        if isinstance(value, dict):
            return {key: convert(item) for key, item in value.items()}
        if isinstance(value, list):
            return [convert(item) for item in value]
        if not isinstance(value, str) or not re.fullmatch(r"#(?:[\da-fA-F]{3}|[\da-fA-F]{4}|[\da-fA-F]{6}|[\da-fA-F]{8})", value):
            return value
        color = value.lower()
        if len(color) in (4, 5):
            color = "#" + "".join(c * 2 for c in color[1:])
        rgb, alpha = color[:7], color[7:]
        if rgb not in mapping:
            hue, _, saturation = colorsys.rgb_to_hls(*(int(rgb[i:i+2], 16) / 255 for i in (1, 3, 5)))
            adjusted = colorsys.hls_to_rgb(hue, .30, saturation * .85)
            mapping[rgb] = "#" + "".join(f"{round(c * 255):02x}" for c in adjusted)
        return mapping[rgb] + alpha

    theme = convert(source)
    theme.update(name=palette["name"], type="light")
    theme["colors"].update({
        "editor.selectionBackground": palette["selection"],
        "editor.lineHighlightBackground": palette["surface"],
        "editorCursor.foreground": palette["cursor"],
        "editorLineNumber.foreground": palette["muted"],
        "list.activeSelectionBackground": palette["selection"],
        "list.focusBackground": palette["selection"],
    })
    return theme


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the checked-in Light theme is stale")
    args = parser.parse_args()
    content = json.dumps(generate(), indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not TARGET.exists() or TARGET.read_text() != content:
            parser.exit(1, "Light theme is stale. Run npm run generate.\n")
        return
    TARGET.write_text(content)
    print(TARGET.relative_to(ROOT))


if __name__ == "__main__":
    main()
