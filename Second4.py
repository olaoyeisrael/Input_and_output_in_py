# Tell me about yourself
# Create a variable name and store your name inside it
# Create another variable age and store your age there
# Print: My name is “Your name” and I am “Your age” years old. (Using concatenation)
# Note: Remember to convert the age variable to a string if not you’ll get a TYPE ERROR.


def tellMeAboutYourself():
    print("Tell me about yourself")
    name = input("What is your name?")
    age = int(input("How old are you?"))
    print("My name is " + name + " and I am " + str(age) + " years old.")

tellMeAboutYourself()
