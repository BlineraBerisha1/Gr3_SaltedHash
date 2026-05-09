
import tkinter as tk
from tkinter import messagebox
from database import insert_user, get_user, get_all_users
from security import generate_salt, hash_password

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("User Manager")
        self.root.geometry("350x300")
        self.root.resizable(False, False)

        # Frame kryesor (center)
        frame = tk.Frame(root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="User Manager", font=("Arial", 16, "bold")).pack(pady=10)

        # Username
        tk.Label(frame, text="Username").pack(anchor="w")
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.pack(pady=5)