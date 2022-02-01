import os
from dotenv import load_dotenv
import pymongo

load_dotenv()
password = os.environ.get('password')
DATABASE_URL = f'mongodb+srv://thaeki:{password}@crud-southamerica-east.9ngcb.mongodb.net/' \
    'myFirstDatabase?retryWrites=true&w=majority'

client = pymongo.MongoClient(DATABASE_URL)
db = client.db

class Product:
    def __init__(self, *args, **kwargs) -> None:
        self.image = kwargs.get('image')
        self.name = kwargs.get('name')
        self.price = kwargs.get('price')
        
    def create(self):
        db.products.insert_one(self.__dict__)