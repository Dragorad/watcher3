import tkinter as tk
from gui.main_window import MainWindow
from gui.notification_window import NotificationWindow
import config

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Monitor")

    # Зареждане на конфигурацията
    config.load_config()

    main_window = MainWindow(root)
    notification_window = NotificationWindow(root)

    root.mainloop()