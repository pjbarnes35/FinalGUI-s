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

    def open_intake_form(self):
        intake_window = tk.Toplevel(self.root)
        intake_window.title("Intake Form")

        ttk.Label(intake_window, text="Type of Rock:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.rock_type_var = tk.StringVar()
        rock_types = ["Sandstone", "Boulder", "Millstone", "Granite", "Sprawls"]
        self.rock_type_combobox = ttk.Combobox(intake_window, textvariable=self.rock_type_var, values=rock_types, state="readonly")
        self.rock_type_combobox.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(intake_window, text="Date Received:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.date_received_entry = ttk.Entry(intake_window)
        self.date_received_entry.grid(row=1, column=1, padx=10, pady=5)
        self.date_received_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Default to today's date

        ttk.Label(intake_window, text="Received From:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.received_from_entry = ttk.Entry(intake_window)
        self.received_from_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(intake_window, text="Submit", command=self.submit_intake_form).grid(row=3, column=1, padx=10, pady=5)

    def submit_intake_form(self):
        rock_type = self.rock_type_var.get()
        date_received = self.date_received_entry.get()
        received_from = self.received_from_entry.get()
        # Validate and process the intake form data


def main():
    root = tk.Tk()
    app = InventoryManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
