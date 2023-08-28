import uuid
from Database_SQL.Models.Class import Class


# suggestions: Add try/except blocks to catch any errors
class ClassRepository:
    def __init__(self, database_manager, r_function):
        self.dm = database_manager
        self.r_func = r_function
        self.table = self.dm.classes_table

        # add a class to the database
    def create(self, name):
        class_ = Class(str(uuid.uuid4()), name, None)
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {self.table} WHERE Name == ?', (class_.name,))
        existing_class = cursor.fetchone()
        if existing_class:
            print(f"class {name} already exists")
            return existing_class[0]
        else:
            cursor.execute(f'INSERT INTO {self.table} (ID, Name) values ("{class_.id}", "{class_.name}")')
            print(f"The class '{class_.name}' has been added")
            connection.commit()
            return class_.id

    # reads the names of the classes in a specific table
    def read(self, class_id=None):
        #raise Exception("fake error!")
        connection = self.dm.connect()
        cursor = connection.cursor()
        results = []
        if class_id is None:
            cursor.execute(f'SELECT ID, Name FROM {self.table}')
            data = cursor.fetchall()
            for c in data:
                subjects = self.r_func.get_subjects_by_class_id(c[0])
                students = self.r_func.get_students_by_class_id(c[0])
                results.append(Class(c[0], c[1], subjects, students))
            return results

        else:
            cursor.execute(f'SELECT ID, Name FROM {self.table} WHERE ID == ?', (class_id,))
            data = cursor.fetchone()
            if data:
                subjects = self.r_func.get_subjects_by_class_id(data[0])
                students = self.r_func.get_students_by_class_id(data[0])
                results.append(Class(data[0], data[1], subjects, students))
            else:
                raise Exception("No class with that id available")
        return results

    def search_classes(self, query):
        courses = self.read()
        result = []
        for class_ in courses:
            if query in class_.name.lower():
                result.append(class_.name)
        return result

    # change the name of an existing class in the database
    def update(self, class_id, new_name):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.table} SET Name = ? WHERE id = ?", (f"{new_name}", class_id))
        connection.commit()

    # Delete all stored classes or delete a specific class
    def delete(self, class_id=None, all=False):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')
        if all:
            cursor.execute(f'DELETE FROM {self.table}')
            print("All classes deleted")
        elif class_id is not None:
            cursor.execute(f'DELETE from {self.table} WHERE ID == "{class_id}"')
            print(f"The class with ID '{class_id}' has been deleted")
        else:
            raise Exception("Error: please specify if you intend to delete a "
                  "specific class (write class ID) or all classes (set all=True)")
        connection.commit()
        cursor.execute(f'''
            SELECT id FROM {self.dm.subjects_table}
            LEFT JOIN {self.dm.classes_subjects}
            ON {self.dm.subjects_table}.id = {self.dm.classes_subjects}.subject_id
            WHERE {self.dm.classes_subjects}.subject_id is NULL
    ''')
        data = cursor.fetchall()
        for subject in data:
            self.r_func.delete_subject(subject[0])
