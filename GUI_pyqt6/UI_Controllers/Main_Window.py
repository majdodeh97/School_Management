from PyQt6 import QtCore
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from PyQt6.QtWidgets import (
    QMainWindow, QMessageBox, QFileDialog, QLabel, QLineEdit, QDialog
)

from GUI_pyqt6.Qt_Designer_py_files.auto_Main_Window import Ui_MainWindow
from GUI_pyqt6.UI_Controllers.Print_Calculation import PrintCalculation
from GUI_pyqt6.UI_Controllers.Edit_Percentages import EditPercentages
from GUI_pyqt6.UI_Controllers.Statistics import StatisticsDialog
from Database_SQL.Models.Class import Class
from Database_SQL.Models.Student import Student
from Database_SQL.Features.Excel_to_database import add_gradebook_to_database, import_excel_files_from_directory


class StandardItem(QStandardItem):
    def __init__(self, text=""):
        super().__init__()
        self.setText(text)


class Window(QMainWindow):

    def __init__(self, c_repo, st_repo, r_func, email_sender, j_table, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.c_repo = c_repo
        self.st_repo = st_repo
        self.r_func = r_func
        self.j_table = j_table
        self.set_widgets_visibility(False)
        self.email_sender = email_sender
        self.recipients = set()
        self.tree_model = QStandardItemModel()
        self.refresh()
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.ui.subject_comboBox.currentTextChanged.connect(self.set_category_combobox)
        self.ui.subject_gc_comboBox.currentTextChanged.connect(self.create_category_labels)
        self.ui.query_text.textChanged.connect(self.search_tree_view)
        self.ui.email_button.clicked.connect(self.email_clicked)
        self.ui.addRecipient_button.clicked.connect(self.add_recipient_clicked)
        self.ui.removeRecipient_button.clicked.connect(self.remove_recipient_clicked)
        self.ui.graph_button.clicked.connect(self.generate_graph_clicked)
        self.ui.select_all_button.clicked.connect(self.select_all_checkboxes)
        self.ui.deselect_all_button.clicked.connect(self.deselect_all_checkboxes)
        self.ui.import_excel_file_menu_action.triggered.connect(self.import_from_excel)
        self.ui.import_from_folder_menu_action.triggered.connect(self.import_from_folder)
        self.ui.print_calculation_menu_action.triggered.connect(self.open_print_calc_dialog)
        self.ui.edit_percentages_button.clicked.connect(self.open_edit_percentages_dialog)
        self.ui.grade_calculate_button.clicked.connect(self.calculate_grade)
        self.ui.gc_extract_grades_button.clicked.connect(self.extract_grades)
        self.ui.gc_clear_button.clicked.connect(self.clear_line_edits)

    def refresh(self):
        self.set_tree_view()
        selection_model = self.ui.treeView.selectionModel()
        selection_model.currentChanged.connect(self.get_subject_combobox)

    def get_subject_combobox(self):
        self.set_subject_combobox(self.ui.subject_comboBox)
        self.set_subject_combobox(self.ui.subject_gc_comboBox)

    def set_subject_combobox(self, widget):
        widget.clear()
        type_ = self.check_type()
        if type_ == "class":
            class_ = self.r_func.get_class_by_class_name(self.ui.treeView.currentIndex().data())
            subjects = self.r_func.get_subjects_by_class_id(class_.id)
            for subject in subjects:
                widget.addItem(subject.name)
        elif type_ == "student":
            class_ = self.r_func.get_class_by_class_name(self.ui.treeView.currentIndex().parent().data())
            subjects = self.r_func.get_subjects_by_class_id(class_.id)
            for subject in subjects:
                widget.addItem(subject.name)

    def set_category_combobox(self):
        type_ = self.check_type()
        current_text = self.ui.subject_comboBox.currentText()
        if current_text == '':
            return
        elif type_ == "student":
            self.ui.category_comboBox.clear()
            self.ui.category_comboBox.addItem("All")
        elif type_ == "class":
            self.ui.category_comboBox.clear()
            subject = self.r_func.get_subject_by_subject_name(current_text)
            categories = self.r_func.get_categories_by_subject_id(subject.id)
            for category in categories:
                self.ui.category_comboBox.addItem(category.name)
        else:
            raise Exception("Invalid Selection from TreeView")

    def set_tree_view(self):
        root_node = self.tree_model.invisibleRootItem()
        classes_ = self.c_repo.read()
        for class_ in classes_:
            c = QStandardItem(class_.name)
            root_node.appendRow(c)
            for student in class_.students:
                s = QStandardItem(student.name)
                c.appendRow(s)
        self.ui.treeView.setHeaderHidden(True)
        self.ui.treeView.setModel(self.tree_model)

    def search_tree_view(self, text):
        if not text:
            self.ui.treeView.setModel(self.tree_model)
            return

        filtered_model = QStandardItemModel()
        root_node = filtered_model.invisibleRootItem()

        for row in range(self.tree_model.rowCount()):
            found_match = False
            class_item = self.tree_model.item(row)
            filtered_class_item = QStandardItem(class_item.text())

            for child_row in range(class_item.rowCount()):
                student_item = class_item.child(child_row)
                if text.lower() in student_item.text().lower():
                    found_match = True
                    filtered_student_item = QStandardItem(student_item.text())
                    filtered_class_item.appendRow(filtered_student_item)
            if found_match:
                root_node.appendRow(filtered_class_item)

        self.ui.treeView.setModel(filtered_model)
        self.ui.treeView.expandAll()

    def check_type(self):
        current_index = self.ui.treeView.currentIndex()
        if current_index.row() == -1:  # No Selection
            return
        else:
            if current_index.parent().data() is None:
                return "class"
            else:
                return "student"

    @staticmethod
    def error_message(text):
        msg_box = QMessageBox()
        msg_box.setText(text)
        msg_box.addButton(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def generate_graph_clicked(self):
        current_subject = self.ui.subject_comboBox.currentText()
        current_category = self.ui.category_comboBox.currentText()

        type_ = self.check_type()
        class_, student, categories = None, None, None
        class_selected = False
        if type_ == "class":
            class_selected = True
            class_ = self.r_func.get_class_by_class_name(self.ui.treeView.currentIndex().data())
        elif type_ == "student":
            class_ = self.r_func.get_class_by_class_name(self.ui.treeView.currentIndex().parent().data())
            student = self.ui.treeView.currentIndex().data()
            subject = self.r_func.get_subject_by_subject_name(current_subject)
            categories = self.r_func.get_categories_by_subject_id(subject.id)
        else:
            return
        checkboxes = [self.ui.Q1_checkBox, self.ui.Q2_checkBox, self.ui.Q3_checkBox, self.ui.Q4_checkBox]
        quarter_checkbox_states = {}

        for i in range(1, 5):
            state = checkboxes[i - 1].isChecked()
            quarter_checkbox_states[i] = state

        if all(value is False for value in quarter_checkbox_states.values()):
            self.error_message("Please Select at least one Quarter before generating a graph")
        else:
            StatisticsDialog(self, self.r_func, current_subject, current_category, quarter_checkbox_states,
                             class_selected, class_, student, categories)

    def add_recipient_clicked(self):
        raise Exception("fake error!")
        type_ = self.check_type()
        if type_ == "class":
            class_name = self.ui.treeView.currentIndex().data()
            class_ = self.r_func.get_class_by_class_name(class_name)
            if class_ not in self.recipients:
                self.ui.recipient_list.addItem(class_.name)
                self.recipients.add(class_)

        elif type_ == "student":  # Student
            student_name = self.ui.treeView.currentIndex().data()
            student = self.r_func.get_student_by_student_name(student_name)
            if student not in self.recipients:
                self.ui.recipient_list.addItem(student_name)
                self.recipients.add(student)

    def remove_recipient_clicked(self):
        current_item = self.ui.recipient_list.currentItem()
        if not current_item:
            return

        current_item_text = current_item.text()
        current_item_index = self.ui.recipient_list.findItems(current_item_text, QtCore.Qt.MatchFlag.MatchExactly)[0]
        row = self.ui.recipient_list.row(current_item_index)
        self.ui.recipient_list.takeItem(row)

        for rec in self.recipients:
            if rec.name == current_item_text:
                self.recipients.remove(rec)
                break

    def email_clicked(self):
        students_to_email = []

        for recipient in self.recipients:
            if type(recipient) is Class:
                students = self.r_func.get_students_by_class_id(recipient.id)
                for student in students:
                    if student in self.recipients:
                        continue
                    else:
                        students_to_email.append(student)
            elif type(recipient) is Student:
                students_to_email.append(recipient)

        self.email_sender.email_students(students_to_email)

    def select_all_checkboxes(self):
        checkboxes = [self.ui.Q1_checkBox, self.ui.Q2_checkBox, self.ui.Q3_checkBox, self.ui.Q4_checkBox]
        for checkbox in checkboxes:
            checkbox.setChecked(True)

    def deselect_all_checkboxes(self):
        checkboxes = [self.ui.Q1_checkBox, self.ui.Q2_checkBox, self.ui.Q3_checkBox, self.ui.Q4_checkBox]
        for checkbox in checkboxes:
            checkbox.setChecked(False)

    def import_from_excel(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter('Excel Files (*.xlsx *.xls)')
        file_dialog.exec()

        selected_file = file_dialog.selectedFiles()
        if selected_file:

            add_gradebook_to_database(selected_file[0], "/Users/loayodeh/PycharmProjects/School/Databases/test1.db")
        self.refresh()

    def import_from_folder(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog.exec()

        selected_dirs = file_dialog.selectedFiles()
        if selected_dirs:
            import_excel_files_from_directory(selected_dirs[0])
        self.refresh()

    def open_edit_percentages_dialog(self):
        categories = self.get_categories()
        if categories:
            edit_percentages_dialog = EditPercentages(self, self.j_table, categories,
                                                      self.ui.subject_gc_comboBox.currentText())
            if edit_percentages_dialog.exec() == QDialog.DialogCode.Accepted:
                self.create_category_labels()
        else:
            self.error_message("Please Select a Student before Editing the Percentages")

    def open_print_calc_dialog(self):
        PrintCalculation(self, self.c_repo, self.r_func)

    def get_categories(self):
        type_ = self.check_type()
        current_text = self.ui.subject_gc_comboBox.currentText()
        if current_text == '':
            return []
        elif type_ == "student":
            subject = self.r_func.get_subject_by_subject_name(current_text)
            categories = self.r_func.get_categories_by_subject_id(subject.id)

            for category in categories:
                if category.name.lower() == "total":
                    categories.remove(category)

        elif type_ == "class":
            return []
        else:
            raise Exception("Invalid treeview selection")
        return categories

    def delete_widgets(self):
        layout = self.ui.gridLayout_grade_calculator_left
        row_count = layout.rowCount()
        for row in range(row_count - 1, 0, -1):
            for col in range(layout.columnCount()):
                item = layout.itemAtPosition(row, col)
                if item is not None:
                    item.widget().deleteLater()
                    layout.removeItem(item)

    def create_category_labels(self):
        self.ui.lcdNumber.display(0)
        self.delete_widgets()
        if self.check_type() == "student":
            self.set_widgets_visibility(True)
        else:
            self.set_widgets_visibility(False)
            return
        self.set_quarter_combobox()
        categories = self.get_categories()
        subject = self.ui.subject_gc_comboBox.currentText()
        if categories:
            grid_layout = self.ui.gridLayout_grade_calculator_left

            for index, category in enumerate(categories):
                category_label = QLabel(category.name)
                percentage_label = QLabel(str(self.j_table.read_percentage(category, subject)) + "%")
                line_edit = QLineEdit()
                grid_layout.addWidget(category_label, index + 1, 0)
                grid_layout.addWidget(line_edit, index + 1, 1)
                grid_layout.addWidget(percentage_label, index + 1, 2)

    def calculate_grade(self):
        grid_layout = self.ui.gridLayout_grade_calculator_left
        row_count = grid_layout.rowCount()
        average = 0
        for i in range(1, row_count):
            percentage_item = grid_layout.itemAtPosition(i, 2)
            line_edit_item = grid_layout.itemAtPosition(i, 1)
            if percentage_item and line_edit_item:
                percentage_string = percentage_item.widget().text()
                if percentage_string != "None%":
                    percentage_decimal = float(percentage_string.strip('%')) / 100
                    grade_input = line_edit_item.widget().text()
                    if grade_input:
                        try:
                            grade = float(grade_input)
                            if 0 <= grade <= 100:
                                grade = percentage_decimal * float(grade_input)
                                average += grade
                            else:
                                self.error_message("Grade input needs to be a value between 0 and 100")
                                return
                        except ValueError:
                            self.error_message("Invalid Number Input: don't use letters or special characters")
                            return
                    else:
                        self.error_message("Please fill all grade fields before calculating the average grade")
                        return
                else:
                    self.error_message("Please Edit Percentages before Calculating the Grade")
                    return
        self.ui.lcdNumber.display(average)

    def set_widgets_visibility(self, boolean):
        layout = self.ui.gridLayout_grade_calculator_left
        for index in range(layout.columnCount()):
            layout.itemAtPosition(0, index).widget().setVisible(boolean)

    def extract_grades(self):
        type_ = self.check_type()
        if type_ == "student":
            student = self.ui.treeView.currentIndex().data()
            subject = self.ui.subject_gc_comboBox.currentText()
            quarter = self.ui.gc_quarters_comboBox.currentText()[1]
            categories = self.get_categories()
            for index, category in enumerate(categories):
                cat_subj_id = self.r_func.get_category_subject_id_by_subject_name_and_category_name(subject,
                                                                                                    category.name)
                grade = self.r_func.get_grade_by_student_name_and_cat_subj_id_and_quarter(student, cat_subj_id, quarter)
                layout = self.ui.gridLayout_grade_calculator_left
                widget = layout.itemAtPosition(index + 1, 1).widget()
                widget.setText(str(grade))
        else:
            return

    def set_quarter_combobox(self):
        self.ui.gc_quarters_comboBox.clear()
        student = self.ui.treeView.currentIndex().data()
        data = self.r_func.check_available_quarters(student)
        data_unpacked = [value for (value,) in data]
        quarters = list(set(data_unpacked))
        for quarter in quarters:
            self.ui.gc_quarters_comboBox.addItem("Q" + str(quarter))

    def clear_line_edits(self):
        self.ui.lcdNumber.display(0)
        layout = self.ui.gridLayout_grade_calculator_left
        for index in range(1, layout.rowCount()):
            layout.itemAtPosition(index, 1).widget().clear()
