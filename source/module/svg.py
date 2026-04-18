from lxml import etree


def update_svg(filename: str, stats: dict) -> None:
    tree = etree.parse(filename)
    root = tree.getroot()

    for element_id, value in stats.items():
        _justify_format(root, element_id, value)

    tree.write(filename, encoding="utf-8", xml_declaration=True)


def _justify_format(root, element_id: str, new_value) -> None:
    if isinstance(new_value, int):
        new_text = f"{new_value:,}"
    else:
        new_text = str(new_value)

    value_element = root.find(f".//*[@id='{element_id}']")
    if value_element is None:
        return

    dots_element = root.find(f".//*[@id='{element_id}_dots']")
    if dots_element is not None:
        # Keep the sum of (dots span + value) constant so the column stays aligned.
        target_total = len(dots_element.text or "") + len(value_element.text or "")
        dots_element.text = _build_dots(target_total - len(new_text))

    value_element.text = new_text


def _build_dots(total_len: int) -> str:
    if total_len <= 0:
        return ""
    if total_len == 1:
        return " "
    if total_len == 2:
        return ". "
    return " " + ("." * (total_len - 2)) + " "
