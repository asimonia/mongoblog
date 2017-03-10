from database import Database
from models.post import Post

Database.initialize()

post = Post(blog_id="123", 
			title="Another great post", 
			content="Sample content", 
			author="Alex")

post.save_to_mongo()