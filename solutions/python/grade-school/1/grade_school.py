class School:
    def __init__(self):
        self.students = {}
        self.add_log = []

    def add_student(self, name, grade):

        # prevent same student in multiple grades
        for g in self.students:
            if name in self.students[g]:
                self.add_log.append(False)
                return False

        if grade not in self.students:
            self.students[grade] = []

        if name in self.students[grade]:
            self.add_log.append(False)
            return False

        self.students[grade].append(name)
        self.add_log.append(True)
        return True

    def roster(self):
        result = []
        for grade in sorted(self.students):
            result.extend(sorted(self.students[grade]))
        return result

    def grade(self, grade_number):
        return sorted(self.students.get(grade_number, []))

    def added(self):
        return self.add_log
