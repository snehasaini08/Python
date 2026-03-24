#Find the secong greatest number in a list
# l=[12,567,43,235,347,568,45,43,7]

# largest=l[0]
# sec_largest=l[0]

# for i in range(len(l)):
#     if l[i] > largest:
#         largest=l[i]

# print(f"largest element is {largest}" ) 

# for j in range(len(l)):
#     if sec_largest > l[i] and sec_largest != largest :
#         sec_largest = l[i]

# print(f"Second largest element is {sec_largest}")


l= [12,16,13,19,17]

largest = l[0]
sec_largest = l[0]

for i in l:
    if i > largest :
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest=i    

print(f"Second largest element is {sec_largest} and largest {largest}")        
