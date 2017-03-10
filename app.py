from database import Database
from models.post import Post

Database.initialize()

blog = Blog(author="Alex",
			title="Sample",
			description="Sample description")

blog.new_post()

blog.save_to_mongo()

Blog.from_mongo()

blog.get_posts()