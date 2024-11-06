'''In task_b.py write a program which:
- asks users to enter a numerical grade between 0 – 100
- converts the grade to a letter:
A = 80 - 100
B = 60 – 79
C = 50 -59
D = 40 – 49
F = 0 – 39
- And prints out the grade in the format:
Your grade is: A
If the user enters a non-numerical value, your program should instead print:
Error: Please enter a number
And exit
If the user enters a number outside of the permitted value, your program should print:
Error: Grades must be between 0 and 100
And exit'''

grade = input("what is your grade?(please enter 0 and 100)")

if grade.isdigit():
    grade2 =  float(grade)
    if grade2 >= 80 and grade2 <= 100:
        print("Your grade is: A")
    elif grade2 >= 60 and grade2 <= 79:
        print("Your grade is: B")
    elif grade2 >= 50 and grade2 <= 59:
        print("Your grade is: C")
    elif grade2 >= 40 and grade2 <= 49:
        print("Your grade is: D")
    elif grade2 >= 0 and grade2 <= 39:
        print("Your grade is: F")
    else:
        print("Error: Grades must be between 0 and 100")
else:
    print("Error: Please enter a number")
