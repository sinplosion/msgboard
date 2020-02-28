from application import db
from sqlalchemy import text
from application.models import Base

class Thread(Base):  
    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(8192), nullable=False)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    edited = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content


    @staticmethod
    def threadsInfo(threadsid):

        stmt = text ("SELECT Thread.title, Thread.content, Thread.created, Thread.edited, Account.name, Thread.id FROM Thread "
                "JOIN Account ON Account.id = Thread.account_id "
                "WHERE Thread.id = :tid")
    
        res = db.engine.execute(stmt, tid=threadsid)

        response = []

        for row in res:
            response.append({"title":row[0],"content":row[1],"created":row[2],"edited":row[3],"username":row[4],"id":row[5]})
    
        return response


    @staticmethod
    def listAllThreads():

        stmt = text ("SELECT Thread.title, Thread.created, Account.name, Thread.id FROM Thread "
                    "JOIN Account ON Account.id = Thread.account_id")
    
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"title":row[0],"created":row[1],"username":row[2],"id":row[3]})
    
        return response

