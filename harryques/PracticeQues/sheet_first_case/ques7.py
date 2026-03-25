#Q7. Write a program to calculate the factorial of a number using a loop. 
n=int(input("Enter number: "))
fact=1
for i in range(1,n+1) :
    fact=fact*i
print(f"Factorial is : {fact}")    
     
