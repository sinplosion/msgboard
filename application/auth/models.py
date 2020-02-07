from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=True)
    role = db.relationship("Role")

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


    @staticmethod
    def comment_count():
        stmt = text("SELECT Account.name, COUNT(Comment.account_id) FROM account "
                "LEFT JOIN Comment ON account.id = Comment.account_id")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "amount":row[1]})

        return response
        
class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name




