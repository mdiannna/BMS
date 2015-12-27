from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from app import db

class UserData(db.Model, UserMixin):
	__tablename__ = "confidential"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))
	firstname = db.Column(db.String(255))
	lastname = db.Column(db.String(255))
	tel = db.Column(db.String(300))
	secret = db.Column(db.String(255))

	def set_password(self, password):
		self.parola = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pw_hash, password)

	def is_active(self):
		return True