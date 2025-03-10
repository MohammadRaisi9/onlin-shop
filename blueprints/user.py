from flask import Blueprint,render_template,request,redirect,url_for
from models.user import User
from passlib.hash import sha256_crypt
from extenoins import db
from flask_login import login_user

app=Blueprint("user",__name__)

@app.route('/user/login',methods=["GET","POST"])
def user():
    if request.method =="GET":
        return render_template("user/login.html")
    else:
        register=request.form.get("register",None)
        username=request.form.get("username")
        password=request.form.get("password")
        phone=request.form.get("phone")
        address=request.form.get("address")
        if register != None:
            user=User(username=username,password=sha256_crypt.encrypt(password),phone=phone,address=address)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect("/user/dashboard")