students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def overall(x):
        ave = 0
        for i in range(len(x)):
                ave += (x[i]['candies'])
        return ave/len(x)

print(overall(students))


def age(y):
        sum = []
        for i in range(len(y)):
                if (y[i]['candies']) > 4:
                        sum.append(y[i]['name'])
        return sum

print(age(students))