from graphene import ObjectType, String, Int, Field, List, Schema, Float

class Brand(ObjectType):
    id = Int()
    name = String()
    products = List(Product)

class Product(ObjectType):
    id = Int()
    name = String()
    price = Float()