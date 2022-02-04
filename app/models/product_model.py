from datetime import datetime
from bson import ObjectId
from app.__init__ import mongo

class Product:
    def __init__(self, *args, **kwargs) -> None:
        date = datetime.now()
        self.image = kwargs.get('image')
        self.name = kwargs.get('name')
        self.price = float(kwargs.get('price'))
        self.created_at = date.strftime('%d/%m/%Y %H:%M')
        
    @staticmethod
    def get_all():
        product_list = mongo.db.products.find()
        return product_list
        
    def create(self) -> None:
        mongo.db.products.insert_one(self.__dict__)
        
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
    def delete_product(id):
        product = mongo.db.products.find_one_and_delete({"_id": ObjectId(id)})
        return product
    
    @staticmethod
    def update_product(id, data):
        date = datetime.now()
        
        mongo.db.products.find_one_and_update({"_id": ObjectId(id)}, {"$set": data})
        mongo.db.products.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"updated_at": date.strftime('%d/%m/%Y %H:%M')}})
        product = mongo.db.products.find_one({"_id": ObjectId(id)})
        return product