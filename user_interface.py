import tkinter as tk
import json
import os
from tkinter import ttk
from project import (
    add_flower, update_flower, 
    remove_flower, sell_flower, 
    load_json, save_json,
    FLOWER_FILE
    )

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Flower Inventory")
        self.root.geometry("800x500")

        title = tk.Label(self.root, text="Flower Inventory", font=("Arial", 18))
        title.pack(pady=10)

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=5)
        tk.Label(form_frame, text="Price").grid(row=0, column=2, padx=5)
        tk.Label(form_frame, text="Stock").grid(row=0, column=4, padx=5)

        self.entry_name = tk.Entry(form_frame)
        self.entry_price = tk.Entry(form_frame)
        self.entry_stock = tk.Entry(form_frame)

        self.entry_name.grid(row=0, column=1, padx=5)
        self.entry_price.grid(row=0, column=3, padx=5)
        self.entry_stock.grid(row=0, column=5, padx=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add", width=10, command=self.add_flower).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Edit", width=10, command=self.edit_flower).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Delete", width=10, command=self.delete_flower).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Sell", width=10, command=self.sell_flower).grid(row=0, column=3, padx=5)
        tk.Button(button_frame, text="Reset", width=10, command=self.reset_field).grid(row=0, column=4, padx=5)

        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="Search: ").grid(row=0, column =0, padx=5)

        self.entry_search = tk.Entry(search_frame, width=20)
        self.entry_search.grid(row=0, column=1, padx=5)

        tk.Button(search_frame, text="Search", width=10, command=self.search_flower).grid(row=0, column=2, padx=5)
        tk.Button(search_frame, text="Show all", width=10, command=self.load_table_data).grid(row=0, column=3, padx=5)

        self.table = ttk.Treeview(
            self.root, 
            columns=("name", "price", "stock"), 
            show="headings", 
            height=10)
        self.table.pack(padx=10, pady=10, fill='both', expand=True)

        self.table.heading("name", text="Name")
        self.table.heading('price', text="Price")
        self.table.heading('stock', text="Stock")

        self.table.column('name', anchor="center", width=150)
        self.table.column('price', anchor="center", width=100)
        self.table.column('stock', anchor="center", width=100)
        self.table.bind("<<TreeviewSelect>>", self.on_row_select)

        self.load_table_data()
        self.root.mainloop()

    def load_table_data(self):
        data = load_json(FLOWER_FILE)
        self.table.delete(*self.table.get_children())

        for name, info in data.items():
            self.table.insert("", "end", values=(
                name.capitalize(),
                info["price"],
                info["stock"]
            ))

    def on_row_select(self, event):
        selected = self.table.selection()
        if not selected:
            return
        
        item = self.table.item(selected[0])
        name, price, stock = item["values"]

        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)

        self.entry_name.insert(0, name)
        self.entry_price.insert(0, price)
        self.entry_stock.insert(0, stock)

    def add_flower(self):
        name = self.entry_name.get().lower()
        price = self.entry_price.get()
        stock = self.entry_stock.get()

        if not name or not price or not stock:
            print("All fields are required.")
            return
        
        data = load_json(FLOWER_FILE)
        if name in data:
            print(f"{name.capitalize()} already exists.")
            return 
        
        msg = add_flower(name, price, stock)
        print(msg)
        self.load_table_data()


    def edit_flower(self):
        name = self.entry_name.get().lower()
        price = self.entry_price.get()
        stock = self.entry_stock.get()

        msg = update_flower(name, price if price else "-", stock if stock else "-")
        print(msg)
        self.load_table_data()

    def delete_flower(self):
        name = self.entry_name.get().lower()
        msg = remove_flower(name)
        print(msg)
        self.load_table_data()

    def sell_flower(self):
        name = self.entry_name.get().lower()
        qty = self.entry_stock.get()

        if not qty.isdigit():
            print("Invalid sell quantity.")
            return
        
        msg = sell_flower(name, int(qty))
        print(msg)
        self.load_table_data()

    def reset_field(self):
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)

    def search_flower(self):
        keyword = self.entry_search.get().lower()

        if not keyword:
            print("Enter a name to search.")
            return
        
        data =load_json(FLOWER_FILE)
        result = {k: v for k, v in data.items() if keyword in k}

        self.table.delete(*self.table.get_children())

        if not result:
            print("No matching flowers")
            return
        
        for name, info in result.items():
            self.table.insert("", "end", values=(
                name.capitalize(),
                info["price"],
                info["stock"]
            ))
  

if __name__ == "__main__":
    UserInterface()