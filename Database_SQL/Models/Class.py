class Class:
    def __init__(self, id, name, subjects=None, students=None):
        self.id = id
        self.name = name
        self.subjects = subjects
        self.students = students

    def __str__(self):
        return "Class: " + self.name + ", ID: " + self.id

    def __ne__(self, other): # !=
        if isinstance(other, Class):
            return False

        if len(self.students) != len(other.students):
            return False

        for student in self.students:
            if student not in other.students:
                return False

        return not (self.id == other.id and self.name == other.name)

    def __eq__(self, other): # ==
        return not self.__ne__(other)

    def __hash__(self):
        return hash(self.id)

    def __len__(self):
        return len(self.students)

    def __getitem__(self, key):
        return self.students[key]

    def __setitem__(self, key, value):
        self.students[key] = value

    def __delitem__(self, key):
        del(self.students[key])

    def __iter__(self):
        for s in self.students:
            yield s

    def __contains__(self, item):
        return item in self.students