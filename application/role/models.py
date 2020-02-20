from application import db

class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name