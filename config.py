class Configuration(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/blog'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'very secret key'

	### flask-security ###
	SECURITY_PASSWORD_SALT = 'easesalt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'