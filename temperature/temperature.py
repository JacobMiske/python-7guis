# Jacob Miske MIT License
import os
import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtTest import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.output_temperature = 0

        def temperature_module():
            group_box = QtWidgets.QGroupBox("Temperature Converter")
            floating_entry = QtWidgets.QLineEdit()
            number = QtWidgets.QLCDNumber(3, self)
            number.display(self.output_temperature)
            button1 = QtWidgets.QPushButton("Convert F to C")
            button1.clicked.connect(self.convertFC)
            button2 = QtWidgets.QPushButton("Convert C to F")
            button2.clicked.connect(self.convertCF)
            sublayout1 = QtWidgets.QVBoxLayout()
            sublayout1.addWidget(floating_entry)
            sublayout1.addWidget(button1)
            sublayout1.addWidget(button2)
            sublayout2 = QtWidgets.QVBoxLayout()
            sublayout2.addWidget(number)
            layout = QtWidgets.QHBoxLayout()
            layout.addLayout(sublayout1, 1)
            layout.addLayout(sublayout2, 2)
            layout.addStretch(1)
            group_box.setLayout(layout)
            return group_box, floating_entry, number

        # Highest level layout object
        layout = QtWidgets.QVBoxLayout()

        # Sections of application
        self.counting_module, self.floating_entry, self.count_LCD = temperature_module()


        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

        # Add widgets
        layout.addWidget(self.counting_module)

        container = QtWidgets.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QtWidgets.QStatusBar()
        self.setStatusBar(self.status)

        self.update_title()
        self.resize(1140, 760)
        self.show()

        def create_file_toolbar():
            file_toolbar = QtWidgets.QToolBar("File")
            file_toolbar.setIconSize(QSize(14, 14))
            self.addToolBar(file_toolbar)
            file_menu = self.menuBar().addMenu("&File")

            open_file_action = QAction(QIcon(os.path.join('images', 'question.png')), "Settings", self)

            open_file_action.setStatusTip("Settings")
            open_file_action.triggered.connect(self.file_open)
            file_menu.addAction(open_file_action)
            file_toolbar.addAction(open_file_action)

        create_file_toolbar()

    def convertFC(self):
        entry = float(self.floating_entry.text())
        print("Entered: " + str(entry))
        C = (entry - 32.0)*(5/9)
        self.count_LCD.display(C)


    def convertCF(self):
        entry = float(self.floating_entry.text())
        print("Entered: " + str(entry))
        F = (entry*9)/5+32
        self.count_LCD.display(F)


    def dialog_critical(self, s):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QtWidgets.QMessageBox.Critical)
        dlg.show()

    def file_open(self):
        self.dialog_critical(s="See GitHub README")

    def update_title(self):
        self.setWindowTitle("Counter")

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Counter")
    app_icon = QtGui.QIcon()
    # app_icon.addFile('arrow-continue.png')
    app.setWindowIcon(app_icon)
    window = MainWindow()
    app.exec_()
