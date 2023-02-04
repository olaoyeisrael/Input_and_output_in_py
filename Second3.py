# Create a variable name and add a string with your name Create a variable phoneno and add a
# phone number to it Print: Contact Info
# Print: Name: Your name
# Print: Number: Your phone number
def contactInfo():
    name = input("What is you name? ")
    phoneno = int(input("Input your phone number: "))

    print("Contact Info")
    print("Name:", name)
    print("Number:", str(phoneno))

contactInfo()
