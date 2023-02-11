#converting 12 hour format of clock to 24 format
#input 07:05:45PM output 19:05:45
def timeConversion(s):
    if s[-2]=="A":
        if s[0:2]=="12":
            x="00"+s[2:8]
            return x
        else:
            return(s[0:8])
    else:
        if s[0:2]=="12":
            return(s[0:8])
        else:
            x=int(s[0:2])
            x=str(x+12)
            x=x+s[2:8]
            return x
        

s = input()
result = timeConversion(s)
print(result)