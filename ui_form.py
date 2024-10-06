# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(547, 349)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 531, 331))
        self.tabWidget.setStyleSheet(u"QTabWidget:pane\n"
"{\n"
"	border: 6px;\n"
"	background-color: rgb(220, 220, 220);\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 381, 31))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 210, 71, 31))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_2.setFont(font1)
        self.pushButton_save = QPushButton(self.tab)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(320, 240, 161, 31))
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 140, 391, 41))
        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(100, 70, 71, 41))
        font2 = QFont()
        font2.setPointSize(11)
        self.plainTextEdit.setFont(font2)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit_2 = QPlainTextEdit(self.tab)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(190, 70, 71, 41))
        self.plainTextEdit_2.setFont(font2)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_3 = QPlainTextEdit(self.tab)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(280, 70, 71, 41))
        self.plainTextEdit_3.setFont(font2)
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_6 = QPlainTextEdit(self.tab)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setGeometry(QRect(40, 240, 271, 31))
        self.plainTextEdit_6.setFont(font2)
        self.plainTextEdit_6.setReadOnly(False)
        self.plainTextEdit_4 = QPlainTextEdit(self.tab)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(370, 70, 71, 41))
        self.plainTextEdit_4.setFont(font2)
        self.plainTextEdit_4.setReadOnly(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableWidget1 = QTableWidget(self.tab_2)
        if (self.tableWidget1.columnCount() < 5):
            self.tableWidget1.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget1.setObjectName(u"tableWidget1")
        self.tableWidget1.setGeometry(QRect(10, 10, 511, 281))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Stopwatch", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u0427\u0430\u0441\u044b | \u043c\u0438\u043d\u0443\u0442\u044b | \u0441\u0435\u043a\u0443\u043d\u0434\u044b | \u043c\u0438\u043b\u0438\u0441\u0435\u043a\u0443\u043d\u0434\u044b", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_save.setText(QCoreApplication.translate("Widget", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c ->", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u0421\u0422\u0410\u0420\u0422", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"timer", None))
        ___qtablewidgetitem = self.tableWidget1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"\u0447\u0430\u0441\u044b", None));
        ___qtablewidgetitem1 = self.tableWidget1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"\u043c\u0438\u043d\u0443\u0442\u044b", None));
        ___qtablewidgetitem2 = self.tableWidget1.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"\u0441\u0435\u043a\u0443\u043d\u0434\u044b", None));
        ___qtablewidgetitem3 = self.tableWidget1.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"\u043c\u0438\u043b\u0438\u0441\u0435\u043a\u0443\u043d\u0434\u044b", None));
        ___qtablewidgetitem4 = self.tableWidget1.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"results", None))
    # retranslateUi

