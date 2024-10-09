from textnode import TextNode

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        attriubtes = []
        for prop in self.props:
            attriubtes.append(f'{prop}="{self.props[prop]}"')

        return " ".join(attriubtes)

    def __repr__(self):
        return f"{type(self).__name__}({self.tag}, {self.value}, children: {self.children}, {self.props})"

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

