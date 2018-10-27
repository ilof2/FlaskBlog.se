from flask import Blueprint
from flask import render_template

from models import Post, Tag

posts = Blueprint('posts', __name__, template_folder = 'templates')

@posts.route('/')
def index():
	posts = Post.query.all()
	return render_template('posts/index.html', posts = posts)
# /blog/post-name
@posts.route('/<slug>')
def post_datails(slug):
	post = Post.query.filter(Post.slug == slug).first()
	tags = post.tags
	return render_template('posts/post_full.html', post = post, tags = tags)

# /blog/tag/tag-slug
@posts.route('/tag/<slug>')
def tag_datails(slug):
	tag = Tag.query.filter(Tag.slug == slug).first()
	posts = tag.posts.all()
	return render_template('posts/tags_posts.html', tag = tag, posts = posts)