from app.controllers import product_controller

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