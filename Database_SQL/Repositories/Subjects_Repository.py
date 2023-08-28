import uuid
from Database_SQL.Models.Subject import Subject


class SubjectRepository:
    def __init__(self, database_manager, r_func):
        self.r_func = r_func
        self.dm = database_manager

    def create(self, name):
        subject = Subject(str(uuid.uuid4()), name)
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {self.dm.subjects_table} WHERE Name == ?', (subject.name,))
        existing_subject = cursor.fetchone()
        if existing_subject:
            return existing_subject[0]
        else:
            cursor.execute(f'INSERT INTO {self.dm.subjects_table} (ID, Name) values ("{subject.id}", "{subject.name}")')
            print(f"The subject '{subject.name}' has been added")
            connection.commit()
            return subject.id

    def read(self, subject_id=None):
        connection = self.dm.connect()
        cursor = connection.cursor()
        subjects = []
        if subject_id is None:
            cursor.execute(f'SELECT ID, Name FROM {self.dm.subjects_table}')
            data = cursor.fetchall()
            for s in data:
                categories = self.r_func.get_categories_by_subject_id(s[0])
                classes = self.r_func.get_classes_by_subject_id(s[0])
                subjects.append(Subject(s[0], s[1], classes, categories))
        else:
            cursor.execute(f'SELECT Name FROM {self.dm.subjects_table} WHERE ID == ?', (subject_id,))
            subject_name = cursor.fetchone()
            if subject_name:
                categories = self.r_func.get_categories_by_subject_id(subject_id)
                classes = self.r_func.get_classes_by_subject_id(subject_id)
                subjects.append(Subject(subject_id, subject_name[0], classes, categories))
            else:
                raise Exception("No subject with that id available")
        return subjects

    def update(self, subject_id, new_name):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.dm.subjects_table} SET Name = ? WHERE id = ?", (f"{new_name}", subject_id))
        connection.commit()

    def delete(self, subject_id=None, all=False):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')  # enables foreign key restraint
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
