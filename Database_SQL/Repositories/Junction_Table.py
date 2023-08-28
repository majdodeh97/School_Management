import uuid


class JunctionTable:
    def __init__(self, database_manager, cl_repo, s_repo, cat_repo, r_func):
        self.dm = database_manager
        self.r_func = r_func
        self.cat_repo = cat_repo
        self.cl_repo = cl_repo
        self.s_repo = s_repo

    def create_class_subject(self, class_name, subject_name):
        class_id = self.cl_repo.create(class_name)
        subject_id = self.s_repo.create(subject_name)
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {self.dm.classes_subjects} WHERE class_id = ? AND subject_id = ?', (class_id, subject_id))
        existing_relationship = cursor.fetchone()
        if existing_relationship:
            print("Relationship already exists")
        else:
            cursor.execute(f'INSERT INTO {self.dm.classes_subjects} (class_id, subject_id) values ("{class_id}", "{subject_id}")')
            print(f'The relationship between {class_name} and {subject_name} has been made')
            connection.commit()

    def create_category_subject(self, category_name, subject_name):
        category_id = self.cat_repo.create(category_name)
        subject_id = self.s_repo.create(subject_name)
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT Id FROM {self.dm.categories_subjects} WHERE category_id = ? AND subject_id = ?', (category_id, subject_id))
        existing_relationship = cursor.fetchone()
        if existing_relationship:
            print("Relationship already exists")
        else:
            relationship_id = str(uuid.uuid4())
            cursor.execute(f'INSERT INTO {self.dm.categories_subjects} (Id, category_id, subject_id) values ("{relationship_id}", "{category_id}", "{subject_id}")')
            print(f'The relationship between {category_name} and {subject_name} has been made')
            connection.commit()

    def read_percentage(self, category, subject_name):
        subject = self.r_func.get_subject_by_subject_name(subject_name)
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT percentage FROM {self.dm.categories_subjects} WHERE category_id = ? AND subject_id = ?',
                       (category.id, subject.id))
        percentage = cursor.fetchone()
        return percentage[0]

    def update_percentage(self, category, subject_name, percentage):
        connection = self.dm.connect()
        cursor = connection.cursor()
        subject = self.r_func.get_subject_by_subject_name(subject_name)
        category_id, subject_id = category.id, subject.id
        cursor.execute(f'UPDATE {self.dm.categories_subjects} SET percentage = ? '
                       f'WHERE category_id = ? AND subject_id = ?', (percentage, category_id, subject_id))
        connection.commit()





