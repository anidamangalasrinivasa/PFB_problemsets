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
if var4>50:
    print("it is larger than 50")
    if var4%3==0:
        print("divisible by 3")
        if var4>50:
            print("divisible by 3 and larger than 50")
else:
    print("it is lower or equal to 50")
