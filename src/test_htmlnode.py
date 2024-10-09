import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html1(self):
        props = {
                "href": "https://www.google.com", 
                "target": "_blank",
            }

        node = HTMLNode("p","Hello World", None, props)

        self.assertEqual(node.props_to_html(),  'href="https://www.google.com" target="_blank"')

    def test_props_to_html2(self):
        props = {
                "href": "https://www.google.com", 
                "target": "_blank",
            }

        node = HTMLNode("p","Hello World", None, props)

        self.assertNotEqual(node.props_to_html(),  'href="https://www.boot.dev" target="_blank"')

    def test_props_to_html3(self):
        props = {
                "href": "https://www.boot.dev", 
                "target": "#Header",
            }

        node = HTMLNode("p","Hello World", None, props)

        self.assertEqual(node.props_to_html(),  'href="https://www.boot.dev" target="#Header"')

    def test_props_to_html4(self):
        props = None

        node = HTMLNode("p","Hello World", None, props)

        self.assertEqual(node.props_to_html(),  '')

    def test_props_to_html4(self):
        props = None

        node = HTMLNode("p","Hello World", None, props)

        self.assertNotEqual(node.props_to_html(), 'href="https://www.boot.dev" target="#Header"')

    def test_repr(self):
        props = {
                "href": "https://www.boot.dev", 
                "target": "#Header",
            }

        node = HTMLNode("p","Hello World", None, props)
        self.assertEqual(node.__repr__(), f"HTMLNode(p, Hello World, children: None, {props})")

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("p", "I am a LeafNode", {"href": "https://boot.dev", "class": "bold"})
        representation = "LeafNode(p, I am a LeafNode, children: None, {'href': 'https://boot.dev', 'class': 'bold'})"
        self.assertEqual(node.__repr__(), representation)

    def test_to_html1(self):
        node = LeafNode("p", "I am a LeafNode", {"href": "https://boot.dev", "class": "bold"})
        html = '<p href="https://boot.dev" class="bold">I am a LeafNode</p>'
        self.assertEqual(node.to_html(), html)

    def test_to_html2(self):
        node = LeafNode("p", "I am a LeafNode", {"href": "https://boot.dev", "class": "bold"})
        html = '<p href="https://boot.dev" class="bold">I am a LeafNode</p>'
        self.assertEqual(node.to_html(), html)


    def test_to_html3(self):
        node = LeafNode("p", "I am a LeafNode")
        html = '<p>I am a LeafNode</p>'
        self.assertEqual(node.to_html(), html)


class TestParentNode(unittest.TestCase):
    def test_repr(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode("b", "Normal text")])
        self.assertEqual(node.__repr__(), "ParentNode(p, None, children: [LeafNode(b, Bold text, children: None, None), LeafNode(b, Normal text, children: None, None)], None)")

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()
