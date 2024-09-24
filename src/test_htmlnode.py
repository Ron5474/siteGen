import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestHTMLNODE(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a html node")
        node2 = HTMLNode("p", "This is a html node")
        self.assertEqual(print(node),print(node2))
	
    def test_not_eq(self):
        node = HTMLNode("p", "This is a html node")
        node2 = HTMLNode("a", "Go To Boot.dev", [node], {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(' href="https://www.boot.dev" target="_blank"', node2.props_to_html())
		
    def test_url(self):
        node = HTMLNode("p", "This is a html node")
        node2 = HTMLNode("h1", "WELCOME TO THE PAGE", [node])
        self.assertNotEqual(node, node2)
    
    def test_to_html_no_child(self):
        node = LeafNode("h1", "Hello, People!")
        self.assertEqual(node.to_html(), "<h1>Hello, People!</h1>")
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, People!")
        self.assertEqual(node.to_html(), "Hello, People!")
    
    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )
    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
    
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
        

if __name__ == "__main__":
	unittest.main()

