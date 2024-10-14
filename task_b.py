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

grade = int(input("what is your grade?(please enter 0 and 100)"))

if grade >= 80 and grade <= 100:
    print("your grade is A")
elif grade >= 60 and grade <= 79:
    print("your grade is B")
elif grade >= 50 and grade <= 59:
    print("your grade is C")
elif grade >= 40 and grade <= 49:
    print("your grade is D")
elif grade >= 0 and grade <= 39:
    print("your grade is E")
else:
    print("Grades must be between 0 and 100")