from sqlalchemy import *
from extenoins import db

class User(db.Model):
    __tablename__="users"
    id=Column(Integer,primary_key=true,index=true)
    username=Column(String,unique=true,nullable=false,index=true)
    password=Column(String(11),nullable=false,index=true)
    phone=Column(String,nullable=false,index=true)
    address=Column(String,nullable=false,index=true)