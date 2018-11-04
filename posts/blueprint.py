from flask import Blueprint, request
from flask import render_template, redirect, url_for

from models import Post, Tag
from .forms import PostForm, PostForm

from app import db

from flask_security import login_required

posts = Blueprint('posts', __name__, template_folder = 'templates')


# /blog/create

@posts.route('/create', methods = ['POST', 'GET'])
@login_required
def create_post():

	if request.method == 'POST':
		title = request.form['title']
		body = request.form['body']
		tags = request.form['tags']

		try:
			tag = Tag(name = tags)
			post = Post(title = title, body = body)
			post.tags.append(tag)
			db.session.add(post)
			db.session.add(tag)
			db.session.commit()
		except:
			print('Error!!!!')

		return redirect( url_for('posts.index'))


	form = PostForm()
	return render_template('posts/create_post.html', form = form)


# /blog/post-slug/edit
@posts.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
	post = Post.query.filter(Post.slug==slug).first()
	if request.method == 'POST':
		form = EditPostForm(formdata=request.form, obj=post)
		form.populate_obj(post)
		db.session.commit()

		return redirect(url_for('posts.post_details', slug = post.slug))

	form = PostForm(obj = post)
	return render_template('posts/edit_post.html', post=post, form = form)



# /blog/
@posts.route('/')
def index():

	q = request.args.get('q')
	page = request.args.get('page')

	if page and page.isdigit():
		page = int(page)
	elif page:
		page = 1


	if q:
		posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
	else:
		posts = Post.query.order_by(Post.id.desc())

	pages = posts.paginate(page=page, per_page=4)

	return render_template('posts/index.html', pages = pages)


# /blog/post-name
@posts.route('/<slug>')
def post_details(slug):
	post = Post.query.filter(Post.slug == slug).first()
	tags = post.tags
	return render_template('posts/post_full.html', post = post, tags = tags)

# /blog/tag/tag-slug
@posts.route('/tag/<slug>')
def tag_datails(slug):
	tag = Tag.query.filter(Tag.slug == slug).first()
	posts = tag.posts.all()
	return render_template('posts/tags_posts.html', tag = tag, posts = posts)