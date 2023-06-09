from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

### Code GitHub
application.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
DBVAR=os.environ['DATABASE_URL']
# DBVAR="postgresql://username:os.environ.get(‘DB_PASSWORD’)@host:port/database"
# DBVAR="postgresql://username:password@host:port/database"
# application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
# application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

### Code computer
# DBVAR="postgresql://zoheeckhkpxbcv:e7feb75228a074fdd37e60d7c149df58f4ba3e011adc2459e83841483a7a3306@ec2-34-250-252-161.eu-west-1.compute.amazonaws.com:5432/df844lun2nfesb"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

