from sqlalchemy import *
from extenoins import db

class Payment(db.Model):
    __tablename__="payment"
    id=Column(Integer,primary_key=true)
    status=Column(String,default="pending")
    cart_id=Column(Integer,ForeignKey('carts.id'),nullable=False)
    cart=db.relationship('Cart',backref='payments')
    