from flask import Flask, request

from utility.Response import Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from  API.ProductRoute import ProductRoute
from  utility.Product import Product

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://satejall:satej@localhost:5432/Flask_rest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# db configuration to flask app
db = SQLAlchemy(app)


# Schema Marshmallow
ma = Marshmallow(app)


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


product_schma = ProductSchema(strict=True)
products_schma = ProductSchema(many=True, strict=True)


# route
@app.route('/', methods=['get'])
def hello_world():
    a = {"name": "satej"}
    buildResponse = Response(a)
    return buildResponse.getResponse()


# add product

@app.route('/product', methods=['post'])
def add_product():
    print(request.json)
    name = request.json['name']
    price = request.json['price']
    description = request.json['description']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)
    db.session.add(new_product)
    db.session.commit()
    return product_schma.jsonify(new_product)


# get all the product
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = Response(products_schma.dump(all_products).data)
    return result.getResponse()


# get single product

@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)

    return product_schma.jsonify(product)


# delete product

@app.route('/product/<id>', methods=['DELETE'])
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schma.jsonify(product)


# update single  product

@app.route("/product/<id>", methods=['PUT'])
def update_product(id):
    print(request.json)
    product = Product.query.get(id)

    name = request.json['name']
    price = request.json['price']
    description = request.json['description']
    qty = request.json['qty']
    product.name = name
    product.qty = qty
    product.description = description
    product.price = price
    db.session.commit()
    return product_schma.jsonify(product)

app.add_url_rule('/allproduct/',view_func=ProductRoute.as_view(''))
if __name__ == '__main__':
    app.run()
