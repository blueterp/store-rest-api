from flask import Flask


app = Flask(__name__)

stores = [{"name": "Walmart", "items": [{"name": "chair", "price": 14.99}]}]


@app.route("/stores", methods=["GET"])
def list_stores():
    return {"stores": stores}
