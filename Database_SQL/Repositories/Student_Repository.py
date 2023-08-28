from Database_SQL.Models.Student import Student


class StudentRepository:
    def __init__(self, database_manager):
        self.dm = database_manager

    def create(self, student_id, name, class_name):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {self.dm.students_table} WHERE id == ?', (student_id,))
        existing_student = cursor.fetchone()
        if existing_student:
            print("Student already exists")
            return
        else:
            cursor.execute(f'SELECT ID FROM {self.dm.classes_table} WHERE Name == ?', (class_name,))
            class_id = "".join(cursor.fetchone())
            cursor.execute(f'''INSERT INTO {self.dm.students_table} 
                                (ID, class_id, Name) 
                                values ("{student_id}", "{class_id}", "{name}") ''')
            print(f"The student '{name}' has been added to the class '{class_name}'")
            connection.commit()

    # read all student names or a specific student's name given id
    def read(self, id=None):
        connection = self.dm.connect()
        cursor = connection.cursor()
        result = []
        if id is None:
            c = cursor.execute(f'SELECT ID, class_id, Name FROM {self.dm.students_table}')
            data = cursor.fetchall()
            for x in c:
                print(x)
            if data:
                for s in data:
                    result.append(Student(s[0], s[1], s[2]))
        else:
            cursor.execute(f'SELECT ID, class_id, Name FROM {self.dm.students_table} WHERE ID == ?', (id,))
            data = cursor.fetchone()
            if data:
                result.append(Student(data[0], data[1], data[2]))
        return result

    def search_students(self, query):
        students = self.read()
        result = []
        for student in students:
            if query in student.name.lower():
                result.append(student.name)
        return result

    # change the name of the student or move the student to a different class
    def update(self, student_id, new_name=None, new_class_name=None):
        connection = self.dm.connect()
        cursor = connection.cursor()
        if new_name is not None:
            cursor.execute(f"UPDATE {self.dm.students_table} SET Name = ? WHERE id = ?", (f"{new_name}", student_id))
        if new_class_name is not None:
            data = cursor.execute(f'SELECT ID FROM {self.dm.classes_table} WHERE Name == ?', (new_class_name,))
            new_class_id = data.fetchone()[0]
            cursor.execute(f"UPDATE {self.dm.students_table} SET class_id = ? "
                           f"WHERE id = ?", (f"{new_class_id}", student_id))
        connection.commit()

    # Delete all students or a specific student
    def delete(self, student_id=None, all=False):
        connection = self.dm.connect()
        cursor = connection.cursor()
        if all:
            cursor.execute(f'DELETE FROM {self.dm.students_table}')
            print("All students deleted")
        elif student_id is not None:
            name = "".join(cursor.execute(f'SELECT Name FROM {self.dm.students_table} '
                                          f'WHERE ID == ?', (student_id,)).fetchone())
            cursor.execute(f'DELETE from {self.dm.students_table} WHERE ID == "{student_id}"')
            print(f"The student '{name}' with ID '{student_id}' has been deleted")
        else:
            print("Error: please specify if you intend to delete a "
                  "specific student (write student name) or all students (set all=True)")
        connection.commit()
