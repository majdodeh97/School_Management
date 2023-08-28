class Student:
    def __init__(self, id, class_id, name, grades=None):
        self.id = id
        self.class_id = class_id
        self.name = name
        self.grades = grades

    def __str__(self):
        return "Name: " + self.name + ", ID: " + str(self.id) + ", Class_ID: " + self.class_id

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False

        return self.id == other.id and self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

