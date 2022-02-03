from graphene import ObjectType, String, Int, Field, List, Schema, Float, Mutation, InputObjectType, Boolean
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


class ProductInput(InputObjectType):
    name = String(required=True)
    price = Float(required=True)
    stock = Int(required=True)
    parent_id = Int()


class Brand(ObjectType):
    id = Int()
    name = String()
    description = String()
    hq = String()
    products = List(Product)

    def resolve_products(parent, info):
        return data.get_products_by_brand(parent['id'])


class AddBrand(Mutation):
    class Arguments:
        name = String(required=True)
        products = List(ProductInput)

    ok = Boolean()
    brand = Field(Brand)

    def mutate(root, info, name, **kwargs):
        try:
            new_brand = data.add_brand(name)
            products = kwargs.get('products')

            if products is not None:
                for product in products:
                    product['brand_id'] = new_brand['id']
                    data.add_product(product)
            return AddBrand(brand=new_brand, ok=True)
        except:
            return AddBrand(ok=False)


class Mutations(ObjectType):
    add_brand = AddBrand.Field()


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


schema = Schema(query=Query, mutation=Mutations)
