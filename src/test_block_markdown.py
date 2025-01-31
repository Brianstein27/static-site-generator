import unittest

from block_markdown import block_to_block_type, markdown_to_blocks


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
