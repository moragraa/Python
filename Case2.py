Scant = int(input('Insert the amount of grades you want to calificate: '))
i = 0

while i < Scant:
    s_grade = int(input('Type the grade of student %s: ' % (i + 1)))
    if s_grade > 100:
        print('Error')
    elif s_grade >= 91:
        print('The student: ', (i+1), ' got an A, and pass the course')
    elif 71 <= s_grade <= 90:
        print('The student: ', (i+1), ' got a B, and pass the course')
    elif 61 <= s_grade < 70:
        print('The student: ', (i+1), ' got a C, and not pass the course')
    elif 51 <= s_grade <= 60:
        print('The student: ', (i + 1), ' got a D, and not pass the course')
    if 1 <= s_grade <= 50:
        print('The student: ', (i + 1), ' got a F, and not pass the course')
    i = i + 1