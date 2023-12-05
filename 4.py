numbers=[4,6,9,27,17,22,12,33,44]
i=0
a=0
while (a<=8):
    for i in range(0,8):
        if(i<8):
            if (numbers[i]>numbers[i+1]):
                x=numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=x
        i=i+1
    a=a+1
print(numbers)