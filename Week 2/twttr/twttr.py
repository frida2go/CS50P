inpu = input("Input: ")
list_vowels = ["a","e","i","o","u"]
str_without_vowels = ""
for i in range(len(inpu)):
    if inpu[i].lower() not in list_vowels:
        str_without_vowels += inpu[i]

print(f"Output: {str_without_vowels}")
