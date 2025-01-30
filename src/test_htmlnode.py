import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_eq1(self):
        node1 = HTMLNode("p", "This is some text", None, {"class": "w-10"})
        node2 = HTMLNode("p", "This is some text", None, {"class": "w-10"})

        self.assertEqual(node1, node2)

    def test_eq2(self):
        node1 = HTMLNode("p", "This is some text", None, {"class": "w-10"})
        node2 = HTMLNode("p", "This is some text", None, {"class": "w-10"})

        self.assertEqual(node1.props_to_html(), node2.props_to_html())

    def test_eq3(self):
        node1 = HTMLNode("p", "This is some text", None, {"class": "w-8"})
        node2 = HTMLNode("p", "This is some text", None, {"class": "w-10"})

        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())


class TestLeafNode(unittest.TestCase):
    def test_eq1(self):
        node1 = LeafNode("p", "Hi")
        node2 = LeafNode("p", "Hi")

        self.assertEqual(node1.to_html(), node2.to_html())

    def test_eq2(self):
        node1 = LeafNode("p", "Hi", {"class": "w-10"})
        node2 = LeafNode("p", "Hi", {"class": "w-10"})

        self.assertEqual(node1.to_html(), node2.to_html())

    def test_eq3(self):
        node1 = LeafNode("a", "Hi", {"class": "w-10", "href": "www.hi.de"})
        node2 = LeafNode("a", "Hi", {"class": "w-10", "href": "www.hi.de"})

        self.assertEqual(node1.to_html(), node2.to_html())

    def test_eq4(self):
        node1 = LeafNode("p", "Hi")
        node2 = LeafNode("p", "Hi")

        self.assertEqual(node1, node2)

    def test_eq5(self):
        node1 = LeafNode("p", "Hi", {"class": "w-10"})
        node2 = LeafNode("p", "Hi", {"class": "w-10"})

        self.assertEqual(node1, node2)

    def test_eq6(self):
        node1 = LeafNode("a", "Hi", {"class": "w-10", "href": "www.hi.de"})
        node2 = LeafNode("a", "Hi", {"class": "w-10", "href": "www.hi.de"})

        self.assertEqual(node1, node2)

    def test_n_eq1(self):
        node1 = LeafNode("a", "Hi", {"class": "w-4", "href": "www.hi.de"})
        node2 = LeafNode("a", "Hi", {"class": "w-10", "href": "www.hi.de"})

        self.assertNotEqual(node1, node2)

    def test_n_eq2(self):
        node1 = LeafNode("p", "Hi")
        node2 = LeafNode("b", "Hi")

        self.assertNotEqual(node1, node2)

    def test_n_eq3(self):
        node1 = LeafNode("a", "Hi", {"class": "w-4", "href": "www.hi.de"})
        node2 = LeafNode("a", "Hi", {"class": "w-10", "href": "www.hi.de"})

        self.assertNotEqual(node1.to_html(), node2.to_html())


class TestParentNode(unittest.TestCase):
    def test_repr(self):
        node = ParentNode(
            "p", [LeafNode("b", "Bold text"), LeafNode("b", "Normal text")]
        )
        self.assertEqual(
            node.__repr__(),
            "ParentNode(p, None, children: [LeafNode(b, Bold text, children: None, props: None), LeafNode(b, Normal text, children: None, props: None)], props: None)",
        )

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

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

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
