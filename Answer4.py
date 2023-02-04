# Write a Python program to print a specified list after removing the 0th, 4th and 5th
# elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def deleteFromAList(arr):
    res = []
    for i in range(len(arr)):
        
        if i == 0 or i == 4 or i == 5:
            continue
        else:
            res.append(arr[i])
    return res


sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(deleteFromAList(sample))
