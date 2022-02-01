from http import HTTPStatus
from flask import request, jsonify
from app.models.product_model import Product

def retrieve() -> tuple:
    product_list = list(Product.get_all())
    Product.serialize(product_list)
    return jsonify(product_list), HTTPStatus.OK

def create() -> tuple:
    data = request.get_json()
    
    if not data.keys() >= {"name", "price"}:
        return {"message": "fields are missing"}, HTTPStatus.BAD_REQUEST
    
    product = Product(**data)
    product.create()
    Product.serialize(product)
    
    return jsonify(product.__dict__), HTTPStatus.CREATED

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
        