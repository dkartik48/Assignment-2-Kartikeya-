x=int(input(" Please Enter no. of years: "))
tempfinal=0
while (x>0):
    a=12
    c=1
    total=0
    z=0
    temp=0
    while (a>0):
        b=int(input(f"Please enter the average high temperature for month {c}:  "))
        if(b>temp):
            temp=b
        else:
            b=b
        a=a-1
        c=c+1
        total=total+b
    x=x-1
    y=total/12
    print(f"average high temperature for this year: ",y)
    print(f"Highest temperature for this year: ",temp)
    z=z+y
    if(temp>tempfinal):
        tempfinal=temp
    else:
        temp=temp
x=int(input(" Please Enter no. of years again: "))
z=z/x
print("Average Temperature for the whole period: ",z)
print("Highest Temperature for the whole period: ",tempfinal)
    