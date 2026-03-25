marks={
    "Sneha":100,
    "Shubham":56,
    "Rohan":23,
    0:"Harry"
}


#items method : returns a list of key value tuples
print(marks.items())

#keys method: returns keys
print(marks.keys())

#values method: return value
print(marks.values())

#update method: update the existing dictionary
marks.update({"Harry":23,"Riya":100})
print(marks)

#.get method
print(marks.get("Sneha2")) #This prints None
print(marks["Sneha2"])#This prints error
