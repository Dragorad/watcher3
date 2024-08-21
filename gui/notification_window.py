import tkinter as tk
from tkinter import ttk

class NotificationWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Notifications")

        # ... (създаване на графичния интерфейс с tkinter)