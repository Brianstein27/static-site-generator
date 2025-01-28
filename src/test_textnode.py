import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    # Both test functions and file names must start with test_ to be discoverable by unittest
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode(
            "This is a different text node", TextType.ITALIC, "www.brian.de"
        )
        node2 = TextNode(
            "This is a different text node", TextType.ITALIC, "www.brian.de"
        )
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.brian.de")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.emma.de")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
