# handling all types of inline text
from enum import Enum


# defining text types
class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    # sets default behavior of equality comparison between to TextNode instances
    def __eq__(self, other) -> bool:
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True

        return False

    # sets print format of TextNode instances
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
