#!/usr/bin/env python3
import sys

var1=int(sys.argv[1])

print("You are testing", var1)

#3 and 4. testing pos or neg or zero
if var1>0:
    print("It is positive")
elif var1==0:
    print("it is zero")
else:
    print("it is negative")

#5. nested

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

