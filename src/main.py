from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType, split_nodes_delimiter


def main():
    node = TextNode("this `is` some `code`", TextType.NORMAL)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)


main()
