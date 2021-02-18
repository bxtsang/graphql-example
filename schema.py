from graphene import ObjectType, String, Int, Field, List, Schema, Float
import data

class Product(ObjectType):
    id = Int()
    name = String()
    price = Float()
    brand = Field(lambda: Brand)
    stock = Int()
    parent = Field(lambda: Product)

    def resolve_brand(parent, info):
        return data.get_brand_by_id(parent['brand_id'])

    def resolve_parent(parent, info):
        return data.get_product_by_id(parent['parent_id'])

class Brand(ObjectType):
    id = Int()
    name = String()
    products = List(Product)

    def resolve_products(parent, info):
        return data.get_products_by_brand(parent['id'])

class Query(ObjectType):
    brands = List(Brand, name=String())
    brand = Field(Brand, id=Int(required=True))
    products = List(Product, name=String())
    product = Field(Product, id=Int(required=True))

    def resolve_brands(root, info, **kwargs):
        name = kwargs.get('name')

        if name is None:
            return data.get_all_brands()
        return data.get_brands_by_name(name)

    def resolve_brand(root, info, id):
        return data.get_brand_by_id(id)

    def resolve_products(root, info, **kwargs):
        name = kwargs.get('name')

        if name is None:
            return data.get_all_products()
        return data.get_products_by_name(name)

    def resolve_product(root, info, id):
        return data.get_product_by_id(id)

schema = Schema(query = Query)
