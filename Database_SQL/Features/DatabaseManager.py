import _sqlite3


class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.classes_table = "Classes"
        self.subjects_table = "Subjects"
        self.students_table = "Students"
        self.categories_table = "Categories"
        self.grades_table = "Grades"
        self.classes_subjects = "Classes_Subjects"
        self.categories_subjects = "Categories_Subjects"

    def create_database(self):
        self.ensure_created_classes()
        self.ensure_created_subjects()
        self.ensure_created_students()
        self.ensure_created_categories()
        self.ensure_created_grades()
        self.ensure_created_classes_subjects()
        self.ensure_created_categories_subjects()

    def connect(self):
        return _sqlite3.connect(self.database_name)

    def ensure_created_classes(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.classes_table}
                                (ID TEXT PRIMARY KEY, 
                                Name TEXT)''')
        print(f"The table {self.classes_table} has been created")
        connection.commit()

    def ensure_created_subjects(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.subjects_table} (ID TEXT PRIMARY KEY, Name TEXT)')
        print(f"The table '{self.subjects_table}' has been created")
        connection.commit()

    def ensure_created_students(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.students_table} 
                        (ID INTEGER PRIMARY KEY, 
                        class_id, 
                        Name TEXT,
                        FOREIGN KEY (class_id) REFERENCES {self.classes_table}(ID) ON DELETE CASCADE)''')
        print(f"The table '{self.students_table}' has been created")
        connection.commit()

    def ensure_created_categories(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.categories_table} 
                                (ID PRIMARY KEY, 
                                Name TEXT)''')
        print(f"The table '{self.categories_table}' has been created")
        connection.commit()

    def ensure_created_grades(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.grades_table} 
                                        (ID PRIMARY KEY, 
                                        student_id INTEGER,
                                        class_id TEXT,
                                        category_subject_id,
                                        quarter INTEGER,
                                        grade REAL,
                                        FOREIGN KEY (student_id) REFERENCES {self.students_table}(ID) ON DELETE CASCADE,
                                        FOREIGN KEY (class_id) REFERENCES {self.classes_table}(ID) ON DELETE CASCADE,
                                        FOREIGN KEY (category_subject_id) REFERENCES 
                                        {self.categories_subjects} (Id) ON DELETE CASCADE)''')
        print(f"The table {self.grades_table} has been created")
        connection.commit()

    def ensure_created_classes_subjects(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.classes_subjects} 
                                (class_id, 
                                subject_id,
                                FOREIGN KEY (subject_id) REFERENCES {self.subjects_table}(ID) ON DELETE CASCADE,
                                FOREIGN KEY (class_id) REFERENCES {self.classes_table}(ID) ON DELETE CASCADE)''')
        print(f"The table '{self.classes_subjects}' has been created")
        connection.commit()

    def ensure_created_categories_subjects(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.categories_subjects} 
                                (Id PRIMARY KEY,
                                category_id, 
                                subject_id,
                                percentage INTEGER,
                                FOREIGN KEY (subject_id) REFERENCES {self.subjects_table}(ID) ON DELETE CASCADE,
                                FOREIGN KEY (category_id) REFERENCES {self.categories_table}(ID) ON DELETE CASCADE)''')
        print(f"The table '{self.categories_subjects}' has been created")
        connection.commit()
