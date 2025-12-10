import os
import sys
import json

FLOWER_FILE = "flowers.json"

def load_json(filename):
    if not os.path.exists(filename):
        save_json(filename, {})
        return {}
    with open(filename, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            save_json(filename, {})
            return {}

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def add_flower(name, price, stock):
    data = load_json(FLOWER_FILE)

    new_name = name.lower()
    new_price = int(price)
    new_stock = int(stock)
    data[new_name] = {
        "price": new_price,
        "stock": new_stock
    }

    save_json(FLOWER_FILE, data)
    return f"Added {name}."

def update_flower(name, price, stock):
    data = load_json(FLOWER_FILE)

    if name not in data:
        return "Flower not found."

    old_price = data[name]['price']
    old_stock = data[name]['stock']

    if price != "-":
        try:
            price = int(price)
            data[name]['price'] = price
        except ValueError:
            return "Invalid price."

    if stock != "-":
        try:
            stock = int(stock)
            data[name]["stock"] = stock
        except ValueError:
            return "Invalid stock."

    save_json(FLOWER_FILE, data)
    return (
        f"Flower {name.capitalize()} updated. \n"
        f"Price: {old_price} -> {data[name]['price']}\n"
        f"Stock: {old_stock} -> {data[name]['stock']}"
    )

def remove_flower(name):
    data = load_json(FLOWER_FILE)
    if name not in data:
        return "Flower not found"
    del data[name]
    save_json(FLOWER_FILE, data)
    return f"{name} removed."

def sell_flower(name, quantity):
    data = load_json(FLOWER_FILE)

    if name not in data:
        return "Flower not found"

    if data[name]["stock"] < quantity:
        return "Not enough stock."

    data[name]["stock"] -= quantity

    save_json(FLOWER_FILE, data)
    return (f"Remaining stock: {data[name]['stock']}")

def search_flower(keyword):
    data = load_json(FLOWER_FILE)
    results = {k: v for k, v in data.items() if keyword.lower() in k.lower()}

    if not results:
        return "No flower found."

    output = ""
    for name, info in results.items():
        output += f"{name.capitalize():15} | Price: {info['price']:5}| Stock: {info['stock']:5}"

    return output.strip()
def load_data():
    if not os.path.exists(FLOWER_FILE):
        return "No data found"

    data = load_json(FLOWER_FILE)
    if not data:
        return "No flowers in database."

    output = "\n=== Flower List ===\n"
    for name, info in data.items():
        output += f"{name.capitalize():15} | Price: {info['price']:5} | Stock : {info['stock']:5}\n"
    return output

