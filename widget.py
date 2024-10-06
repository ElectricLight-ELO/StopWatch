# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import ctimer
import cdata

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.timer = ctimer.cTimer()
        self.timer.update_time_signal.connect(self.update_time)

        self.ui.pushButton_2.clicked.connect(self.button2clicked)
        self.ui.pushButton_save.clicked.connect(self.saveButton)

        self.cdata = cdata.cData()

        data = self.cdata.loadDate_from_json_toWidget()  # Загружаем данные из JSON
        self.load_data_to_table(data)

    def button2clicked(self):
        if not self.timer.checkWork():
            self.ui.pushButton_2.setText("СТОП")
            self.timer.onTimer(True)
        else:
            self.ui.pushButton_2.setText("СТАРТ")
            self.timer.onTimer(False)

    def saveButton(self):
        # Извлекаем значения из полей ввода
        hours = self.ui.plainTextEdit.toPlainText()
        minutes = self.ui.plainTextEdit_2.toPlainText()
        seconds = self.ui.plainTextEdit_3.toPlainText()
        milliseconds = self.ui.plainTextEdit_4.toPlainText()
        description = self.ui.plainTextEdit_6.toPlainText()

        # Добавляем новую строку в таблицу
        row_position = self.ui.tableWidget1.rowCount()
        self.ui.tableWidget1.insertRow(row_position)

        self.ui.tableWidget1.setItem(row_position, 0, QTableWidgetItem(hours))
        self.ui.tableWidget1.setItem(row_position, 1, QTableWidgetItem(minutes))
        self.ui.tableWidget1.setItem(row_position, 2, QTableWidgetItem(seconds))
        self.ui.tableWidget1.setItem(row_position, 3, QTableWidgetItem(milliseconds))
        self.ui.tableWidget1.setItem(row_position, 4, QTableWidgetItem(description))

        # Сохраняем данные в JSON файл
        self.cdata.save_new_result(hours, minutes, seconds, milliseconds, description)

    def load_data_to_table(self, data):
        print(f"Loading data to table: {data}")
        for entry in data:
            row_position = self.ui.tableWidget1.rowCount()
            self.ui.tableWidget1.insertRow(row_position)

            self.ui.tableWidget1.setItem(row_position, 0, QTableWidgetItem(str(entry["hours"])))
            self.ui.tableWidget1.setItem(row_position, 1, QTableWidgetItem(str(entry["minutes"])))
            self.ui.tableWidget1.setItem(row_position, 2, QTableWidgetItem(str(entry["seconds"])))
            self.ui.tableWidget1.setItem(row_position, 3, QTableWidgetItem(str(entry["milliseconds"])))
            self.ui.tableWidget1.setItem(row_position, 4, QTableWidgetItem(entry["information"]))

    def update_time(self, hours, minutes, seconds, milliseconds):
        # Обновляем текст
        self.ui.plainTextEdit.setPlainText(str(hours))
        self.ui.plainTextEdit_2.setPlainText(str(minutes))
        self.ui.plainTextEdit_3.setPlainText(str(seconds))
        self.ui.plainTextEdit_4.setPlainText(str(milliseconds))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
