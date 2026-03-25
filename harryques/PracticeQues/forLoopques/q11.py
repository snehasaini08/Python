#Reverse a string without using the string function
n=input("Enter string: ")
for i in range(len(n)-1,-1,-1):
    print(n[i])
