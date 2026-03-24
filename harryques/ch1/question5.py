import os

# Select the directory whose content you want to list
directory_path = "/"   # change this to your directory

# use the os module to list the directory path
contents = os.listdir(directory_path)

# Print the contents of the directory
print("Contents :")
