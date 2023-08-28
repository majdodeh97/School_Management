from PyQt6.QtWidgets import (
    QDialog, QMessageBox
)

from GUI_pyqt6.Qt_Designer_py_files.auto_statistics_dialog import Ui_Statistics_Dialog
import numpy as np


import matplotlib.pyplot as plt
from scipy.stats import norm


class StatisticsDialog(QDialog):
    def __init__(self, parent, r_func, subject, current_category, quarters_dict,
                 class_selected=False, class_=None, student=None, categories=None):
        super().__init__(parent=parent)
        self.ui = Ui_Statistics_Dialog()
        self.ui.setupUi(self)
        self.subject = subject
        self.current_category = current_category
        self.categories = categories
        self.quarters_dict = quarters_dict
        self.class_ = class_
        self.class_selected = class_selected
        self.student = student
        self.r_func = r_func
        self.check_selection()

    def check_selection(self):
        if self.class_selected:
            quarters = self.get_quarters()
            result = self.get_class_graph_info(quarters)
            if result:
                grades, label = result[0], result[1]
                self.create_class_graph(grades, label)
            else:
                return
        elif not self.class_selected:
            self.create_student_graph()

        else:
            raise Exception("No Selection Detected (class or student)")

    @staticmethod
    def error_message_no_grades_found(quarters_not_found):
        # Create a message box with a title and a message
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        text = ", ".join(quarters_not_found)
        msg_box.setText(f"No Available grades for {text}")

        # Add an "OK" button to the message box
        msg_box.addButton(QMessageBox.StandardButton.Ok)

        # Show the message box and wait for the user to close it
        msg_box.exec()

    def check_quarters(self, category):
        cat_subj_id = self.r_func.get_category_subject_id_by_subject_name_and_category_name(self.subject, category)
        quarters = self.get_quarters()
        quarters_not_found = []
        found_match = True
        for index, quarter in enumerate(quarters):
            existing_grades = self.r_func.get_grades_by_class_name_and_category_subject_id_and_quarter(self.class_.name,
                                                                                                       cat_subj_id,
                                                                                                       quarter)
            if not existing_grades:
                found_match = False
                quarters_not_found.append("Q" + str(quarter))

        if not found_match:
            self.error_message_no_grades_found(quarters_not_found)
            return False
        return True

    def get_quarters(self):
        quarters = []
        for key, value in self.quarters_dict.items():
            if value:
                quarters.append(key)
        return quarters

    def get_class_graph_info(self, quarters):
        label = []
        cat_subj_id = self.r_func.get_category_subject_id_by_subject_name_and_category_name(self.subject,
                                                                                            self.current_category)
        grades = []
        found_match = True
        quarters_not_found = []
        for index, quarter in enumerate(quarters):
            existing_grades = self.r_func.get_grades_by_class_name_and_category_subject_id_and_quarter(self.class_.name,
                                                                                                       cat_subj_id,
                                                                                                       quarter)
            if not existing_grades:
                found_match = False
                quarters_not_found.append("Q" + str(quarter))
                if index != len(quarters) - 1:
                    continue
            if not found_match:
                self.error_message_no_grades_found(quarters_not_found)
                return False
            else:
                label.append("Q" + str(quarter))
                grades.append(existing_grades)
        result = [grades, label]
        return result

    def create_class_graph(self, grades, label):
        # Flatten the list of lists into a single list of grades
        flat_grades = [grade for sublist in grades for grade in sublist]

        # Calculate the mean and standard deviation of the flattened list of grades
        mean_grade = np.mean(flat_grades)
        stddev_grade = np.std(flat_grades)

        # Create a Figure object and add a subplot
        fig, ax = plt.subplots(figsize=(8, 6), dpi=100)

        # Set the window title
        fig.canvas.manager.set_window_title('Class Graph')

        # Create a histogram of the grades distribution
        counts, bins, patches = ax.hist(grades, bins=10, label=label, edgecolor='black')
        ax.set_title(f"{self.class_.name} - {self.subject} - {self.current_category}")
        ax.set_xlabel('Grade')
        ax.set_ylabel('Frequency')

        # Generate a normal distribution curve with the same mean and standard deviation
        x = np.linspace(np.min(flat_grades), np.max(flat_grades), 100)
        y = norm.pdf(x, mean_grade, stddev_grade)

        # Overlay the normal distribution curve on the histogram
        bin_width = np.diff(bins)[0]
        scaling_factor = 175 + (25 * len(grades))
        ax.plot(x, y * scaling_factor, 'r--', label='Normal Distribution')
        ax.legend()

        if len(label) == 1:
            y1 = 0.8
            y2 = 0.75
        elif len(label) == 2:
            y1 = 0.77
            y2 = 0.72
        elif len(label) == 3:
            y1 = 0.74
            y2 = 0.69
        else:
            y1 = 0.71
            y2 = 0.66

        # Add average and standard deviation labels
        ax.text(0.03, y1, f"Mean: {mean_grade:.2f}", ha='left', va='center', transform=ax.transAxes)
        ax.text(0.03, y2, f"Standard Deviation: {stddev_grade:.2f}", ha='left', va='center', transform=ax.transAxes)

        # Show the plot using Matplotlib show() method
        plt.show()

    def get_student_graph_info(self):
        # Set the data
        categories = [category.name for category in self.categories]

        if not self.check_quarters(categories[0]):
            return False

        quarters = self.get_quarters()

        means, grades = [], []
        for quarter in quarters:
            means_temp, grades_temp = [], []
            for category in categories:
                means_temp.append(self.get_mean_grade_by_category_and_quarter(category, quarter))
                grades_temp.append(self.get_student_grade_by_category_and_quarter(category, quarter))
            means.append(means_temp)
            grades.append(grades_temp)
        return categories, quarters, means, grades

    def create_student_graph(self):
        data = self.get_student_graph_info()
        if data:
            categories, quarters, means, grades = data
        else:
            return

        fig, axs = plt.subplots(len(quarters), 1, figsize=(8, 6 * len(quarters)), sharex=True,
                                gridspec_kw={'hspace': 0.5})  # Adjust vertical space value

        fig.canvas.manager.set_window_title('Student Graph')  # Set the window title

        if not isinstance(axs, np.ndarray):
            axs = [axs]  # Convert single Axes object to a list

        for i in range(len(quarters)):
            labels = categories
            data1 = grades[i]
            data2 = means[i]

            ax = axs[i]  # Select the appropriate subplot
            x = np.arange(len(labels))
            width = 0.35

            ax.bar(x - width / 2, data1, width, label='Student Grade')
            ax.bar(x + width / 2, data2, width, label='Class Average')

            ax.set_ylabel(" Q" + str(quarters[i]))
            ax.set_xticks(x)
            ax.set_xticklabels(labels)

        axs[len(quarters) - 1].set_xlabel('Categories')
        axs[0].set_title(self.student + " - " + self.subject)
        axs[len(quarters) - 1].legend(loc='lower right')  # Create a single shared legend

        plt.tight_layout()  # Adjust spacing between subplots
        plt.show()

    def get_mean_grade_by_category_and_quarter(self, category, quarter):
        cat_subj_id = self.r_func.get_category_subject_id_by_subject_name_and_category_name(self.subject,
                                                                                            category)
        grades = self.r_func.get_grades_by_class_name_and_category_subject_id_and_quarter(self.class_.name,
                                                                                          cat_subj_id, quarter)
        for i in range(len(grades)):
            if grades[i] == 'None':
                grades[i] = 0

        mean_grade = np.mean(grades)
        return mean_grade

    def get_student_grade_by_category_and_quarter(self, category, quarter):
        cat_subj_id = self.r_func.get_category_subject_id_by_subject_name_and_category_name(self.subject,
                                                                                            category)

        grade = self.r_func.get_grade_by_student_name_and_cat_subj_id_and_quarter(self.student, cat_subj_id, quarter)
        if grade == 'None':
            grade = 0
        return grade
