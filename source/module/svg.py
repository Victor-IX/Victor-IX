from lxml import etree

_JUSTIFY_LENGTHS = {
    "age_data": 46,
    "commit_data": 21,
    "star_data": 12,
    "repo_data": 6,
    "contrib_data": 0,
    "follower_data": 8,
    "blender_launcher_dl": 0,
    "default_cube": 0,
}


def update_svg(filename: str, stats: dict) -> None:
    tree = etree.parse(filename)
    root = tree.getroot()

    for element_id, length in _JUSTIFY_LENGTHS.items():
        if element_id in stats:
            _justify_format(root, element_id, stats[element_id], length)

    tree.write(filename, encoding="utf-8", xml_declaration=True)


def _justify_format(root, element_id: str, new_text, length: int = 0) -> None:
    if isinstance(new_text, int):
        new_text = f"{new_text:,}"
    new_text = str(new_text)

    _find_and_replace(root, element_id, new_text)

    just_len = max(0, length - len(new_text))
    if just_len <= 2:
        dot_string = {0: "", 1: " ", 2: ". "}[just_len]
    else:
        dot_string = " " + ("." * just_len) + " "
    _find_and_replace(root, f"{element_id}_dots", dot_string)


def _find_and_replace(root, element_id: str, new_text: str) -> None:
    element = root.find(f".//*[@id='{element_id}']")
    if element is not None:
        element.text = new_text
