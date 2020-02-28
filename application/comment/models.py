from application import db
from application.models import Base
from sqlalchemy import text


class Comment(Base):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    edited = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    
    content = db.Column(db.String(8192), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
        nullable=False)

    thread_id = db.Column(db.Integer, db.ForeignKey('account.id'),
        nullable=False)

    def __init__(self, content):
        self.content = content


    @staticmethod
    def listComments(threadsid):

        stmt = text ("SELECT Comment.content, Comment.created, Comment.edited, Account.name, Comment.thread_id, Comment.id FROM Comment "
                "JOIN Account ON Account.id = Comment.account_id "
                "WHERE Comment.thread_id = :tid")
    
        res = db.engine.execute(stmt, tid=threadsid)

        response = []

        for row in res:
            response.append({"comment":row[0],"created":row[1],"edited":row[2],"username":row[3], "id":row[4]})
    
        return response

    @staticmethod
    def deleteCommentsThread(threadsid):

        stmt = text ("DELETE FROM Comment WHERE thread_id = :tid")

        res = db.engine.execute(stmt, tid= threadsid)