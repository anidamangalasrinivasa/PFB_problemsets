#!/usr/bin/env python3

var1=25
if var1==25:
    print("aye aye captain")
else:
    print("oh no, not true")

var2=-15
if var2>0 :
    print("Positive")
elif var2==0:
    print("it's zero")
else:
    print("Negative")


var3=24
if var3<50:
    print("Smaller than 50")
    if var3%2==0:
        print("it is an even number")
        if var3<50:
            print("it is an even number smaller than 50")


var4=50
if var1>0:
    print("test 2: it is positive")
    if var1<50:
        print(var1,"is lower than 50")
        if var1%2==0:
            print(var1, 'is even and lower than 50')
        else:
            print(var1,'is odd and lower than 50')
    elif var1>50:
        print(var1,'is larger than 50')
        if var1%3==0:
            print(var1, 'is larger than 50 and divisible by 3')
        else:
            print(var1, 'is larger than 50 but not divisible by 3')
    else:
        print(var1, 'is probably 50')
else:
    print(var1, 'is negative')
