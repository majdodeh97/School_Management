from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QSpinBox, QLineEdit


class CustomSpinBox(QSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lineEdit()

    def lineEdit(self):
        print("here")
        line_edit = QLineEdit(self)
        line_edit.setReadOnly(True)  # Set line edit to read-only

        line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text
        font = QFont("AppleSystemUiFont", 18)  # Change the font

        line_edit.setFont(font)
        self.setLineEdit(line_edit)
        return line_edit

    def stepBy(self, steps):
        # Override the stepBy() method
        # to prevent automatic selection/highlighting of numbers
        super().stepBy(steps)
        current_text = self.lineEdit().text()
        self.lineEdit().setText(current_text)
