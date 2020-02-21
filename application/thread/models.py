from application import db

from application.models import Base

class Thread(Base):  
    title = db.Column(db.String(144), nullable=False)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

def __init__(self, title):
    self.title = title