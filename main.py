# Matching greetings
greetings = ["Hi", "Hello", "Morning"]  # i Extract data in list i1 = "Hi"
name = ["Reed", "James"]  # i1 = "Hi" + j Extract data in list j1 = "Reed" == i1 + j1, i1 + j2
result = []  # collect i1 + j1, i1 + j2 > i2 + j1, i2 + j2 > i3 + j1, i3 + j2 > End Loop

# Nomally
for i in greetings:  # i extract data form greetings list
    for j in name:  # j extract data form name list
        result.append(i + j)  # adding data form i + j in result list    
           
print("Normal: ", result)
