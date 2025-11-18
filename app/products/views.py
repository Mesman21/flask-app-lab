from flask import render_template
from . import products_bp

@products_bp.route("/")
def list_products():
    products = [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Mouse"}]
    return render_template("products/list.html", products=products)

@products_bp.route("/<int:product_id>")
def product_detail(product_id):
    return render_template("products/detail.html", product_id=product_id)