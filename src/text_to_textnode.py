from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode

def text_to_textnodes(text):
    textnodes = [TextNode(text, "text")]
    characters = list(text)
    for index in range(len(characters)):
        match characters[index]:
            case "*":
                if characters[index + 1] == "*":
                    new_textnodes = []
                    for textnode in textnodes:
                        new_textnodes.extend(split_nodes_delimiter([textnode], "**", "bold"))
                    textnodes = new_textnodes
                else:
                    new_textnodes = []
                    for textnode in textnodes:
                        new_textnodes.extend(split_nodes_delimiter([textnode], "*", "italic"))
                    textnodes = new_textnodes
            case "`":
                new_textnodes = []
                for textnode in textnodes:
                    new_textnodes.extend(split_nodes_delimiter([textnode], "`", "code"))
                textnodes = new_textnodes
            case "!":
                if characters[index + 1] == "[":
                    new_textnodes = []
                    for textnode in textnodes:
                        new_textnodes.extend(split_nodes_image([textnode]))
                    textnodes = new_textnodes
            case "[":
                new_textnodes = []
                for textnode in textnodes:
                    new_textnodes.extend(split_nodes_link([textnode]))
                textnodes = new_textnodes

    return textnodes
