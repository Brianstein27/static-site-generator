# represents all types of inline text
from enum import Enum

from htmlnode import LeafNode


# defining text types
class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # sets default behavior of equality comparison between to TextNode instances
    def __eq__(self, other) -> bool:
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True

        return False

    # sets print format of TextNode instances
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type is TextType.NORMAL:
        return LeafNode(None, text_node.text)
    if text_node.text_type is TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type is TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type is TextType.LINK:
        return LeafNode("code", text_node.text, {"href": text_node.url})
    if text_node.text_type is TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})


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
