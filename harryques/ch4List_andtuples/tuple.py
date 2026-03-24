a= (1,2,3,4,5)
print(a)
#if we want to create a tuple with only one element then we have to put a comma after the element otherwise it will be considered as a string
b = (1,)
print(type(b))
c=(1,45,342,"Shivam",True,5.87)
print(c)

#if we try to change the element of tuble
d=(1,45,342,"Shivam",True,5.87)
d[0]=34 #it will give an error because tuple is immutable in python
print(d)