a=int(input("Enter the number: "))
rev=0
copy=a
while a>0:
    rev=rev*10+a%10
    a=a//10
if copy==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")    

       

