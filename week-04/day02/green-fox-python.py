class Person(object):

    def __init__(self, name=None, age=None, gender=None):
        if name is None:
            name = "Jane Doe"
        if age is None:
            age = "30"
        if gender is None:
            gender = "female"
        self.name = name
        self.age = age
        self.gender = gender
        self.goal = "My goal is: Live for the moment!"

    def introduce(self):
        return "Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + "."

    def get_goal(self):
        return self.goal

class Student(Person):

    def __init__(self, name=None, age=None, gender=None, prev_org="The School of Life", skip_d=0):
        super(Student, self).__init__(name, age, gender,)
        self.prev_org = prev_org
        self.skip_d = skip_d
        self.goal = "Be a junior software developer."

    def introduce(self):
        return "Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + " from " + self.prev_org + " who skipped " + str(self.skip_d) + " days from the course already."

    def skip_days(self, number_of_days):
        self.skip_d += number_of_days

class Mentor(Person):

    def __init__(self, name=None, age=None, gender=None, level="intermediate"):
        super().__init__(name, age, gender)
        if (level == "junior" or level == "intermediate" or level == "senior"):
            self.level = level
        else:
            self.level = "Not defined"
        self.goal = "Educate brilliant junior software developers."

    def introduce(self):
        return "Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + " " + self.level + " mentor."

class Sponsor(Person):

    def __init__(self, name=None, age=None, gender=None, company="Google", hired_students=0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students
        self.goal = "Hire brilliant junior software developers."

    def introduce(self):
        return "Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + " who represents " + self.company + " and hired " + str(self.hired_students) + " students so far."

    def hire(self):
        self.hired_students += 1

class Corsac(object):

    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.mentors = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            return "not a student"
    
    def add_mentor(self, mentor):
        if isinstance(mentor, Mentor):
            self.mentors.append(mentor)
        else:
            return "not a mentor"

    def info(self):
        return "The Corsac " + self.class_name + " class has " + str(len(self.students)) + " students and " + str(len(self.mentors)) + " mentors."


person_one = Sponsor("Jane Doe", 30, "female","Google")
person_one.hire()
person_two = Mentor("Rad", 30, "male", "senior")
corsac = Corsac("Badcat")

print(corsac.info())
corsac.add_student(person_one)
print(corsac.info())

print(corsac.add_student(person_two))

print(person_one.introduce())
print(person_one.get_goal())
print(person_two.get_goal())

people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person()
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student()
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor()
people.append(mentor)
sponsor = Sponsor()
people.append(sponsor)
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for member in people:
    print(member.introduce())
    print(member.get_goal())