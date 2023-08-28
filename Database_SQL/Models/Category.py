class Category:
    def __init__(self, id, category_name):
        self.id = id
        self.name = category_name

    def __str__(self):
        return "Category: " + self.name + ", ID: " + str(self.id)

