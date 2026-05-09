
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
         # Password
        tk.Label(frame, text="Password").pack(anchor="w")
        self.password_entry = tk.Entry(frame, width=30, show="*")
        self.password_entry.pack(pady=5)

        # Show password checkbox
        self.show_pass = tk.BooleanVar()
        tk.Checkbutton(frame, text="Show Password",
                       variable=self.show_pass,
                       command=self.toggle_password).pack(anchor="w")

        # Buttons frame
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)

        self.register_btn = tk.Button(btn_frame, text="Register", width=10, command=self.register)
        self.register_btn.grid(row=0, column=0, padx=5)

        self.login_btn = tk.Button(btn_frame, text="Login", width=10, command=self.login)
        self.login_btn.grid(row=0, column=1, padx=5)

        self.show_btn = tk.Button(frame, text="Show Users", command=self.show_users)
        self.show_btn.pack(pady=5)

        # Status label (poshtë)
        self.status = tk.Label(frame, text="", fg="green")
        self.status.pack(pady=5)

    def toggle_password(self):
        if self.show_pass.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def set_loading(self, state=True):
        # disable/enable buttons
        state_val = "disabled" if state else "normal"
        self.register_btn.config(state=state_val)
        self.login_btn.config(state=state_val)
        self.show_btn.config(state=state_val)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Plotëso të gjitha fushat")
            return

        self.set_loading(True)
        self.status.config(text="Duke krijuar user...")

        self.root.after(300, lambda: self._do_register(username, password))

    def _do_register(self, username, password):
        salt = generate_salt()
        password_hash = hash_password(password, salt)

        if insert_user(username, password_hash, salt):
            self.status.config(text="User u krijua me sukses", fg="green")
            messagebox.showinfo("Success", "User u krijua")
        else:
            self.status.config(text="Username ekziston", fg="red")
            messagebox.showerror("Error", "Username ekziston")

        self.set_loading(False)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.set_loading(True)
        self.status.config(text="Duke u loguar...")

        self.root.after(300, lambda: self._do_login(username, password))