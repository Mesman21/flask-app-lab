from flask import render_template, abort
from . import products_bp
from .models import Product
from app import db

@products_bp.route("/")
def list_products():
    products = db.session.query(Product).all()
    return render_template("products/list.html", products=products)

@products_bp.route("/<int:product_id>")
def product_detail(product_id):
    product = db.session.get(Product, product_id)
    if not product:
        abort(404)
    return render_template("products/detail.html", product=product, product_id=product_id)