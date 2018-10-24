from app import app


@app.route('/')
def index():
	return '<h1>Index Page<h1>'