def home_route(app) -> None:
    @app.get("/")
    def home():
        return ""