from flask import Flask
from flask_restful import Api
from Inhe_dbModel import db
from Inhe_UsersResq import Users
from Inhe_UserResq import User

# Setup Flask, Database, REST API
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Inhe_database.db'
db.init_app(app)
api = Api(app)

# Create api/users Resource Endpoint
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/user/<int:id>')

# Prepare Route
@app.route('/')
def index():
    return '<h1>Flask REST API</h1>'

if __name__ == '__main__':
    app.run(debug=True)