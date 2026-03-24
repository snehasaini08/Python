#Check if the list is sorted or not
a=[12,13,14,15,16]
for i in range(len(a)-1) :  #Because in this a[i]=4,thena[i+1]=5 (that is out of the list)
    if a[i] < a[a+1]:
        continue
    else:
        print("Your List is not sorted")
        break
else:
    print("Your list is sorted")    
