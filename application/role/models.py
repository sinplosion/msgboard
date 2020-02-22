from application import db
from application.models import Base
from sqlalchemy import event, DDL

class Role(Base):
    name = db.Column(db.String(10), nullable=False)
    
event.listen(Role.__table__,'after_create',
            DDL(""" INSERT INTO Role (name) VALUES ('USER'), ('MOD'), ('ADMIN') """))
