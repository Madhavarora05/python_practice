#check whether a number is strong number or not
# i.e sum of factorial of each digit of number is equal to number 
x=input('Enter a Number:')
y=1
z=0
for i in x:
    i=int(i)
    for j in range(i,1,-1):
        y=y*j
    z=z+y
    y=1
if z==int(x):
    print("strong number")
else:
    print("not a strong number")