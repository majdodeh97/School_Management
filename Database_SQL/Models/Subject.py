class Subject:
    def __init__(self, id, name, classes=None, categories=None):
        self.id = id
        self.name = name
        self.classes = classes
        self.categories = categories

    def __str__(self):
        return "Subject: " + self.name + ", ID: " + self.id
