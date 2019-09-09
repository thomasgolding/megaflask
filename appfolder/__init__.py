from flask import Flask
from config import Config

demoapp = Flask(__name__)
demoapp.config.from_object(Config)

from appfolder import routes


# comment 