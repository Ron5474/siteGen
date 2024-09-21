from htmlnode import HTMLNode

class LeafNode(HTMLNode):

	def __init__(self, value, tag=None, props=None):
		super().__init__(tag, value, None, props)
	
	def to_html(self):
		if not self.value:
			raise ValueError()
		if not self.tag:
			return self.value
		html = f"<{self.tag}"
		if self.props:
			prop_str = self.props_to_html()
			html = html + prop_str + '>'
		else:
			html += '>'
		html += self.value
		html += f'</{self.tag}>'
		return html
		
