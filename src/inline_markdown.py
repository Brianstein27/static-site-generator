from textnode import TextNode
import re

def extract_markdown_links(text):
    pattern = r'\[([^\]]+)\]\((http[s]?://[^\)]+)\)'
    return re.findall(pattern, text)

def extract_markdown_images(text):
    pattern = r"\!\[([^\]]+)\]\((http[s]?://[^\)]+)\)"
    return re.findall(pattern, text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], "text"))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # print(old_node.text)
        links = extract_markdown_links(old_node.text)
        splitters = []
        if len(links) > 1:
            for link in links:
                splitters.append([link[0], link[1]])

            for index in range(len(splitters)):
                split_node = old_node.text.split(f"[{ splitters[index][0] }]({splitters[index][1]})")
                new_nodes.append(TextNode(split_node[0], "text"))
                new_nodes.append(TextNode(splitters[index][0], "link", splitters[index][1]))
                if index == len(splitters) - 1:
                    new_nodes.append(TextNode(split_node[1], "text"))
                else:
                    old_node.text = split_node[1]
        elif len(links) > 0:
            split_node = old_node.text.split(f"[{links[0][0]}]({links[0][1]})")
            if split_node[0] != '':
                new_nodes.append(TextNode(split_node[0], "text"))
            new_nodes.append(TextNode(links[0][0], "link", links[0][1]))
            if split_node[1] != '':
                new_nodes.append(TextNode(split_node[1], "text"))
        else:
            new_nodes.append(old_node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_images(old_node.text)
        splitters = []
        if len(links) > 1:
            for link in links:
                splitters.append([link[0], link[1]])

            for index in range(len(splitters)):
                split_node = old_node.text.split(f"![{ splitters[index][0] }]({splitters[index][1]})")
                if split_node[0] != '':
                    new_nodes.append(TextNode(split_node[0], "text"))
                new_nodes.append(TextNode(splitters[index][0], "image", splitters[index][1]))
                if index == len(splitters) - 1 and split_node[1] != '':
                    new_nodes.append(TextNode(split_node[1], "text"))
                else:
                    old_node.text = split_node[1]
        elif len(links) > 0:
            split_node = old_node.text.split(f"![{links[0][0]}]({links[0][1]})")
            if split_node[0] != '':
                new_nodes.append(TextNode(split_node[0], "text"))
            new_nodes.append(TextNode(links[0][0], "image", links[0][1]))
            if split_node[1] != '':
                new_nodes.append(TextNode(split_node[1], "text"))
        else:
            new_nodes.append(old_node)
    return new_nodes
