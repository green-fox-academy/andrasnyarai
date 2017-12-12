
class Person(object):

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return "Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + "."

    def get_goal(self):
        return "My goal is: Live for the moment!"

class Student(Person):

    def __init__(self,name,age,gender,prev_org,skip_d=0):
        super().__init__(name,age,gender)
        self.prev_org = prev_org
        self.skip_d = skip_d

    def introduce(self):
        return "Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + " from " + self.prev_org + " who skipped " + str(self.skip_d) + " days from the course already."

    def get_goal(self):
        return "Be a junior software developer."

    def skip_days(self,number_of_days):
        self.skip_d += number_of_days

class Mentor(Person):

    def __init__(self,name,age,gender,level):
        super().__init__(name,age,gender)
        if (level == "junior" or level == "intermediate" or level == "senior"):
            self.level = level
        else:
            self.level = "Not defined"

        
    def get_goal(self):
        return "Educate brilliant junior software developers."

    def introduce(self):
        return "Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + " " + self.level + " mentor."

class Sponsor(Person):

    def __init__(self,name,age,gender,company,hired_students=0):
        super().__init__(name,age,gender)
        self.company = company
        self.hired_students = hired_students

    def get_goal(self):
        return "Hire brilliant junior software developers."

    def introduce(self):
        return "Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + " who represents " + self.company + " and hired " + str(self.hired_students) + " students so far."

    def hire(self):
        self.hired_students += 1

class Corsac(object):

    def __init__(self,class_name,):
        self.class_name = class_name
        self.students = []
        self.mentors = []

    def add_student(self,student):
        self.students.append(student)
    
    def add_mentor(self,mentor):
        self.mentors.append(mentor)

    def info(self):
        return "The Corsac " + self.class_name + " class has " + str(len(self.students)) + " students and " + str(len(self.mentors)) + " mentors."
# Create a PallidaClass class that has the following

# fields:
# class_name: the name of the class
# students: a list of Students
# mentors: a list of Mentors
# methods:
# add_student(Student): adds the given Student to students list
# add_mentor(Mentor): adds the given Mentor to mentors list
# info(): prints out "Pallida className class has len(students) students and len(mentors) mentors."
# The PallidaClass class has the following constructors:

# PallidaClass(class_name): beside the given parameter, it sets students and mentors as empty lists

person_one = Sponsor("Jane Doe", 30, "female","Google")
person_one.hire()

corsac = Corsac("Badcat")

print(corsac.info())
corsac.add_student(person_one)
print(corsac.info())

print(person_one.introduce())
print(person_one.get_goal())
