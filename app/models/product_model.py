import os
from dotenv import load_dotenv
import pymongo
from datetime import datetime
from bson import ObjectId

load_dotenv()
password = os.environ.get('password')
DATABASE_URL = f'mongodb+srv://thaeki:{password}@crud-southamerica-east.9ngcb.mongodb.net/' \
    'myFirstDatabase?retryWrites=true&w=majority'

client = pymongo.MongoClient(DATABASE_URL)
db = client.db

class Product:
    def __init__(self, *args, **kwargs) -> None:
        date = datetime.now()
        self.image = kwargs.get('image')
        self.name = kwargs.get('name')
        self.price = kwargs.get('price')
        self.created_at = date.strftime('%d/%m/%Y %H:%M')
        
    @staticmethod
    def get_all():
        product_list = db.products.find()
        return product_list
        
    def create(self) -> None:
        db.products.insert_one(self.__dict__)
        
    @staticmethod
    def serialize(data) -> None:
        if type(data) is list:
            for product in data:
                product.update({"_id": str(product["_id"])})
        elif type(data) is Product:
            data._id = str(data._id)
        elif type(data) is dict:
            data.update({"_id": str(data["_id"])})
            
    @staticmethod
    def delete_post(id):
        post = db.products.find_one_and_delete({"_id": ObjectId(id)})
        return post
    
    @staticmethod
    def update_post(id, data):
        date = datetime.now()
        
        db.posts.find_one_and_update({"_id": ObjectId(id)}, {"$set": data})
        db.posts.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"updated_at": date.strftime('%d/%m/%Y %H:%M')}})
        post = db.posts.find_one({"_id": ObjectId(id)})
        return post