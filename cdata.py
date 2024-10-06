# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Signal
import json
import os
filename = "time_saved.json"


class cData(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # Загружаем данные из файла при инициализации
        if not self.existFile():
            self.createJsonfile()

    def existFile(self):
        # Проверяем, существует ли файл
        return os.path.exists(filename)

    def createJsonfile(self):
        # Создаем новый JSON файл, если его нет
        with open(filename, 'w') as file:
            json.dump([], file)  # Создаем пустой список и сохраняем его как JSON

    def loadDate_from_json_toWidget(self):
                # Загружаем данные из файла
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
                print(f"Loaded data from file: {data}")  # Отладочный вывод
            except json.JSONDecodeError:
                data = []
                print("Failed to decode JSON, initializing empty data.")  # Отладочный вывод
            return data

    def save_new_result(self, hours, minutes, seconds, milliseconds, description):
        # Сохраняем новый результат в файл
        new_entry = {
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "milliseconds": milliseconds,
            "information": description
        }

        # Если файл существует, загружаем его содержимое, добавляем новую запись и сохраняем обратно
        data = self.loadDate_from_json_toWidget()
        data.append(new_entry)

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
