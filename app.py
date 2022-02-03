from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import requests
import data

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to the best online shop in SG"

@app.route('/brands')
def get_all_brands():
    return jsonify(data.get_all_brands())

@app.route('/brands/<int:id>')
def get_brand_by_id(id):
    brand = data.get_brand_by_id(id)
    if brand is not None:
        return jsonify(brand)
    return jsonify(error = "Brand id does not correspond with any products."), 404

@app.route('/brands/name/<name>')
def get_brands_by_name(name):
    return jsonify(data.get_brands_by_name(name))

@app.route('/products')
def get_all_products():
    return jsonify(data.get_all_products())

@app.route('/products/<int:id>')
def get_product_by_id(id):
    product = data.get_product_by_id(id)
    if product is not None:
        return jsonify(product)

    return jsonify(error = "Product id does not correspond with any products."), 404

@app.route('/products/name/<name>')
def get_products_by_name(name):
    return jsonify(data.get_products_by_name(name))

@app.route('/brands/<int:id>/products')
def get_products_by_brand(id):
    return jsonify(data.get_products_by_brand(id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
