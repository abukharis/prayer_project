# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import getenv
#from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

# create a new instance of Flask and store it in app 
app = Flask(__name__)
#bcrypt = Bcrypt(app)
DATABASE_URI="mysql+pymysql://root:salimd@35.242.160.164/prayer"
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

#app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')

# import the ./application/routes.py file
db=SQLAlchemy(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'login'

from application import routes
