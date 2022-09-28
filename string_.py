str=input('')
n=len(str)
max=1
tt=0
sum=1
for i in range(0,n-1):
    if str[i]==str[i+1]:
        sum+=1
    else :
        if sum>tt:
            tt=sum
            str1=str[i]
            sum=1
        sum=1
if sum>tt:
    tt=sum
    str1=str[n-1]
for i in range(1,tt):
    print(str1)
