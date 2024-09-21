from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(children=children, tag=tag, props=props)

	def to_html(self):
		if not self.tag:
			raise ValueError()
		if not self.children:
			raise ValueError("Expected Children")
		st = ""
		for node in self.children:
			st += node.to_html()
		final_st = f'<{self.tag}>' + st + f'</{self.tag}>'
		return final_st
