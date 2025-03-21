from Inhe_main import app
from Inhe_dbModel import db

with app.app_context():
    db.create_all()