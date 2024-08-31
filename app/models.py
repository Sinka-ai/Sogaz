from datetime import datetime, timezone
from flask_login import UserMixin
from app import db, login

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)

    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_messages', lazy='joined')
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='received_messages', lazy='joined')

    def __repr__(self):
        return f"Message('{self.sender_id}', '{self.recipient_id}', '{self.content}', '{self.timestamp}')"


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



