import tkinter as tk
from tkinter import ttk

class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Rockyard Inventory Management System")
        
        # Sign-In Page
        self.username_label = ttk.Label(root, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = ttk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.password_label = ttk.Label(root, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = ttk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.signin_button = ttk.Button(root, text="Sign In", command=self.sign_in)
        self.signin_button.grid(row=2, column=1, padx=10, pady=5)

        # Sign-Up Page
        self.signup_button = ttk.Button(root, text="Sign Up", command=self.open_signup_window)
        self.signup_button.grid(row=3, column=1, padx=10, pady=5)

        # Initialize other components...
        self.users = {}  # Dictionary to hold user accounts

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Validate username and password, and proceed to the main system if valid

    def open_signup_window(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign Up")

        # Sign-Up Form
        ttk.Label(signup_window, text="Create an Account").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        
        ttk.Label(signup_window, text="Username:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.signup_username_entry = ttk.Entry(signup_window)
        self.signup_username_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(signup_window, text="Password:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.signup_password_entry = ttk.Entry(signup_window, show="*")
        self.signup_password_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(signup_window, text="Create Account", command=self.create_account).grid(row=3, column=1, padx=10, pady=5)

    def create_account(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        # Add the new user to the dictionary of users
        self.users[username] = password
        # Optionally, you can save the user data to a file or database for persistence


def main():
    root = tk.Tk()
    app = InventoryManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
