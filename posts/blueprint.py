from flask import Blueprint, request
from flask import render_template, redirect, url_for

from models import Post, Tag
from .forms import PostForm

from app import db


posts = Blueprint('posts', __name__, template_folder = 'templates')

# /blog/create
@posts.route('/create', methods = ['POST', 'GET'])
def create_post():

	if request.method == 'POST':
		title = request.form['title']
		body = request.form['body']

		try:
			post = Post(title = title, body = body)
			db.session.add(post)
			db.session.commit()
		except:
			print('Error!!!!')

		return redirect( url_for('posts.index'))


	form = PostForm()
	return render_template('posts/create_post.html', form = form)





@posts.route('/')
def index():
	q = request.args.get('q')

	if q:
		posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
	else:
		posts = Post.query.order_by(Post.created.desc())
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