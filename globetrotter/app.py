from sanic import Sanic, response
from views import user_bp, game_bp

app = Sanic("GlobetrotterApp")

# Register blueprints
app.blueprint(user_bp)
app.blueprint(game_bp)

# CORS Middleware
@app.middleware("response")
async def add_cors_headers(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
