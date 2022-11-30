file = open("error.py", "w")
for i in file:
    line = i.lstrip(' ')
    if '#' == line[0]:
        
