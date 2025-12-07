# __FLOWER SHOP__

#### Video Demo: https://youtu.be/yHstsR73Qh0

## Description
This project is a flower shop inventory system build in Python. It allows users to manage flower stock, update prices, sell flowers, search for specific items, and view all stored data.

Project Structure:
- final_project.py
- flowers.json
- README.md

## Run Project
cd flower_inventory_system
python project.py

## Functionality
This projects has 6 main functions:
### add_flower(name, price, stock)
This function takes 3 arguments: flower, price, and stock, it will add new flower to the inventory after ensuring the flower does not exists.
### sell_flower(name, quantity)
This function takes 2 arguments, it reduces the stock of the specified flower. The function checks whether the flower exists and ensures the quantity sold does not exceed available stock.
### update_flower(name, price, stock)
This function takes 3 arguments, it updates price and stock of existing flower according to user's input.
### remove_flower(name)
This function takes 1 argument, it will remove existing flower according to user's input.
### search_flower(name)
This functions takes 1 argument, it searches for existing flower and displays the result with details of name, price, and stock
### load_data():
This function takes no argument, it displays all saved flowers with details of price and stock to the user.

Other helper functions:
### load_json(filename):
This function takes 1 argument, it loads data from a JSON file. If the file does not exist, it creates an empty JSON structure and returns it.
### save_json(filename, data):
This function takes 2 argument, it saves the given dictionary into the specified JSON file.
### print_menu():
This function takes 0 argument, it prints out choices of actions that can be taken.

### Author: Charlene
