
students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1}
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies



def counting(x):
        full = 0
        for i in range(len(x)):
                full += (x[i]['candies'])
        return full 

print(counting(students))


def age(y):
        sum = 0
        for i in range(len(y)):
                if (y[i]['candies']) < 5:
                        sum += (students[i]['age'])
        return sum

print(age(students))
