#Finding smallest from user given numbers using list:
n=int(input("Total Number of terms= "))
list1=[]
for i in range(1,n+1):
    item=int(input(f"Enter {i} number: "))
    list1.append(item)
print(min(list1))
