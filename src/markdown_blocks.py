import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        stripped_blocks.append(block.strip())

    return stripped_blocks

def block_to_blocktype(block):
    if block[:3] == "```" and block[-3:] == "```":
        return "code"

    pattern = r"#{1,6}\s+"
    match = re.search(pattern, block)
    if match:
        return "heading"

    lines = block.split("\n")

    quotes = map(lambda line: line[0] == ">", lines)
    if all(quotes):
        return "quotes"

    unordered_list= map(lambda line: line[:2] == "* " or line[:2] == "- ", lines)
    if all(unordered_list):
        return "ul"

    index = 0
    ordered_list = []
    for line in lines:
        if line[0].isnumeric() and int(line[0]) > index and line[1:3] == ". ":
            ordered_list.append(True)
        else:
            ordered_list.append(False)

    if all(ordered_list):
        return "ol"
