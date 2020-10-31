from flask import Flask

app = Flask(__name__)

from app import flaskRoutes
from app import elasticRoutes
