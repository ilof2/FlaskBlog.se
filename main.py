#! ../venv/bin/python3
from app import app, db
import view
from posts.blueprint import posts

from models import Post

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
	app.run()