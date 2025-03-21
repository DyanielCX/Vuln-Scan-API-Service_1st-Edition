from flask_restful import Resource, marshal_with, abort
from Inhe_dbModel import UserModel, db
from Inhe_RespFmt import user_agrs, UserFields

"""
User Resource (Single User)
- Purpose: Manage individual user data (GET/PATCH/DELETE)
- Route: '/api/user/<int:id>' 
- Methods: GET, PATCH, DELETE
"""
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