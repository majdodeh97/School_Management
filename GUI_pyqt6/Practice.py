import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a menu bar
        menubar = self.menuBar()

        # Create a File menu
        file_menu = menubar.addMenu('File')

        # Create an Open action
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.openFile)

        # Add the Open action to the File menu
        file_menu.addAction(open_action)

        self.setWindowTitle('File Explorer Example')
        self.setGeometry(300, 300, 400, 300)

    def openFile(self):
        file_dialog = QFileDialog()
        file_dialog.exec()
        # You can access the selected file using file_dialog.selectedFiles()
        # For example:
        # selected_files = file_dialog.selectedFiles()
        # if selected_files:
        #     print(selected_files[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())