from flask_restful import fields, reqparse

# Define User Args
user_agrs = reqparse.RequestParser()
user_agrs.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_agrs.add_argument('email', type=str, required=True, help="Email cannot be blank")

# User format in Response
UserFields = {
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String, 
}