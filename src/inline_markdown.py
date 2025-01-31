import re

from textnode import TextNode, TextType


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


def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        text = node.text
        for link in links:
            link_text = link[0]
            link_url = link[1]
            sections = text.split(f"[{link_text}]({link_url})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], node.text_type))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            if len(extract_markdown_links(sections[1])) == 0 and sections[1] != "":
                new_nodes.append(TextNode(sections[1], node.text_type))
            text = sections[1]

    return new_nodes


def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        text = node.text
        for image in images:
            image_alt = image[0]
            image_link = image[1]
            sections = text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], node.text_type))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            if len(extract_markdown_images(sections[1])) == 0 and sections[1] != "":
                new_nodes.append(TextNode(sections[1], node.text_type))
            text = sections[1]

    return new_nodes
