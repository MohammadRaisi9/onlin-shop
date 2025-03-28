from flask import Blueprint,render_template,request,redirect,url_for,flash
from models.user import User
from models.cart import Cart
from models.product import Product
from models.cart_item import CartItem
from passlib.hash import sha256_crypt
from extenoins import db
from flask_login import login_user,login_required,current_user

app=Blueprint("user",__name__)

@app.route('/user/login',methods=["GET","POST"])
def login():
    if request.method =="GET":
        return render_template("user/login.html")
    else:
        register=request.form.get("register",None)
        username=request.form.get("username",None)
        password=request.form.get("password",None)
        phone=request.form.get("phone",None)
        address=request.form.get("address",None)
        if register != None:
            user=User.query.filter(User.username==username).first()
            if user==None:
                flash("نام کاربری تکراری است!")
                return redirect(url_for("user.login"))
            user=User(username=username,password=sha256_crypt.encrypt(password),phone=phone,address=address)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("user.dashboard"))
        else:
            user=User.query.filter(User.username==username).first()
            if user==None:
                flash("نام کاربری یا رمز اشتباه است")
                return redirect(url_for("user.login"))
            if sha256_crypt.verify(password,user.password):
                login_user(user)
                return redirect(url_for("user.dashboard"))
            else:
                flash("نام کاربری یا رمز اشتباه است")
                return redirect(url_for("user.login"))



@app.route('/add-to-cart',methods=["GET"])
@login_required
def add_to_cart():
    id=request.args.get("id")
    product=Product.query.filter(Product.id==id).first_or_404()
    
    cart=current_user.carts.filter(Cart.status=="pending").first()
    if cart==None:
        cart=Cart()
        current_user.carts.append(cart)
        
    cart_item=cart.cart_items.filter(CartItem.product==product).first()
    
    if cart_item==None:
        item=CartItem(quantity=1)
        item.cart=cart
        item.product=product
        db.session.add(item)
    else:
        cart_item.quantity += 1
    db.session.add(cart)
    
    db.session.commit()
    return redirect(url_for("user.cart"))



@app.route('/cart',methods=["GET"])
@login_required
def cart():
    return render_template("user/cart.html")



@app.route('/user/dashboard',methods=["GET"])
@login_required
def dashboard():
    return "this is dashboard"