from sqlalchemy import *
from extenoins import db
from sqlalchemy.orm import backref

class Cart(db.Model):
    __tablename__="carts"
    id=Column(Integer,primary_key=true)
    status=Column(String,default="pending")
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False)
    user=db.relationship('User',backref=backref('carts',lazy="dynamic"))
    