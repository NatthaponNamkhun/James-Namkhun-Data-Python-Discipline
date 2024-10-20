#  Group of Even and Odd number
numbers = []
numOdd = []
numEven =  []

# create input
numMember = int(input("Enter number of member: ")) 

for i in range(numMember):
    # input for adding member value in list
    member = int(input(f"Member {i + 1}: "))
    numbers.append(member)  # adding member to numbers list
    if member % 2 == 0:  # Group by 
        numEven.append(member)
    else:
        numOdd.append(member)

# show result
print("List of numbers: \n", numbers)

# sorting data
numEven.sort()
print("Even number list: \n", numEven)
numOdd.sort()
print("Odd number list: \n", numOdd)
