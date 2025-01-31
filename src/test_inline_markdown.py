import unittest

from inline_markdown import (extract_markdown_images, extract_markdown_links,
                             split_nodes_delimiter, split_nodes_images,
                             split_nodes_links, text_to_textnodes)
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node with some `code`", TextType.BOLD)
        expected = [
            TextNode("This is a text node with some ", TextType.BOLD, None),
            TextNode("code", TextType.CODE, None),
        ]
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), expected)

    def test_eq2(self):
        node = TextNode(
            "This is a text node with some `code` and some `more code`", TextType.BOLD
        )
        expected = [
            TextNode("This is a text node with some ", TextType.BOLD, None),
            TextNode("code", TextType.CODE, None),
            TextNode(" and some ", TextType.BOLD, None),
            TextNode("more code", TextType.CODE, None),
        ]
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), expected)

    def test_eq3(self):
        node = TextNode("This is some **bold** text", TextType.ITALIC)
        expected = [
            TextNode("This is some ", TextType.ITALIC, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(" text", TextType.ITALIC, None),
        ]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), expected)

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.BOLD),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.BOLD
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.BOLD),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.BOLD),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.BOLD
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.BOLD),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.BOLD),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.BOLD),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.BOLD),
            ],
            new_nodes,
        )


class TestExtractLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )


class TestSplitLinks(unittest.TestCase):
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.BOLD,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.BOLD),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.BOLD,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.BOLD,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.BOLD),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.BOLD),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.BOLD,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.BOLD),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.BOLD),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.BOLD),
            ],
            new_nodes,
        )


class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes_eq1(self):
        text = "This is some code: `print('hello')`. find the source code [here](www.github.com/Brianstein27)"
        expected_nodes = [
            TextNode("This is some code: ", TextType.NORMAL),
            TextNode("print('hello')", TextType.CODE),
            TextNode(". find the source code ", TextType.NORMAL),
            TextNode("here", TextType.LINK, "www.github.com/Brianstein27"),
        ]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_text_to_textnodes_eq2(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]


if __name__ == "__main__":
    unittest.main()
