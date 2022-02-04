from http import HTTPStatus
from flask import request, jsonify
from app.models.product_model import Product
from app.__init__ import mongo

def retrieve() -> tuple:
    product_list = list(Product.get_all())
    Product.serialize(product_list)
    return jsonify(product_list), HTTPStatus.OK

def create() -> tuple:
    if "image" in request.files:
        image = request.files["image"]
        mongo.save_file(image.filename, image)
        data = {
            "name": request.form.get("name"),
            'price': request.form.get("price"),
            'image': image.filename
        }
        
        product = Product(**data)
        product.create()
        Product.serialize(product)

        return jsonify(product.__dict__), HTTPStatus.CREATED
    return {"message": "no image found"}, HTTPStatus.BAD_REQUEST

def delete_product(id) -> tuple:
    product = Product.delete_product(id)
    Product.serialize(product)
    return jsonify(product), HTTPStatus.OK

def update_product(id) -> tuple:
    try:
        data = request.get_json()
        
        product = Product.update_product(id, data)
        Product.serialize(product)
        return jsonify(product), HTTPStatus.OK
    except:
        return {"message": "the fields are invalid"}, HTTPStatus.BAD_REQUEST
        