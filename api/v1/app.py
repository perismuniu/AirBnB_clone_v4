#!/usr/bin/python3

# api/v1/app.py
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """Closes the storage on teardown."""
    storage.close()

if __name__ == "__main__":
    host = "0.0.0.0" if not os.getenv("HBNB_API_HOST") else os.getenv("HBNB_API_HOST")
    port = 5000 if not os.getenv("HBNB_API_PORT") else int(os.getenv("HBNB_API_PORT"))
    app.run(host=host, port=port, threaded=True)
