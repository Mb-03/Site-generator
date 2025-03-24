
class HTMLNode:
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        else:
            return f"{" ".join([f'{key}="{value}"' for key, value in self.props.items()])}"

    def __repr__(self):
        print(HTMLNode(self.tag, self.value, self.children, self.props))    


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props, children=None)

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return f"{self.value}"
        elif not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, props, children)
    
    def to_html(self):
        if not self.tag:
            raise ValueError
        elif not self.children:
            raise ValueError("ParentNode must have children")
        elif not self.props:
            return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"