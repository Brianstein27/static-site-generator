from generate_page import generate_pages_recursively
from static_to_public import static_to_public


def main():
    static_to_public()
    generate_pages_recursively("./content", "./template.html", "./public")


main()
