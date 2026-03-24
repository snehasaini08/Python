letter = '''Dear <|NAME|>,\n\nYou are selected!\n\nOn <|DATE|>'''
print(letter.replace("<|NAME|>","Sneha").replace("<|DATE|>","20th June 2024")) #We can use it as a chain