from flask import Flask
from app.routes import app as ziggy_routes

app = Flask(__name__)
app.register_blueprint(ziggy_routes)

if __name__ == '__main__':
    app.run(debug=True)
