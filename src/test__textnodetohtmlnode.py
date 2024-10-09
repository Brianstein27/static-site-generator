import unittest
from text_node_to_html_node import text_node_to_html_node
from htmlnode import LeafNode
from textnode import TextNode

test_cases = [
    TextNode("This is a text node", "text"),
    TextNode("This is a bold node", "bold"),
    TextNode("This is a italic node", "italic"),
    TextNode("This is a code node", "code"),
    TextNode("This is a link node", "link", "https://boot.dev"),
    TextNode("This is a image node", "image", "https://boot.dev")
]
expected_results = [
    "LeafNode(None, This is a text node, children: None, None)",
    "LeafNode(b, This is a bold node, children: None, None)",
    "LeafNode(i, This is a italic node, children: None, None)",
    "LeafNode(code, This is a code node, children: None, None)",
    "LeafNode(a, This is a link node, children: None, {'href': 'https://boot.dev'})",
    "LeafNode(img, , children: None, {'src': 'https://boot.dev', 'alt': 'This is a image node'})",
]

class TextNode_To_HTMLNode(unittest.TestCase):
    def test_func(self):
        for index in range(len(test_cases)):
            self.assertEqual(text_node_to_html_node(test_cases[index]).__repr__(), expected_results[index])

if __name__ == "__main__":
    unittest.main()
