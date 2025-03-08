from sqlalchemy import *
from extenoins import db

class Product(db.Model):
    __tablename__="products"
    id =Column(Integer,primary_key=true,index=true)
    name =Column(String,unique=true,nullable=false,index=true)
    description =Column(String,nullable=false,index=true)
    price =Column(Integer,nullable=false,index=true)
    active =Column(Integer,nullable=false,index=true)
    