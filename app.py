from flask import Flask, request


app = Flask(__name__)

stores = [{"name": "walmart", "items": [{"name": "chair", "price": 14.99}]}]


@app.route("/store", methods=["GET", "POST"])
def list_stores():
    if request.method == "POST":
        data = request.get_json()
        name = data["name"]
        items = []
        new_store = {"name": name, "items": items}
        stores.append(new_store)
        return new_store, 201
    return {"stores": stores}


@app.route("/store/<string:store_name>/item", methods=["POST"])
def create_item(store_name):
    data = request.get_json()
    for store in stores:
        if store["name"] == store_name:
            new_item = {"name": data["name"], "price": data["price"]}
            store["items"].append(new_item)
        return new_item, 201

    return {"message": "store not found"}, 404
