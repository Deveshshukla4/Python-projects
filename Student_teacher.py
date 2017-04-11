pankaj = {
    "name": "Pankaj",
    "homework": [80, 90, 60, 70],
    "quizzes":[90, 80, 90, 70],
    "tests": [60, 60, 70, 80]
}

devesh = {
    "name": "Devesh",
    "homework": [80, 90, 90, 80],
    "quizzes": [90, 90, 90, 100],
    "tests": [60, 55, 70, 80]
}
shivam = {
    "name": [90, 90, 90, 90],
    "homework": [90, 90, 70, 80],
    "quizzes": [80, 80, 90, 60],
    "tests": [80, 80, 90, 100]
}
students = ['pankaj', 'devesh', 'shivam']

def average(numbers): #get average of numbers
    total = sum(numbers)
    t = float(total)/ len(numbers)
    return t

def get_average(student): #get average of student marks
    homework = average(student["homework"])
    quizzes= average(student["quizzes"])
    tests= average(student["tests"])
    home = homework * 0.1
    quiz = quizzes * 0.3
    test = tests * 0.6
    return home + quiz + test

def get_letter_grade(score): #grade of student
    if score >=90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"

get_letter_grade(get_average(pankaj))

def get_class_average(students): #get the class average
    results =[]
    for student in students:
        results.append(get_average(student))
    return average(results)

students =[pankaj, devesh, shivam]
print "Class Average " +  str(get_class_average(students))
print "Class Grade " + str(get_letter_grade(get_class_average(students)))