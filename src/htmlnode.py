

class HTMLNode:
	
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	
	def to_html(self):
		raise NotImplementedError()
	
	def props_to_html(self):
		html = ""
		if not self.props:
			return html
		for key, value in self.props.items():
			html += f' {key}="{value}"'
		return html
	
	def __repr__(self):
		return f'(HTML NODE: {self.tag}, {self.value}, {self.children}, {self.props_to_html()})'
	
	
		
