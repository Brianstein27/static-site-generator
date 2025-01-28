from textnode import TextNode, TextType


def main():
    node = TextNode("This is some text", TextType.BOLD, "www.google.com")
    print(node)


main()
