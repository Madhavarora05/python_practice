#print factorial of a given number like !4=4*3*2*1

x=int(input("Enter your number: "))
print("Factorial of",x,"=",end=' ')
y=1
while x!=1:
	y=y*x
	print(x,"*",end=' ')
	x-=1
print("1 = ",y)
