from flask.views import MethodView
from utility.ProductSchema import  ProductSchema
from utility.Response import Response
from  utility.Product import Product
product_schma = ProductSchema(strict=True)
products_schma = ProductSchema(many=True, strict=True)

class ProductRoute(MethodView):
    def get(self):

        all_products = Product.query.all()
        result = Response(products_schma.dump(all_products).data)
        print(result)
        return result.getResponse()
