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
        self.count = 0

        def counter_module():
            group_box = QtWidgets.QGroupBox("Counter")
            number = QtWidgets.QLCDNumber(3, self)
            number.display(self.count)
            button1 = QtWidgets.QPushButton("Increase by 1")
            button1.clicked.connect(self.counter_up)
            button2 = QtWidgets.QPushButton("Decrease by 1")
            button2.clicked.connect(self.counter_down)
            sublayout1 = QtWidgets.QVBoxLayout()
            sublayout1.addWidget(button1)
            sublayout1.addWidget(button2)
            sublayout2 = QtWidgets.QVBoxLayout()
            sublayout2.addWidget(number)
            layout = QtWidgets.QHBoxLayout()
            layout.addLayout(sublayout1, 1)
            layout.addLayout(sublayout2, 2)
            layout.addStretch(1)
            group_box.setLayout(layout)
            return group_box, number

        # Highest level layout object
        layout = QtWidgets.QVBoxLayout()

        # Sections of application
        self.counting_module, self.count_LCD = counter_module()


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
            file_toolbar.setIconSize(QtCore.QSize(14, 14))
            self.addToolBar(file_toolbar)
            file_menu = self.menuBar().addMenu("&File")

            open_file_action = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'question.png')), "Settings", self)

            open_file_action.setStatusTip("Settings")
            open_file_action.triggered.connect(self.file_open)
            file_menu.addAction(open_file_action)
            file_toolbar.addAction(open_file_action)

        create_file_toolbar()

    def counter_up(self):
        self.count += 1
        self.count_LCD.display(self.count)

    def counter_down(self):
        self.count -= 1
        self.count_LCD.display(self.count)


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
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Counter")
    app_icon = QtGui.QIcon()
    # app_icon.addFile('arrow-continue.png')
    app.setWindowIcon(app_icon)
    window = MainWindow()
    app.exec_()
