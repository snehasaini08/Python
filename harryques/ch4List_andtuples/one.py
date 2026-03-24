#print positive and negative elements of a list
a=[1,-8,9,-98,-2,-43,-1]
print("Positive elements are: ")
for i in a:
    if i>=0:
        print(i)

print("Negative elements are: ")
for i in a:
    if i<0:
        print(i)