# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget
import os
from ui_form import Ui_Widget

Worked_check = False  # для проверки работы таймера

class cTimer(QtCore.QObject):  # Наследуемся от QObject для работы с сигналами и потоками
    update_time_signal = QtCore.Signal(int, int, int, int)  # Сигнал для передачи времени в главный поток (часы, минуты, секунды, миллисекунды)

    def __init__(self):
        super().__init__()
        self.running = False  # Флаг для управления таймером
        self.timer_thread = QtCore.QThread()  # Отдельный поток для таймера
        self.moveToThread(self.timer_thread)  # Перемещаем объект таймера в поток
        self.timer_thread.started.connect(self.run)  # Подключаем запуск таймера при старте потока

    def checkWork(self):
        return Worked_check

    def onTimer(self, bo):
        global Worked_check
        Worked_check = bo
        if bo:
            self.start_timer()  # Запускаем таймер
        else:
            self.stop_timer()  # Останавливаем таймер

    def start_timer(self):
        if not self.running:
            self.running = True
            self.timer_thread.start()  # Запускаем поток таймера

    def stop_timer(self):
        self.running = False  # Останавливаем таймер
        self.timer_thread.quit()  # Останавливаем поток

    def run(self):
        hours, minutes, seconds, milliseconds = 0, 0, 0, 0
        while self.running:
            QtCore.QThread.msleep(3)  # задерка
            milliseconds += 10
            if milliseconds == 1000:
                milliseconds = 0
                seconds += 1
            if seconds == 60:
                seconds = 0
                minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
            # Отправляем сигнал с обновленным временем
            self.update_time_signal.emit(hours, minutes, seconds, milliseconds)
