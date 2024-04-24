import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Rockyard Inventory Management System")

        self.intake_button = ttk.Button(root, text="Open Intake Form", command=self.open_intake_form)
        self.intake_button.grid(row=0, column=0, padx=10, pady=5)

        self.graph_button = ttk.Button(root, text="View Inventory Graph", command=self.open_graph_window)
        self.graph_button.grid(row=1, column=0, padx=10, pady=5)

    def open_intake_form(self):
        # Implementation of intake form...
        pass

    def open_graph_window(self):
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Inventory Graph")

        # Sample data for plotting
        rock_types = ["Sandstone", "Boulder", "Millstone", "Granite", "Sprawls"]
        quantities = [10, 20, 15, 30, 25]

        # Create a figure and plot the data
        fig, ax = plt.subplots()
        ax.bar(rock_types, quantities)
        ax.set_ylabel('Quantity')
        ax.set_xlabel('Rock Type')
        ax.set_title('Inventory Overview')

        # Embed the plot into a Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

def main():
    root = tk.Tk()
    app = InventoryManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
