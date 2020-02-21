from application import db

class Comment(db.Model):
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