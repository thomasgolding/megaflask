from flask import Flask

demoapp = Flask(__name__)

from appfolder import routes
