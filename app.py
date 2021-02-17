from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import requests
from data import data

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to the best online shop in SG"

@app.route('/brands')
def get_all_brands() :
    return jsonify(data['brands'])

@app.route('/brands/<int:id>')
def get_brand_by_id(id) :
    for brand in data['brands']:
        if brand['id'] == id:
            return brand

    return jsonify(error = "Brand id does not correspond with any brands."), 404

@app.route('/brands/name/<name>')
def get_brands_by_name(name) :
    output = []

    for brand in data['brands']:
        if brand['name'].upper() == name.upper():
            output.append(brand)

    return jsonify(output)

@app.route('/products')
def get_all_products() :
    return jsonify(data['products'])

@app.route('/products/<int:id>')
def get_product_by_id(id):
    for product in data['products']:
        if product['id'] == id:
            return product

    return jsonify(error = "Product id does not correspond with any products."), 404

@app.route('/products/name/<name>')
def get_products_by_name(name):
    output = []
    for product in data['products']:
        if name in product['name']:
            output.append(product)

    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
