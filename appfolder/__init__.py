from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 



demoapp = Flask(__name__)
demoapp.config.from_object(Config)

db = SQLAlchemy(demoapp)
migrate = Migrate(demoapp, db)


from appfolder import routes, models


# comment s