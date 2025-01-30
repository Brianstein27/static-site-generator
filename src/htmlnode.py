# represents nodes in an HTML document tree


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    # prints the props in an html compatible string
    def props_to_html(self):
        if self.props is None:
            return ""

        attributes = []
        for prop in self.props:
            attributes.append(f'{prop}="{self.props[prop]}"')

        return " ".join(attributes)

    # sets default behavior of equality comparison between to HTMLNode instances
    def __eq__(self, other) -> bool:
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    # sets print format of HTMLNode instances
    def __repr__(self) -> str:
        self_class = str(self.__class__).split(".")[1].split("'")[0]
        return f"{type(self).__name__}({self.tag}, {self.value}, children: {self.children}, props: {self.props})"


# represents a node in an HTML document tree that has no children. It's a "leaf" on a tree
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        elif self.tag is None:
            return self.value
        else:
            if self.props is None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"


# handles nesting of HTMLNodes inside each other. Any node with children is a parent node
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: Parent Node has no tag")

        if self.children is None:
            raise ValueError("Invalid HTML: Parent Node has no children")

        opening_tag = f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return opening_tag + children_html + closing_tag
