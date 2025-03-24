
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return f"{"".join([f'{key}="{value}" ' for key, value in self.props.items()])}"

    def __repr__(self):
        print(HTMLNode(self.tag, self.value, self.children, self.props))    


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=None)

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")