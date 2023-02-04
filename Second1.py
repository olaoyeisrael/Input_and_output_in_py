# ● Ask user for the name of the city they grew up in
# ● Ask user for their pet’s name
# ● Print: Your band name could be (a combination of the city and pet name using
# concatenation)

# Band Name Generator
def bandNameGEnerator():
    nameOfCity = input("Enter the city you grew up: ")
    petName = input("Enter your pet name: ")

    print("Your band name could be " +nameOfCity + petName)

bandNameGEnerator()
