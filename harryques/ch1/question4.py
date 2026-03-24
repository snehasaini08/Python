import os

# Specify the directory path
path = "/"   # change this to your directory

# Get the list of contents
contents = os.listdir(path)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)