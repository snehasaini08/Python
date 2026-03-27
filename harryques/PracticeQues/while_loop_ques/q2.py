#Accept the number and print the reverse of it
a=int(input("Enter number: "))
rev=0
while a>0: 
    rev=rev*10+a%10
    a=a//10
print(rev)    
