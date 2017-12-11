# Create Student and Teacher classes
# Student
# learn()
# question(teacher) -> calls the teachers answer method
# Teacher
# teach(student) -> calls the students learn method
# answer()

class Student(object):

    def __init__(self, name, learning):
        self.name = name
        self.learning = learning

    def learn(self):
        return self.learning

    def question(self, teacher):
        return teacher.answer()


class Teacher(object):

    def __init__(self, name, answering):
        self.name = name
        self.answering = answering
    
    def answer(self):
        return self.answering

    def teach(self, student):
        return student.learn()


jacob = Student("Jacob", "2 + 2")

moria = Teacher("Moria", "= 4")

print(jacob.question(moria))

print(moria.teach(jacob))