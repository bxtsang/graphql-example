from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import requests

app = Flask(__name__)

data = {
    "brands": [
        {
            "id": 1,
            "name": "Apple"
        },
        {
            "id": 2,
            "name": "Huawei"
        },
        {
            "id": 3,
            "name": "Dell"
        }
    ],
    "products": [
        {
            "id": 1,
            "name": "Macbook Pro 16 inch",
            "price": 3000,
            "brand": 1,
            "stock": 12,
            "parent": None
        },
        {
            "id": 2,
            "name": "XPS 13",
            "price": 2800,
            "brand": 3,
            "stock": 4,
            "parent": None
        },
        {
            "id": 3,
            "name": "Matebook Pro",
            "price": 2300,
            "brand": 2,
            "stock": 25,
            "parent": None
        },
        {
            "id": 4,
            "name": "IPad Pro",
            "price": 1500,
            "brand": 1,
            "stock": 3,
            "parent": None
        },
        {
            "id": 5,
            "name": "Apple Pencil",
            "price": 200,
            "brand": 1,
            "stock": 8,
            "parent": 4
        },
        {
            "id": 6,
            "name": "IDock",
            "price": 100,
            "brand": 1,
            "stock": 80,
            "parent": 1
        },
        {
            "id": 7,
            "name": "The best IPad case",
            "price": 50,
            "brand": 1,
            "stock": 100,
            "parent": 4
        }
    ]
}

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
