a="abc456#@!90"
char=0
dig=0
sp_chr=0
for i in a:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        sp_chr+=1    
print(f'''No of digits are : {dig}
No of alpha are : {char}
No ofspecial character are : {sp_chr}
''')            