import tkinter as tk
from tkinter import ttk
import pandas as pd

class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Rockyard Inventory Management System")

        self.intake_button = ttk.Button(root, text="Open Intake Form", command=self.open_intake_form)
        self.intake_button.grid(row=0, column=0, padx=10, pady=5)

        self.graph_button = ttk.Button(root, text="View Inventory Data", command=self.open_data_window)
        self.graph_button.grid(row=1, column=0, padx=10, pady=5)

    def open_intake_form(self):
        # Implementation of intake form...
        pass

    def open_data_window(self):
        data_window = tk.Toplevel(self.root)
        data_window.title("Inventory Data")

        # Sample data for demonstration
        data = {
            'Type of Rock': ["Sandstone", "Boulder", "Millstone", "Granite", "Sprawls"],
            'Quantity': [10, 20, 15, 30, 25],
            'Price': [100, 200, 150, 300, 250],
            'Date Received': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01'],
            'Received From': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D', 'Supplier E']
        }

        # Create a DataFrame
        df = pd.DataFrame(data)

        # Create a treeview widget to display the data
        tree = ttk.Treeview(data_window, columns=list(df.columns), show="headings")

        # Set column headings
        for col in df.columns:
            tree.heading(col, text=col)

        # Insert data into the treeview
        for i, row in df.iterrows():
            tree.insert("", "end", values=list(row))

        tree.pack(expand=True, fill="both")

def main():
    root = tk.Tk()
    app = InventoryManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
