# import random
# num=random.randint(1,10)
# print(num)
# guess=int(input("Guess  your number between 1 to 10: "))
# if num==guess:
#     print("Yayy,you are right")
# else:
#     print("OOpss, You are wrong")    

import random
num=random.randint(1,10)
print(num)
tries=0

while True:
    guess=int(input("Guess  your number between 1 to 10: "))

    if num==guess :
       tries+=1
       print(f"Right guess,the number is {tries} tries")
       break
    elif num < guess :
         print("Go lower")
    elif num>guess :
        print("Go higher")
        tries+=1
    else:
        tries+=1
        print("Sorry you are wrong")         



 
