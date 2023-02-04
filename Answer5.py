# Write a python code that prints all odd numbers between 1 and 100 using a while
# statement.
def oddNumber():

    i = 1
    while i <= 100:
        if i % 2 == 1:
            print (i)
        i += 1
   
oddNumber()