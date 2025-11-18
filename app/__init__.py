from flask import Flask
from .users import users_bp
from .products import products_bp

app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)

from . import views