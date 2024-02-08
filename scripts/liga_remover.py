import fontforge

LIGATURES_TO_REMOVE = ["fi", "fl"]


def remove_ligatures(font_path, output_path):
    font = fontforge.open(font_path)

    for ligature in LIGATURES_TO_REMOVE:
        if ligature in font:
            print(f"Removing ligature: {ligature}")
            font.removeGlyph(ligature)

    font.generate(output_path)


if __name__ == "__main__":
    remove_ligatures("/path/to/font", "/path/to/output/font")
