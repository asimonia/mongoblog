from models.post import Post

post = Post()
post2 = Post()
post2.content = "Some different content"

print(post.content)
print(post2.content)