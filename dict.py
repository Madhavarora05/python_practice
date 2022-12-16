#printing dict in format(x:x*x)
n=int(input("Enter value of n: "))
d={}
for i in range(1,n+1):
    d[i]=i**2
print(d)
