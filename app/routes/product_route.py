from app.controllers import product_controller
from app.models.product_model import fs
from PIL import Image

def product_route(app) -> None:
    
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
    
    @app.get("/files/<filename>")
    def retrieve_image(filename):
        im_stream = fs.get_last_version(filename)
        im = Image.open(im_stream)
        return product_controller.serve_pil_image(im)