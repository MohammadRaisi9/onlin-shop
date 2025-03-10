from sqlalchemy import *
from extenoins import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__="users"
    id=Column(Integer,primary_key=true,index=true)
    username=Column(String,unique=true,nullable=false,index=true)
    password=Column(String(11),nullable=false,index=true)
    phone=Column(String,nullable=false,index=true)
    address=Column(String,nullable=false,index=true)