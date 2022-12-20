#print a dict in tale format,inputing keys and values from users
#dict format={1:[a,b],2:[c,d]}
keys=input("Enter Keys in comma seperated format: ").split(",")
d={}
for i in range(len(keys)):
    x=input("Enter 1st list of value(sep by comma): ").split(",")
    d[keys[i]]=x
print(d)
print("Answer in tabular form is: ")
for i in zip(*(([key]+(val) for key,val in d.items()))):
    print(*i)