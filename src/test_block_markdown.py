import unittest

from block_markdown import (block_to_block_type, extract_title,
                            markdown_to_blocks, markdown_to_html_node)


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks_eq1(self):
        markdown = """ # This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item"""
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
            * This is a list item
            * This is another list item""",
        ]

        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_blocktype_heading1(self):
        block = "# Hello"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "heading")

    def test_block_to_blocktype_heading2(self):
        block = "## Hello"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "heading")

    def test_block_to_blocktype_heading3(self):
        block = "### Hello"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "heading")

    def test_block_to_blocktype_heading4(self):
        block = "#### Hello"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "heading")

    def test_block_to_blocktype_heading5(self):
        block = "##### Hello"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "heading")

    def test_block_to_blocktype_heading6(self):
        block = "###### Hello"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "heading")

    def test_block_to_blocktype_heading7(self):
        block = "######Hello"
        blocktype = block_to_block_type(block)
        self.assertNotEqual(blocktype, "heading")

    def test_block_to_blocktype_code1(self):
        block = "```hello```"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "code")

    def test_block_to_blocktype_code2(self):
        block = "```  hello this is a codeblock ```"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "code")

    def test_block_to_blocktype_code3(self):
        block = "`  hello this is not a codeblock `"
        blocktype = block_to_block_type(block)
        self.assertNotEqual(blocktype, "code")

    def test_block_to_blocktype_quote(self):
        block = """> quote
        > this is a quote
        > so is this
        > and this
        """
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "quote")

    def test_block_to_block_type_unordered_list1(self):
        block = """* Hi
        * Bye
        * Goodnight"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "unordered_list")

    def test_block_to_block_type_unordered_list2(self):
        block = """- Hi
        - Bye
        - Goodnight"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "unordered_list")

    def test_block_to_block_type_ordered_list(self):
        block = """1. Hi
        2. Bye
        3. Night"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, "ordered_list")

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_extract_title_eq1(self):
        markdown = """
        # This is a title

        This is a regular paragraph
        This should be the same paragraph?

        - List item 1
        - List item 2
        - List item 3
        """
        self.assertEqual(extract_title(markdown), "This is a title")

    def test_extract_title_error1(self):
        markdown = """
        # This is a different title     

        This is a regular paragraph
        This should be the same paragraph?

        - List item 1
        - List item 2
        - List item 3
        """
        self.assertEqual(extract_title(markdown), "This is a different title")


if __name__ == "__main__":
    unittest.main()
