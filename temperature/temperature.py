# Jacob Miske MIT License
import os
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtTest import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Highest level layout object
        layout = QVBoxLayout()

        # Sections of application
        self.editor = QPlainTextEdit()

        # Setup the QTextEdit editor configuration
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

        # Add widgets
        layout.addWidget(self.editor)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.update_title()
        self.resize(1140, 760)
        self.show()

        def create_file_toolbar():
            file_toolbar = QToolBar("File")
            file_toolbar.setIconSize(QSize(14, 14))
            self.addToolBar(file_toolbar)
            file_menu = self.menuBar().addMenu("&File")

            open_file_action = QAction(QIcon(os.path.join('images', 'question.png')), "Settings", self)

            open_file_action.setStatusTip("Settings")
            open_file_action.triggered.connect(self.file_open)
            file_menu.addAction(open_file_action)
            file_toolbar.addAction(open_file_action)

            save_file_action = QAction(QIcon(os.path.join('images', 'disk.png')), "Save", self)
            save_file_action.setStatusTip("Save current page")
            save_file_action.triggered.connect(self.file_save)
            file_menu.addAction(save_file_action)
            file_toolbar.addAction(save_file_action)

            saveas_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save As...", self)
            saveas_file_action.setStatusTip("Save current page to specified file")
            saveas_file_action.triggered.connect(self.file_saveas)
            file_menu.addAction(saveas_file_action)
            file_toolbar.addAction(saveas_file_action)

        create_file_toolbar()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_open(self):
        self.dialog_critical(s="See README.txt in ")

    def file_save(self):
        if self.path is None:
            # If we do not have a path, we need to use Save As.
            return self.file_saveas()
        self._save_to_path(self.path)

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")
        if not path:
            # If dialog is cancelled, will return ''
            return

        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()

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
