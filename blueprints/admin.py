from flask import Blueprint,render_template,request,redirect,session,abort,url_for
import config
from models.product import Product
from extenoins import db

app=Blueprint("admin",__name__)

@app.before_request
def before_request():
    if session.get("admin_login",None)==None and request.endpoint != "admin.login":
        abort(403)

@app.route('/admin/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        username=request.form.get("username",None)
        password=request.form.get("password",None)
        if username==config.ADMIN_USERNAME and password==config.ADMIN_PASSWORD:
            session["admin_login"]=username
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")
    else:
        return render_template("admin/login.html")


@app.route('/admin/dashboard',methods=["GET"])
def dashboard():
    return render_template("admin/dashboard.html")


@app.route('/admin/dashboard/products',methods=["POST","GET"])
def products():
    if request.method=="GET":
        products=Product.query.all()
        return render_template("admin/products.html",products=products)
    else:
        name=request.form.get("name",None)
        description=request.form.get("description",None)
        price=request.form.get("price",None)
        active=request.form.get("active",None)
        file=request.files.get("cover",None)
        
        p = Product(name=name,description=description,price=price)
        if active==None:
            p.active = 0
        else:
            p.active = 1
        db.session.add(p)
        db.session.commit()
        
        file.save(f"static/cover/{p.id}.jpg")
        return "done"
    

@app.route('/admin/dashboard/edit-product/<id>',methods=["POST","GET"])
def edit_product(id):
    product=Product.query.filter(Product.id == id).first_or_404()
    if request.method=="GET":
        return render_template("admin/edit-product.html",product=product)
    else:
        name=request.form.get("name")
        description=request.form.get("description")
        price=request.form.get("price")
        active=request.form.get("active")
        file=request.files.get("cover",None)
        
        product.name=name
        product.description=description
        product.price=price
        if active==None:
            product.active = 0
        else:
            product.active = 1
        
        if file != None:
            file.save(f"static/cover/{product.id}.jpg")
        
        db.session.commit()
        
        
            
        return redirect(url_for("admin.edit_product",id=id))