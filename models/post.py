class Post:

	def __init__(self, blog_id, title, content, author, date, id):
		self.blog_id = blog_id
		self.title = title
		self.content = content
		self.author = author
		self.created_date = date
		self.id = id

	def save_to_mongo(self):
		"""Save a post to the mongo database"""
		Database.insert(collection='posts', data=self.json())

	def json(self):
		"""Returns a json representation of the object"""
		return {
			'id': self.id,
			'blog_id': self.blog_id,
			'author': self.author,
			'content': self.content,
			'title': self.title,
			'created_date': self.created_date
		}