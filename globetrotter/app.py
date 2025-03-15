from sanic import Sanic
from views import user_bp

app = Sanic("GlobetrotterApp")

app.blueprint(user_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
