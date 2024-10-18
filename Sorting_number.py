# Sorting number 
# recive number form input > collect in number list > sorting number in list

# declare list name > member is null 
number = []

# recive input number of member in number_list
numMember = int(input("enter number of member in list: "))

for count in range(numMember):
    # adding number form numMember variable
    number.append(int(input("Enter number: ")))
 
# show member in number list
print("before sorting number in list: \n", number)

# sorting member in list > AESC is Default
number.sort()
print("after sorting number in list: \n", number)

# sorting member in list > DESC
number.reverse()
print("Sorting member in number list > DESC: \n", number)