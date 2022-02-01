from app.routes.home_route import home_route
from app.routes.product_route import product_route


def init_app(app) -> None:
    home_route(app)
    product_route(app)