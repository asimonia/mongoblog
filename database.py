import pymongo

class Database:
	URI = 'mongodb://127.0.0.1:27017'
	DATABASE = None

	@staticmethod
	def initialize():
		"""Initialize the database"""
		client = pymongo.MongoClient(Database.URI)
		Database.DATABASE = client['fullstack']

	@staticmethod
	def insert(collection, data):
		"""Inserts data into a collection of the database"""
		Database.DATABASE[collection].insert(data)

	@staticmethod
	def find(collection, query):
		"""Returns document from a collection"""
		Database.DATABASE[collection].find(query)

	@staticmethod
	def find_one(collection, query):
		"""Return a row from a document in a collection"""
		Database.DATABASE[collection].find_one(query)

