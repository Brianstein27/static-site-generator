# handles markdown blocks like heading, lists, paragraphs
import re


def markdown_to_blocks(markdown):
    splits = markdown.split("\n\n")
    stripped_splits = []
    for split in splits:
        stripped_split = split.strip("\n").strip()
        if stripped_split != "":
            stripped_splits.append(stripped_split)

    return stripped_splits


def block_to_block_type(block):
    if block[:3] == "```" and block[-3:] == "```":
        return "code"

    pattern = r"#{1,6}\s+"
    match = re.search(pattern, block)
    if match:
        return "heading"

    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line != "":
            stripped_lines.append(stripped_line)

    quotes = map(lambda line: line[0] == ">", stripped_lines)
    if all(quotes):
        return "quote"

    unordered_list = map(
        lambda line: line.strip()[:2] == "* " or line.strip()[:2] == "- ", lines
    )
    if all(unordered_list):
        return "unordered_list"

    index = 0
    ordered_list = []
    for line in lines:
        line = line.strip()
        if line[0].isnumeric() and int(line[0]) > index and line[1:3] == ". ":
            ordered_list.append(True)
        else:
            ordered_list.append(False)

    if all(ordered_list):
        return "ordered_list"

    return "paragraph"
