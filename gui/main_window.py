import tkinter as tk
from tkinter import ttk
import config

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        # Създаване на таблицата за директориите
        self.directory_table = ttk.Treeview(self, columns=("Path", "Days", "Start Time", "End Time", "Interval", "Actions"), show="headings")
        self.directory_table.heading("Path", text="Path")
        self.directory_table.heading("Days", text="Days")
        self.directory_table.heading("Start Time", text="Start Time")
        self.directory_table.heading("End Time", text="End Time")
        self.directory_table.heading("Interval", text="Interval")
        self.directory_table.heading("Actions", text="Actions")
        self.directory_table.pack()

        # Зареждане на директориите от config.json
        self.load_directories()

        # Създаване на бутони за стартиране и спиране (ще ги имплементираме по-късно)
        self.start_button = ttk.Button(self, text="Start")
        self.stop_button = ttk.Button(self, text="Stop")
        self.start_button.pack()
        self.stop_button.pack()
    
    def load_directories(self):
        directories = config.get_directories()["directories"]  # Достъпваме списъка с директории
        for i, directory in enumerate(directories):
            values = (
                directory["path"],
                ", ".join(directory["days"]),
                directory["start_time"],
                directory["end_time"],
                directory.get("interval", ""),
                "Edit Delete"  # Поставяме текста "Edit Delete" в колоната "Actions"
               
            )

            self.directory_table.insert("", "end", values=values, iid=i, tags=("odd",))

            edit_button = ttk.Button(self, text="Edit", command=lambda index=i: self.edit_directory(index))
            delete_button = ttk.Button(self, text="Delete", command=lambda index=i: self.delete_directory(index))

            self.directory_table.tag_configure("odd", background="white")
            self.directory_table.tag_configure("even", background="lightblue")
            

    def edit_directory(self, index):
        print('edit started')
        # ... (логика за редактиране на директория)
        pass

    def delete_directory(self, index):
        # ... (логика за изтриване на директория)
        pass