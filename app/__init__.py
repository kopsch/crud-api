from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from app.controllers import product_controller
import os
from dotenv import load_dotenv

load_dotenv()
password = os.environ.get('password')

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = f'mongodb+srv://thaeki:{password}@crud-southamerica-east.9ngcb.mongodb.net/' \
'myFirstDatabase?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.get("/")
def home():
    return ""

@app.get("/products")
def retrieve():
    return product_controller.retrieve()
        
@app.post("/products")
def product():
    return product_controller.create()

@app.delete("/products/<id>")
def delete(id):
    return product_controller.delete_product(id)

@app.patch("/products/<id>")
def update(id):
    return product_controller.update_product(id)


@app.post("/image")
def upload_image():
    if "image" in request.files:
        image = request.files["image"]
        mongo.save_file(image.filename, image)
        return {"message": "saved"}, 201
        
@app.get("/files/<filename>")
def retrieve_image(filename):
    return mongo.send_file(filename)
