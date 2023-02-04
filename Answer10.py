# Define a function in python that accepts 3 values and returns the maximum of three
# numbers.
firstNum = int(input("Input first number: "))
SecondNum = int(input("Input second number: "))
ThirdNum = int(input("Input third number: "))

def maxNum(firstNum, SecondNum, ThirdNum):
    maxiNum = max(firstNum, SecondNum, ThirdNum)
    return "Maximum number is " + str(maxiNum)


    
print(maxNum(firstNum, SecondNum, ThirdNum))

