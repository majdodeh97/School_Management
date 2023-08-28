from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QMessageBox, QDialogButtonBox
from GUI_pyqt6.Qt_Designer_py_files.auto_edit_percentages import Ui_edit_percentages_dialog


class EditPercentages(QDialog):
    def __init__(self, parent, j_table, categories, subject):
        super().__init__(parent=parent)
        self.ui = Ui_edit_percentages_dialog()
        self.ui.setupUi(self)
        self.categories = categories
        self.subject = subject
        self.j_table = j_table
        self.line_edits = self.fill_form_layout()
        self.connect_signals_slots()
        self.move(575, 350)
        self.show()

    def connect_signals_slots(self):
        self.ui.edit_percentages_buttonBox.button(QDialogButtonBox.StandardButton.Ok).clicked\
            .connect(self.update_percentages_in_database)
        self.ui.edit_percentages_buttonBox.button(QDialogButtonBox.StandardButton.Cancel).clicked\
            .connect(self.reject)

    def fill_form_layout(self):
        form_layout = self.ui.edit_percentages_formLayout
        line_edits = []
        for category in self.categories:
            label = QLabel(category.name)
            line_edit = QLineEdit(str(self.j_table.read_percentage(category, self.subject)))
            line_edits.append(line_edit)
            form_layout.addRow(label, line_edit)
        return line_edits

    def update_percentages_in_database(self):
        total = 0
        for line_edit in self.line_edits:
            number = line_edit.text()
            try:
                value = float(number)
                if 0 <= value <= 100:
                    total += value
                else:
                    self.error_message("Values should be between 0 and 100")
                    return
            except ValueError:
                self.error_message("Invalid Number Input: Don't use letters or special characters")
                return
        if total == 100:
            for index, line_edit in enumerate(self.line_edits):
                number = int(line_edit.text())
                if not number:
                    number = 0
                self.j_table.update_percentage(self.categories[index], self.subject, number)
            self.accept()
        else:
            self.error_message(f'The Percentages must add up to 100. Current Total: {total} ')

    @staticmethod
    def error_message(text):
        msg_box = QMessageBox()
        msg_box.setText(text)
        msg_box.addButton(QMessageBox.StandardButton.Ok)
        msg_box.exec()
