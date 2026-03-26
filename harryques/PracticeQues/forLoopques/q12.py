#Check if the number is palindrome or not
a = input("String is : ")
b=""
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
if b==a:
    print("Palindrome")
else :
    print("Not a palindrome")        

