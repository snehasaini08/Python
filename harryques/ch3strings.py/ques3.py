#to detect the double space in a program
name="Sneha is a  good girl"
print(name.find("  ")) #it will return -1 if it does not find the double space in the string
print(name.find("is")) #it will return the index of the first character of the word "is"
print(name.find("  "))