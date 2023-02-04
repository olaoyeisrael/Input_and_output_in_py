# Write a program to accept a number from 1 to 7 and display the name of the day like 1
# for Sunday , 2 for Monday and so on.

dict = {1:"Sunday", 2: "Monday", 3: "Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Sturday"}

num = int(input("Input the number of the day you will like to see. Note(between 1-7): "))

if num in dict:
    print(num, 'for', dict[num])
else:
    print("An Error Occured: Input a valid number from 1-7.")