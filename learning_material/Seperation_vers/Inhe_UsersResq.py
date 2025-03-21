from flask_restful import Resource, marshal_with
from Inhe_dbModel import UserModel, db
from Inhe_RespFmt import user_agrs, UserFields

"""
Users Resource (All Users)
- Purpose: Manage users data (GET/POST)
- Route: '/api/users' 
- Methods: GET, POST
"""
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