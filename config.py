class Configuration(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/blog'
	SQLALCHEMY_TRACK_MODIFICATIONS = False