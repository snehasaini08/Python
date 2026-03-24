friends=["Apple","Mango", 5 , 345.67 , False, "sneha", "harry"]
print(friends)

#append method

friends.append("ansh") #it will add the element at the end of the list
print(friends)

#sort method
l1=[5, 2, 9, 1, 3]
l1.sort() #it will sort the list in ascending order
print(l1)

#reverse method
l1.reverse() #it will reverse the list
print(l1)

#insert method
l1.insert(2,3333) #it will insert the element 3333 at index 3
print(l1)

#pop method = will delete element at particular index
'''
l1.pop() #it will remove the last element of the list
print(l1)
'''
'''
l1.pop(2) #it will remove the element at index 2
print(l1)'''
print(l1.pop(3)) #it will remove the element at index 3
print(l1)

'''
or
value = l1.pop(3)    #it will remove the element at index 3 and store it in the variable value
print(value)    #it will print the value which is removed from the list
print(l1)    #it will print the list after removing the element at index 3

'''

#remove method = will remove the element by value
l1.remove(3333) #it will remove the element 3333 from the list
print(l1)


