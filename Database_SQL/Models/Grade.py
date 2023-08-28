class Grade:
    def __init__(self, id, student_id, class_id, category_subject_id, quarter, grade):
        self.id = id
        self.student_id = student_id
        self.class_id = class_id
        self.category_subject_id = category_subject_id
        self.quarter = quarter
        self.grade = grade

    def __str__(self):
        return "ID: " + str(self.id) + ", student_id: " + str(self.student_id) + \
                ", quarter: " + str(self.quarter) + ", grade: " + str(self.grade)



