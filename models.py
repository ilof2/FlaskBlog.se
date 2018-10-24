from datetime import datetime
from app import db
import re




def slugify(title):
	pattern = r'[^\w+]'
	return re.sub(pattern, '-', title.lower())

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(140))
	slug = db.Column(db.String(140), unique = True)
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		self.generate_slug()


	def generate_slug(self):
		if self.title:
			self.slug = slugify(self.title)


	def __repr__(self):
		return '<Post id: {0}, title: {1}>'.format(self.id, self.title)