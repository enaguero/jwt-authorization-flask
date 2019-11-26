from flask_sqlalchemy import SQLAlchemy
from utils import generate_hash, verify_hash
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = generate_hash(self.password)

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()