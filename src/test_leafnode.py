import unittest
from leafnode import LeafNode

class TestHTMLNODE(unittest.TestCase):
	def test_eq(self):
		node = LeafNode(tag="p", value="This is a leaf node")
		node2 = LeafNode(tag="p", value="This is a leaf node")
		self.assertEqual(node.__repr__(), node2.__repr__())
	
	def test_not_eq(self):
		node = LeafNode(tag="p", value="This is a html node")
		node2 = LeafNode(tag="a", value="Go To Boot.dev", props={"href": "https://www.boot.dev", "target": "_blank"})
		self.assertEqual(' href="https://www.boot.dev" target="_blank"', node2.props_to_html())
		
	def test_url(self):
		node = LeafNode(tag="p", value="This is a html node")
		node2 = LeafNode(tag="h1", value="WELCOME TO THE PAGE")
		self.assertEqual(node.to_html(), "<p>This is a html node</p>")
		

if __name__ == "__main__":
	unittest.main()

