a=int(input("Your daily intake of calories during a diet: "))
b=int(input("Please enter Average daily percentage Increase/Decrease.(IF decrese, please enter the value in -ve): "))
c=int(input("Pleae Enter the number of day: "))
x=1
if b>0 or b==0:
    while (x<=c):
        if(a>=1200):
            print(f"Day {x}: ",a)
            a=a+(a*(b/100))
            x=x+1
        else:
            print("Calorie intake is less than 1200")
            break
            

else:
    while (x<=c):
        if (a>=1200):
            print(f"Day {x}: ",a)
            a=a-(a*(b/100))
            x=x+1
        else:
            print("Calorie intake is less than 1200")
            break
