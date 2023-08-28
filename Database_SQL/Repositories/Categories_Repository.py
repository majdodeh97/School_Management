import uuid

from Database_SQL.Models.Category import Category


class CategoriesRepository:
    def __init__(self, database_manager):
        self.dm = database_manager

    def create(self, category_name):
        category = Category(str(uuid.uuid4()), category_name)
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {self.dm.categories_table} WHERE Name == ?', (category.name.lower(),))
        existing_category = cursor.fetchone()
        if existing_category:
            return existing_category[0]
        else:
            cursor.execute(f'INSERT INTO {self.dm.categories_table} (ID, Name) '
                           f'values ("{category.id}", "{category.name.lower()}")')
            print(f"The category '{category.name}' has been added")
            connection.commit()
            return category.id

    def read(self, id=None):
        connection = self.dm.connect()
        cursor = connection.cursor()
        result = []
        if id is None:
            cursor.execute(f'SELECT * FROM {self.dm.categories_table}')
            data = cursor.fetchall()
            for category in data:
                c = Category(category[0], category[1])
                result.append(c)
        else:
            cursor.execute(f'SELECT * FROM {self.dm.categories_table} WHERE ID == ?', (id,))
            data = cursor.fetchone()
            if data:
                result.append(Category(data[0], data[1]))
            else:
                raise Exception("No category with that ID available")
        return result

    def update(self, category_id, new_name):
        connection = self.dm.connect()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.dm.categories_table} SET Name = ? WHERE id = ?", (f"{new_name}", category_id))
        connection.commit()

    def delete(self, category_id=None, all=False):
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
