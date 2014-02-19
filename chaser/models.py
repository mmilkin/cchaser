from chaser import db
from passlib.apps import custom_app_context as pwd_context

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(320), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    @staticmethod
    def get_hash(password):
        return pwd_context.encrypt(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __init__(self, user_name=None, password=None, role=ROLE_USER):
        self.user_name = user_name
        self.password = User.get_hash(password)
        self.role = role

    def __repr__(self):
        return '<User %r>' % (self.user_name)

    def hash_password(self, password):
        self.password = User.get_hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)
