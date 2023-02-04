# Write a program to accept percentage from the user and display the grade according to
# the following criteria:
# Marks Grade
# > 90 A
# > 80 and <= 90 B
# >= 60 and <= 80 C
# below 60 D

data = int(input("What is the percentage?"))

if data > 90:
    print("Grade: A")
elif 80 < data <=90:
    print("Grade: B")
elif 60 <= data <= 80:
    print("Grade: C")
else:
    print("Grade: D")
