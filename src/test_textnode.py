import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a different text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", "italic", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a text node", "bold", "https://react.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        representation = 'TextNode(This is a text node, bold, None)'
        self.assertEqual(node.__repr__(), representation)

    def test_repr2(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        representation = 'TextNode(This is a text node, bold, https://boot.dev)'
        self.assertEqual(node.__repr__(), representation)



if __name__ == "__main__":
    unittest.main()
