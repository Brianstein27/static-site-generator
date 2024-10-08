import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()
