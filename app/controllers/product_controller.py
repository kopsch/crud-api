from http import HTTPStatus
from flask import request, jsonify, send_file
from app.models.product_model import Product, fs
from io import BytesIO


def serve_pil_image(pil_img):

    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


def retrieve() -> tuple:
    product_list = list(Product.get_all())
    Product.serialize(product_list)
    return jsonify(product_list), HTTPStatus.OK


def create() -> tuple:
    if "image" in request.files:
        image = request.files["image"]
        fs.put(image, filename=image.filename)
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

    if "image" in request.files:
        image = request.files["image"]
        fs.put(image, filename=image.filename)
        data = {
            "name": request.form.get("name"),
            'price': request.form.get("price"),
            'image': image.filename
        }

        product = Product.update_product(id, data)
        Product.serialize(product)

        return jsonify(product), HTTPStatus.CREATED
    else:
        data = {
            "name": request.form.get("name"),
            'price': request.form.get("price"),
        }

        product = Product.update_product(id, data)
        Product.serialize(product)

        return jsonify(product), HTTPStatus.CREATED
