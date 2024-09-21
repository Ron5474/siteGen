import unittest
from htmlnode import HTMLNode

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
		

if __name__ == "__main__":
	unittest.main()

