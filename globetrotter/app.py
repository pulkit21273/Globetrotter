from sanic import Sanic
from views import user_bp, game_bp

app = Sanic("GlobetrotterApp")

# Register each blueprint separately
app.blueprint(user_bp)
app.blueprint(game_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
