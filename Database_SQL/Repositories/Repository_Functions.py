from Database_SQL.Models.Subject import Subject
from Database_SQL.Models.Student import Student
from Database_SQL.Models.Class import Class
from Database_SQL.Models.Category import Category
from Database_SQL.Models.Grade import Grade


class RepositoryFunctions:
    def __init__(self, database_manager):
        self.dm = database_manager

    def get_subjects_by_class_id(self, class_id):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT subject_id FROM {self.dm.classes_subjects} WHERE class_id == ?', (class_id,))
        subjects_ids = cursor.fetchall()
        result = []
        for subject_id in subjects_ids:
            cursor.execute(f'SELECT Name FROM {self.dm.subjects_table} WHERE ID == ?', (subject_id[0],))
            name = cursor.fetchone()
            result.append(Subject(subject_id[0], name[0]))
        return result

    def get_classes_by_subject_id(self, subject_id):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT class_id FROM {self.dm.classes_subjects} WHERE subject_id == ?', (subject_id,))
        classes_ids = cursor.fetchall()
        result = []
        for class_id in classes_ids:
            cursor.execute(f'SELECT Name FROM {self.dm.classes_table} WHERE ID == ?', (class_id[0],))
            name = cursor.fetchone()
            result.append(Class(class_id[0], name[0]))
        return result

    def get_categories_by_subject_id(self, subject_id):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT category_id FROM {self.dm.categories_subjects} WHERE subject_id == ?', (subject_id,))
        category_ids = cursor.fetchall()
        result = []
        for category_id in category_ids:
            cursor.execute(f'SELECT Name FROM {self.dm.categories_table} WHERE ID == ?', (category_id[0],))
            name = cursor.fetchone()
            result.append(Category(category_id[0], name[0]))
        return result

    def get_students_by_class_id(self, class_id):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT ID, Name FROM {self.dm.students_table} WHERE class_id == ?', (class_id,))
        students = cursor.fetchall()
        result = []
        for student in students:
            result.append(Student(student[0], class_id, student[1]))
        return result

    def get_class_by_class_name(self, class_name):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT ID, Name FROM {self.dm.classes_table} WHERE Name == ?', (class_name,))
        result = cursor.fetchone()
        class_ = Class(result[0], result[1])
        return class_

    def get_number_of_students_by_class_name(self, class_name):
        class_id = self.get_class_by_class_name(class_name).id
        number_of_students = len(self.get_students_by_class_id(class_id))
        return number_of_students

    def get_student_by_student_name(self, name):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT ID, class_id, Name FROM {self.dm.students_table} WHERE Name == ?', (name,))
        student = cursor.fetchone()
        return Student(student[0], student[1], student[2])

    def get_category_by_category_name(self, category_name):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT ID, Name FROM {self.dm.categories_table} WHERE Name == ?', (category_name.lower(),))
        result = cursor.fetchone()
        category = Category(result[0], result[1])
        return category

    def get_subject_by_subject_name(self, subject_name):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT ID, Name FROM {self.dm.subjects_table} WHERE Name == ?', (subject_name,))
        result = cursor.fetchone()
        subject = Subject(result[0], result[1])
        return subject

    def get_grades_by_student_id(self, student_id):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {self.dm.grades_table} WHERE student_id == ?', (student_id,))
        grades = cursor.fetchall()
        result = []
        if grades:
            for grade in grades:
                result.append(Grade(grade[0], grade[1], grade[2], grade[3], grade[4], grade[5]))
        else:
            raise Exception("No student with that id found")
        return result

    def get_category_subject_by_category_subject_id(self, category_subject_id):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {self.dm.categories_subjects} WHERE id == ?', (category_subject_id,))
        category_subject = cursor.fetchone()
        result = []

        category_id = category_subject[1]
        cursor.execute(f'SELECT * FROM {self.dm.categories_table} WHERE ID == ?', (category_id,))
        category = cursor.fetchone()
        result.append(Category(category[0], category[1]))

        subject_id = category_subject[2]
        cursor.execute(f'SELECT * FROM {self.dm.subjects_table} WHERE ID == ?', (subject_id,))
        subject = cursor.fetchone()
        result.append(Subject(subject[0], subject[1]))

        return result

    def get_category_subject_id_by_subject_name_and_category_name(self, subject_name, category_name):
        connection = self.dm.connect()
        cursor = connection.cursor()
        subject_id = self.get_subject_by_subject_name(subject_name).id
        category_id = self.get_category_by_category_name(category_name).id
        cursor.execute(f'SELECT id FROM {self.dm.categories_subjects} WHERE category_id == ? AND subject_id == ?',
                       (category_id, subject_id))
        category_subject_id = cursor.fetchone()
        return category_subject_id[0]

    def get_grades_by_class_name_and_category_subject_id_and_quarter(self, class_name, category_subject_id, quarter):
        class_id = self.get_class_by_class_name(class_name).id
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT grade FROM {self.dm.grades_table} '
                       f'WHERE class_id == ? AND category_subject_id == ? AND quarter == ?',
                       (class_id, category_subject_id, quarter))
        data = cursor.fetchall()
        grades = []
        for grade in data:
            grades.append(grade[0])
        return grades

    def get_grade_by_student_name_and_cat_subj_id_and_quarter(self, student_name, cat_subj_id, quarter):
        student_id = self.get_student_by_student_name(student_name).id
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT grade FROM {self.dm.grades_table} '
            f'WHERE student_id == ? AND category_subject_id == ? AND quarter == ?',
            (student_id, cat_subj_id, quarter))
        grade = cursor.fetchone()
        return grade[0]

    def delete_subject(self, subject_id=None, all=False):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')
        if all:
            cursor.execute(f'DELETE FROM {self.dm.subjects_table}')
            print("All subjects deleted")
        elif subject_id is not None:
            cursor.execute(f'DELETE from {self.dm.subjects_table} WHERE ID == "{subject_id}"')
            print(f"The subject with ID '{subject_id}' has been deleted")
        else:
            raise Exception("Error: please specify if you intend to delete a "
                  "specific subject (write subject ID) or all subjects (set all=True)")
        connection.commit()
        cursor.execute(f'''
                    SELECT {self.dm.categories_table}.ID FROM {self.dm.categories_table}
                    LEFT JOIN {self.dm.categories_subjects} 
                    ON {self.dm.categories_table}.ID = {self.dm.categories_subjects}.category_id
                    WHERE {self.dm.categories_subjects}.category_id is NULL
            ''')
        data = cursor.fetchall()
        for category in data:
            self.delete_category(category[0])

    def delete_category(self, category_id=None, all=False):
        connection = self.dm.connect()
        cursor = connection.cursor()
        # cursor.execute('PRAGMA foreign_keys = ON;')  # enables foreign key restraint
        if all:
            cursor.execute(f'DELETE FROM {self.dm.categories_table}')
            print("All categories deleted")
        elif category_id is not None:
            cursor.execute(f'DELETE from {self.dm.categories_table} WHERE ID == "{category_id}"')
            print(f"The category with ID '{category_id}' has been deleted")
        else:
            raise Exception("Error: please specify if you intend to delete a "
                  "specific category (write category ID) or all categories (set all=True)")
        connection.commit()

    def check_available_quarters(self, student_name):
        student = self.get_student_by_student_name(student_name)
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT quarter FROM {self.dm.grades_table} WHERE student_id == "{student.id}"')
        quarters = cursor.fetchall()
        return quarters
