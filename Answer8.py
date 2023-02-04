# Create a dictionary for birthdays with a name as the key and a person’s birthday as the
# value i.e birthdays = 
# ● Ask the user for input of name
# ● print out the name of a person whose birthday is stored in the database
# ● if the person’s name is not in the database you should print “I do not have
# birthday information for [name]”
# ● If the name is in the dictionary you should print “[Birthday] is the
# birthday of [name]”

database = {
    'Anita': 'April 22', 
    'Hansel': 'August 3',
    'Israel': 'July 5'

    }
print("Note: Name should begin with a Capital letter")
name = input("Input your name: ")
print(name)
if name in database:
    print(database[name] +" is the birthday of", name+ ".")

else:
    print("I do not have birthday information for "+ name)

