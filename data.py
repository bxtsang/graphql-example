data = {
    "brands": [
        {
            "id": 1,
            "name": "Apple",
            "description": "I keep the doctor away if you eat one of me a day",
            "hq": "California"
        },
        {
            "id": 2,
            "name": "Huawei",
            "description": "Chinese company that makes good mobile phones without Android",
            "hq": "Shenzhen"
        },
        {
            "id": 3,
            "name": "Dell",
            "description": "Company that makes decent laptops",
            "hq": "Texas"
        }
    ],
    "products": [
        {
            "id": 1,
            "name": "Macbook Pro 16 inch",
            "price": 3000,
            "brand_id": 1,
            "stock": 12,
            "parent_id": None
        },
        {
            "id": 2,
            "name": "XPS 13",
            "price": 2800,
            "brand_id": 3,
            "stock": 4,
            "parent_id": None
        },
        {
            "id": 3,
            "name": "Matebook Pro",
            "price": 2300,
            "brand_id": 2,
            "stock": 25,
            "parent_id": None
        },
        {
            "id": 4,
            "name": "IPad Pro",
            "price": 1500,
            "brand_id": 1,
            "stock": 3,
            "parent_id": None
        },
        {
            "id": 5,
            "name": "Apple Pencil",
            "price": 200,
            "brand_id": 1,
            "stock": 8,
            "parent_id": 4
        },
        {
            "id": 6,
            "name": "IDock",
            "price": 100,
            "brand_id": 1,
            "stock": 80,
            "parent_id": 1
        },
        {
            "id": 7,
            "name": "The best IPad case",
            "price": 50,
            "brand_id": 1,
            "stock": 100,
            "parent_id": 4
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
