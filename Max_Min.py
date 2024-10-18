# find max and min number in numbers list 
# declare number list
numbers = []

# Create input for recive number of member in list
numMember = int(input("Enter number of member in list: "))

for i in range(numMember):
    member = int(input("Enter member value in numbers list: "))  # recive value to list form input
    numbers.append(member)
    
print("show member in numbers list: \n", numbers)

# Sorting member in list > DESC
numbers.sort()
numbers.reverse()
print("Sorting member in numbers list: \n", numbers)

# find max value in numbers list
print("Maximum value in numbers list: ", max(numbers))

# find min value in numbers list
print("Minimum value in numbers list: ", min(numbers))