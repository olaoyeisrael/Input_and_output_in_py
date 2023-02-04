# ● Ask user for their favorite color
# ● Ask user for their month of birth (The number)
# ● Ask user for their pet’s name
# ● Combine all these using string concatenation to form the password e.g. (Bruno12blue or
# yellowgrumpy5)

# Password Generator 
def passwordGenerator():
    favoriteColor = input("Enter your favorite color here: ")
    birthMonth = input("Enter your month of birth here (the number): ")
    petName = input("Enter your pet's name here: ")
    res = favoriteColor + birthMonth + petName
    print(res)
passwordGenerator()
