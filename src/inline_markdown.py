import re

from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        splits = node.text.split(delimiter)
        for index, split in enumerate(splits):
            if split == "":
                pass
            elif index % 2 == 1 or index == 1:
                new_nodes.append(TextNode(split, text_type, node.url))
            elif index % 2 == 0 or index == 0:
                new_nodes.append(TextNode(split, node.text_type, node.url))

    return new_nodes


def extract_markdown_links(text):
    pattern = r"\[([^\]]+)\]\((http[s]?://[^\)]+)\)"
    return re.findall(pattern, text)


def extract_markdown_images(text):
    pattern = r"\[([^\]]+)\]\((http[s]?://[^\)]+)\)"

    return re.findall(pattern, text)
