from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

# Setup Flask, Database, REST API
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

# Database Model
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"

# Define User Agrs
user_agrs = reqparse.RequestParser()
user_agrs.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_agrs.add_argument('email', type=str, required=True, help="Email cannot be blank")

# User format in Response
UserFields = {
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String, 
}

''' All Users '''
class Users(Resource):
    
    # Get Request
    @marshal_with(UserFields)
    def get(self):
        users = UserModel.query.all()
        return users
    
    # Post Request
    @marshal_with(UserFields)
    def post(self):
        agrs = user_agrs.parse_args()
        user = UserModel(name=agrs["name"], email=agrs["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201

''' Single User '''
class User(Resource):
    # Get Request
    @marshal_with(UserFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        return user
    
    # Patch Request
    @marshal_with(UserFields)
    def patch(self, id):
        agrs = user_agrs.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        user.name = agrs["name"]
        user.email = agrs["email"]
        db.session.commit()
        return user
    
    # Delete Request
    @marshal_with(UserFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users

# Create api/users Resource Endpoint
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/user/<int:id>')

# Prepare Route
@app.route('/')
def index():
    return '<h1>Flask REST API</h1>'

if __name__ == '__main__':
    app.run(debug=True)