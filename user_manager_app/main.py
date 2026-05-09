import tkinter as tk
from database import create_table
from ui import App

def main():
    # krijo databazen nese nuk ekziston
    create_table()

    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()