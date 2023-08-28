import uuid

from Database_SQL.Models.Grade import Grade


class GradesRepository:
    def __init__(self, database_manager, r_func):
        self.r_func = r_func
        self.dm = database_manager

    def create(self, student_id, class_id, category_name, subject_name, quarter, grade):
        connection = self.dm.connect()
        cursor = connection.cursor()
        category = self.r_func.get_category_by_category_name(category_name)
        subject = self.r_func.get_subject_by_subject_name(subject_name)
        cursor.execute(f'SELECT Id FROM {self.dm.categories_subjects} WHERE category_id = ? AND subject_id = ?',
                       (category.id, subject.id))
        category_subject_id = cursor.fetchone()
        grade = Grade(uuid.uuid4(), student_id, class_id, category_subject_id[0], quarter, grade)
        cursor.execute(f'SELECT Id FROM {self.dm.grades_table} '
                       f'WHERE student_id = ? AND category_subject_id = ? AND quarter = ?',
                       (grade.student_id, grade.category_subject_id, grade.quarter))
        existing_grade = cursor.fetchone()
        if existing_grade:
            print("grade already exists")
            return
        else:
            cursor.execute(f'INSERT INTO {self.dm.grades_table} '
                           f'(ID, student_id, class_id, category_subject_id, quarter, grade) '
                           f'values ("{grade.id}", "{grade.student_id}", "{grade.class_id}", '
                           f'"{grade.category_subject_id}", "{grade.quarter}", "{grade.grade}")')
            print(f"The grade '{grade.grade}' has been added")
        connection.commit()

    def read(self, id=None):
        connection = self.dm.connect()
        cursor = connection.cursor()
        result = []
        if id is None:
            cursor.execute(f'SELECT ID, student_id, class_id, category_subject_id, quarter, grade '
                           f'FROM {self.dm.grades_table}')
            data = cursor.fetchall()
            for g in data:
                grade_object = Grade(g[0], g[1], g[2], g[3], g[4], g[5])
                result.append(grade_object)
        else:
            cursor.execute(f'SELECT ID, student_id, class_id, category_subject_id, quarter, grade '
                           f'FROM {self.dm.grades_table} WHERE ID == ?', (id,))
            data = cursor.fetchone()
            if data:
                result.append(Grade(data[0], data[1], data[2], data[3], data[4], data[5]))
            else:
                raise Exception("No grade with that ID available")
        return result

    def update(self, grade_id, new_grade):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.dm.grades_table} SET grade = ? WHERE id = ?", (f"{new_grade}", grade_id))
        connection.commit()

    def delete(self, grade_id=None, all=False):
        connection = self.dm.connect()
        cursor = connection.cursor()
        # cursor.execute('PRAGMA foreign_keys = ON;')  # enables foreign key restraint
        if all:
            cursor.execute(f'DELETE FROM {self.dm.grades_table}')
            print("All grades deleted")
        elif grade_id is not None:
            cursor.execute(f'DELETE from {self.dm.grades_table} WHERE ID == "{grade_id}"')
            print(f"The grade with ID '{grade_id}' has been deleted")
        else:
            raise Exception("Error: please specify if you intend to delete a "
                  "specific grade (write grade ID) or all grades (set all=True)")
        connection.commit()
