from osm import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__():
        print(f"User('{self.username}','{self.email}')")

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(30),nullable=False)
    branch = db.Column(db.String(50),nullable=False)
    semester = db.Column(db.String(10), nullable=False)
    sem_type = db.Column(db.String(15), nullable=False)
    paper_type = db.Column(db.String(10), nullable=False)
    date_accessed = db.Column(db.DateTime , nullable=False, default=datetime.utcnow)
    faculty = db.Column(db.String(50), nullable=False)
    target = db.Column(db.Integer, nullable=False)
    paper_accessed = db.Column(db.Integer, nullable=False)
    paper_moderated = db.Column(db.Integer, default=0)
    percent = db.Column(db.Integer)
