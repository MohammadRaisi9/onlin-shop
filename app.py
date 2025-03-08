from flask import Flask
from flask_wtf.csrf import CSRFProtect
from blueprints.general import app as general
from blueprints.user import app as user
from blueprints.admin import app as admin 
import config
import extenoins

app=Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)


app.config["SQLALCHEMY_DATABASE_URI"]=config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"]=config.SECRET_KEY
extenoins.db.init_app(app)

csrf=CSRFProtect(app)

with app.app_context():
    extenoins.db.create_all()

if __name__=='__main__':
    app.run(debug=True)