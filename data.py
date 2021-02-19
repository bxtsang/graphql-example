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

def get_all_brands() :
    return data['brands']

def get_brand_by_id(id) :
    for brand in data['brands']:
        if brand['id'] == id:
            return brand

    return None

def get_brands_by_name(name) :
    output = []

    for brand in data['brands']:
        if name.upper() in brand['name'].upper():
            output.append(brand)

    return output

def add_brand(name):
    id = data['brands'][-1]['id'] + 1
    brand = {'id': id, 'name': name}

    data['brands'].append(brand)
    return brand

def get_all_products() :
    return data['products']

def get_product_by_id(id):
    for product in data['products']:
        if product['id'] == id:
            return product

    return None

def get_products_by_name(name):
    output = []
    for product in data['products']:
        if name.upper() in product['name'].upper():
            output.append(product)

    return output

def get_products_by_brand(brand_id):
    output = []
    for product in data['products']:
        if product['brand_id'] == brand_id:
            output.append(product)

    return output

def add_product(product):
    id = data['products'][-1]['id'] + 1
    product['id'] = id
    if 'parent_id' not in product.keys():
        product['parent_id'] = None

    data['products'].append(product)
    return product
