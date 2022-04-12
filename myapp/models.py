#models 
from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
#allows to set up isAuthenticate etc 
from flask_login import UserMixin
from datetime import datetime

#login management 
# allows us to use this in templates for isUser stuff 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    cards = db.relationship('TimeCard', backref='employee', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

#going to use this in our login view 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"

class TimeCard(db.Model):
    __tablename__ = 'time_cards'
    id = db.Column(db.Integer, primary_key=True)
    time_in = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_out = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"Card ID: {self.id} -- In: {self.time_in} -- Out: {self.time_out}"



