# handles markdown blocks like heading, lists, paragraphs
import re

from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


def markdown_to_blocks(markdown):
    splits = markdown.split("\n\n")
    stripped_splits = []
    for split in splits:
        stripped_split = split.strip()
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
        stripped_line = line.strip().strip("\n")
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


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = create_html_node(block_type, block)
        html_nodes.append(html_node)
    return ParentNode("div", html_nodes)


def create_html_node(block_type, block):
    if block_type == "quote":
        return quote_to_html_node(block)
    if block_type == "code":
        return code_to_html_node(block)
    if block_type == "heading":
        return heading_to_html_node(block)
    if block_type == "paragraph":
        return paragraph_to_html_node(block)
    if block_type == "ordered_list":
        return create_list(block, "ol")
    if block_type == "unordered_list":
        return create_list(block, "ul")


def quote_to_html_node(block):
    lines = block.replace(">", "").replace("\n", "").lstrip()
    children = text_to_children(lines)
    return ParentNode("blockquote", children)


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    html_nodes = []
    for textnode in textnodes:
        html_nodes.append(text_node_to_html_node(textnode))

    return html_nodes


def code_to_html_node(block):
    text = block.strip("```")
    children = text_to_children(text)
    return ParentNode("pre", [ParentNode("code", children)])


def heading_to_html_node(block):
    header_level = block.count("#")
    text = block.replace("#", "").strip()
    children = text_to_children(text)
    if header_level < 1 and header_level > 6:
        raise ValueError(f"Invalid heading: h{header_level}")
    return ParentNode(f"h{header_level}", children)


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def create_list(markdown, list_type):
    list_items = markdown.split("\n")
    stripped_list_items = []
    for item in list_items:
        if list_type == "ul":
            stripped_list_items.append(item[2:])
        if list_type == "ol":
            stripped_list_items.append(item[3:])

    html_list_items = []
    for item in stripped_list_items:
        html_list_items.append(ParentNode("li", text_to_children(item)))

    ordered_list = ParentNode(list_type, html_list_items)

    return ordered_list
