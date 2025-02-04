from block_markdown import extract_title
from generate_page import generate_page
from static_to_public import static_to_public


def main():
    generate_page("./content/index.md", "./template.html", "./public/index.html")


main()
