#Number is prime or not
n=int(input("Enter number: "))
cnt=0
for i in range(2,n): #Condition can also be 1,n+1 par yha 1 aur n ko check karne ki zrt he nhi hai
    if(n%i==0):
        cnt=cnt+1
if cnt==0:
    print("Prime Number")  
else:
    print("Not a prime number")          
