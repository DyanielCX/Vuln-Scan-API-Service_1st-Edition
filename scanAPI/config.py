from flask import Flask
from dbModel import db

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scanInfo_database.db'
db.init_app(app)