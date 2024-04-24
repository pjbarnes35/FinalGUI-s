import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Rockyard Inventory Management System")

        self.intake_button = ttk.Button(root, text="Open Intake Form", command=self.open_intake_form)
        self.intake_button.grid(row=0, column=0, padx=10, pady=5)

        self.outgoing_button = ttk.Button(root, text="Open Outgoing Orders", command=self.open_outgoing_form)
        self.outgoing_button.grid(row=1, column=0, padx=10, pady=5)

    def open_intake_form(self):
        intake_window = tk.Toplevel(self.root)
        intake_window.title("Intake Form")

        # Intake form implementation...

    def open_outgoing_form(self):
        outgoing_window = tk.Toplevel(self.root)
        outgoing_window.title("Outgoing Orders")

        ttk.Label(outgoing_window, text="Type of Rock:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.rock_type_var = tk.StringVar()
        rock_types = ["Sandstone", "Boulder", "Millstone", "Granite", "Sprawls"]
        self.rock_type_combobox = ttk.Combobox(outgoing_window, textvariable=self.rock_type_var, values=rock_types, state="readonly")
        self.rock_type_combobox.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(outgoing_window, text="Date Sold:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.date_sold_entry = ttk.Entry(outgoing_window)
        self.date_sold_entry.grid(row=1, column=1, padx=10, pady=5)
        self.date_sold_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Default to today's date

        ttk.Label(outgoing_window, text="Price:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.price_entry = ttk.Entry(outgoing_window)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(outgoing_window, text="Destination:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.destination_entry = ttk.Entry(outgoing_window)
        self.destination_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(outgoing_window, text="Quantity:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.quantity_entry = ttk.Entry(outgoing_window)
        self.quantity_entry.grid(row=4, column=1, padx=10, pady=5)

        ttk.Button(outgoing_window, text="Submit", command=self.submit_outgoing_form).grid(row=5, column=1, padx=10, pady=5)

    def submit_outgoing_form(self):
        rock_type = self.rock_type_var.get()
        date_sold = self.date_sold_entry.get()
        price = self.price_entry.get()
        destination = self.destination_entry.get()
        quantity = self.quantity_entry.get()
        # Validate and process the outgoing order data


def main():
    root = tk.Tk()
    app = InventoryManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
