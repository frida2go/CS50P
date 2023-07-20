inpu = input("camelCase: ")
str_u = ""
for i in range (len(inpu)):
    if inpu[i].isupper():
                str_u+="_"
    str_u+=inpu[i]
print (f"snake_case: {str_u.lower()}")