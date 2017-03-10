import uuid
from database import Database
import datetime

class Post:

	def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
		"""universal unique id for each blog post"""
		self.blog_id = blog_id
		self.title = title
		self.content = content
		self.author = author
		self.created_date = date
		self.id = uuid.uuid4().hex if id is None else id

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

	@staticmethod
	def from_mongo(id):
		"""Return data from the mongo db"""
		return Database.find_one(collection='posts', query={'id': id})

	@staticmethod
	def from_blog(id):
		"""Return data from the blog"""
		return [post for post in Database.find(collection='posts', query={'blog_id': id})]

