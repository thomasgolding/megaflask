from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_login import LoginManager

demoapp = Flask(__name__)
demoapp.config.from_object(Config)

db = SQLAlchemy(demoapp)
migrate = Migrate(demoapp, db)
login = LoginManager(demoapp)

## define the endpoint for logging in.
login.login_view = 'login'

from appfolder import routes, models


# comment s