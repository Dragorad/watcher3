import json
import logging

# Конфигуриране на logging
logging.basicConfig(filename='monitor.log', level=logging.INFO, format='%(asctime)s - %(message)s')

config_file = 'config.json'  # Задаваме пътя към конфигурационния файл

def load_config():
    try:
        with open(config_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"directories": []}

def save_config(config_data):
    with open(config_file, "w") as f:
        json.dump(config_data, f, indent=4)


def get_directories():
        return load_config()

def add_directory(directory):
    config_data = load_config()
    config_data["directories"].append(directory)
    save_config(config_data)

def update_directory(index, directory):
    config_data = load_config()
    if 0 <= index < len(config_data["directories"]):  # Проверка дали индексът е валиден
        config_data["directories"][index] = directory
        save_config(config_data)
    else:
        logging.error(f"Невалиден индекс при опит за актуализация на директория: {index}")

def delete_directory(index):
    config_data = load_config()
    if 0 <= index < len(config_data["directories"]):  # Проверка дали индексът е валиден
        del config_data["directories"][index]
        save_config(config_data)
    else:
        logging.error(f"Невалиден индекс при опит за изтриване на директория: {index}")

def log_directory_check(directory_path):
    logging.info(f"Проверка на директория: {directory_path}")