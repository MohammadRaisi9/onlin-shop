from sqlalchemy import *
from extenoins import db
from sqlalchemy.orm import backref

class CartItem(db.Model):
    __tablename__="cart_items"
    id=Column(Integer,primary_key=true)
    product_id=Column(Integer,ForeignKey('products.id'),nullable=False)
    cart_id=Column(Integer,ForeignKey('carts.id'),nullable=False)
    quantity=Column(Integer)
    
    product=db.relationship('Product',backref='cart_items')
    cart=db.relationship('Cart',backref=backref('cart_items',lazy="dynamic"))
    