from application import db
from application.models import Base
from application.role import models
from sqlalchemy.sql import text


roles = db.Table('user_role',
                   db.Column('account_id', db.Integer,
                             db.ForeignKey('account.id'), primary_key=True),
                   db.Column('role_id', db.Integer,
                             db.ForeignKey('role.id'), primary_key=True)
                   )


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    
    role = db.relationship('Role', secondary=roles, backref=db.backref(
        'userroles', lazy='dynamic'))

    threads = db.relationship("Thread", backref='account', lazy=True)

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
        stmt = text("SELECT name, COUNT(Comment.account_id) FROM account "
                "LEFT JOIN Comment ON account.id = Comment.account_id "
                "GROUP BY account.id")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "amount":row[1]})

        return response



    @staticmethod
    def get_username(accountsid):   
        #figure out how to call this from html {{ }}
        stmt = text("SELECT username FROM account WHERE account.id = :accountsid;").params(accountsid = accountsid)
        response = db.engine.execute(stmt)
        return response



