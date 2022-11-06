#Counting number of alphabets,numbers and special symbols in a string
a="A@m73xpiR*#$lov31!@48!loe?>"
char_count=0
num_count=0
sym_count=0
for char in a:
    if char.isalpha():
        char_count+=1
    elif char.isdigit():
        num_count+=1
    else:
        sym_count+=1   
print("Alphabets:-",char_count)
print("Numbers:-",num_count) 
print("Symbols:-",sym_count)