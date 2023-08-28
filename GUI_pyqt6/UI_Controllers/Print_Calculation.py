
from PyQt6.QtWidgets import QDialog, QFormLayout, QLabel, QCheckBox
from GUI_pyqt6.Qt_Designer_py_files.auto_print_calculation_dialog import Ui_Dialog


class PrintCalculation(QDialog):
    def __init__(self, parent, c_repo, r_func):
        super().__init__(parent=parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.c_repo = c_repo
        self.r_func = r_func
        self.create_class_labels_and_checkboxes()
        self.ui.print_calculate_button.clicked.connect(self.calculate_clicked)
        self.show()

    def get_classes_from_database(self):
        classes = []
        data = self.c_repo.read()
        for class_ in data:
            classes.append(class_.name)
        return classes

    def create_class_labels_and_checkboxes(self):
        classes = self.get_classes_from_database()

        form_layout = self.ui.classes_formLayout
        form_layout.setSpacing(20)

        for class_ in classes:
            label = QLabel(class_)
            checkbox = QCheckBox()
            form_layout.addRow(checkbox, label)

    def calculate_clicked(self):
        form_layout = self.ui.classes_formLayout

        total = 0
        checked_checkboxes = 0

        for row in range(form_layout.rowCount()):

            checkbox_widget = form_layout.itemAt(row, QFormLayout.ItemRole.LabelRole).widget()
            label_widget = form_layout.itemAt(row, QFormLayout.ItemRole.FieldRole).widget()

            if isinstance(checkbox_widget, QCheckBox) and isinstance(label_widget, QLabel):
                checkbox_value = checkbox_widget.isChecked()
                label_content = label_widget.text()

                if checkbox_value:
                    checked_checkboxes += 1
                    total += self.r_func.get_number_of_students_by_class_name(label_content)

        extras = self.ui.extras_spinBox.value() * checked_checkboxes
        total += extras
        self.ui.lcdNumber.display(total)
