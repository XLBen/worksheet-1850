'''In task_a.py write a program which:
- asks users to enter a day of the week (“Monday”, “Tuesday”, etc)
- allows for users to enter this in any case (“MONDAY”, “Monday”, “monday”, “MOnDaY” should all
be treated the same)
- prints out the corresponding number (Monday = 1, Sunday = 7) in the format:
Monday is day 1
(Note: the name of the day should always be printed in with the first letter capitalised, all other
letters lower case)
- if the day does not exist, print:
Please enter a valid day
And exit'''

inputday = input("enter a day of the week. (such like Monday,tuesday)")
day = inputday.lower()
if day == "monday":
    print("Monday is 1")
elif day == "tuesday":
    print("Tuesday is 2")
elif day == "wednesday":
    print("Wednesday is 3")
elif day == "thursday":
    print("Thursday is 4")
elif day == "friday":
    print("Friday is 5")
elif day == "saturday":
    print("Saturday is 6")
elif day == "sunday":
    print("Sunday is 7")
else:
    print("Please enter a valid day, exit.")


    



