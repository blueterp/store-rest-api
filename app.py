from flask import Flask, request
from flask_smorest import abort
from db import stores, items
import uuid
import json

app = Flask(__name__)


@app.route("/store", methods=["GET", "POST"])
def list_stores():
    if request.method == "POST":
        data = request.get_json()
        store_id = uuid.uuid4().hex
        new_store = {**data, "id": store_id}
        stores[store_id] = new_store
        return new_store, 201
    return {"stores": stores}


@app.route("/item", methods=["POST"])
def create_item():
    if request.method == "POST":
        data = request.get_json()
        if data["store_id"] in stores:
            item_id = uuid.uuid4().hex
            new_item = {**data, "id": item_id}
            items[item_id] = new_item
            return new_item, 201
    abort(404, message="Item not found")


@app.get("/item")
def get_items():
    return {"items": items}


@app.get("/store/<string:store_id>")
def get_store_by_id(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Message store not found.")


@app.get("/item/<string:item_id>")
def get_item_by_id(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Message item not found.")
