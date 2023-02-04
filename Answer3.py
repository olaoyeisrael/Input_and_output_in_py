# Write a Python program to find the sum of two given integers. However, if the sum is 
# between 15 and 20 it will return 20
def sum_of_integer(num1, num2):
    add = num1 + num2
    if 15 <= add <= 20:
        return 20
    else:
        return add
    
# print(sum_of_integer(5,12))

