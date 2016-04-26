from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
# from flask.ext.migrate import Migrate, MigrateCommand
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

manager = Manager(app)
# manager.add_command('db', MigrateCommand)

Bootstrap(app)
from app import views, models