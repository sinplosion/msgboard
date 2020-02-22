from application import db
from application.models import Base


class Role(Base):
    name = db.Column(db.String(10), nullable=False)

class UserRole(Base):
    account_id = db.Column(db.Integer,db.ForeignKey('account.id'))
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'), nullable=False)
    account = db.relationship('Account', backref='account_role')
    role = db.relationship('Role', backref='role_account')


    

