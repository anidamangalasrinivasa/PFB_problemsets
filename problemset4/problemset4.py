#!/usr/bin/env python3

#Problem2
taxa_string='sapiens : erectus : neanderthalensis'
print(taxa_string)
#types of data- splitting and making a list from a string
taxa_list=taxa_string.split(sep=':')
print(taxa_list)
print(taxa_list[1])
print(type(taxa_string))
print(type(taxa_list))
#sorting using sorted function and adding a key
taxa_list_sorted=sorted(taxa_list)
taxa_list_sorted_len=sorted(taxa_list, key=len)
print(f'sorted alphabetically: {taxa_list_sorted}, sorted by length: {taxa_list_sorted_len}')

#problem4
#while loops: print 1-100; add a cumulative sum of each number per loop

count=1
sum=0

while count<101:
    print(count)
    sum+=count
    count+=1
print(f"Done with loop and the total sum is {sum}")

#problem5
#factorial of 10 calculation: 10*9*8...*1

count=10
factorial=1

while count>0:
    factorial*=count
    count-=1
print(f'Done with loop and 10!={factorial}')

#problem6
#for loop to print even elements of the list
numbers=[101,2,15,22,95,33,2,27,72,15,52]

for number in numbers:
    if number%2==0:
        print(number)

#problem7
#sort and cumulative sum for odd and even values
sum_e=0
sum_o=0

numbers_sorted=sorted(numbers)

for number in numbers_sorted:
    if number%2==0:
        sum_e+=number
    else:
        sum_o+=number

print(f'Sum of even numbers: {sum_e:>2}\nSum of odd numbers: {sum_o:>2}')

#problem8
#range

for n in range(100):
    print(n+1)

#problem9
#list comprehension

list3=[x for x in range(100)]
list4=[x for x in range(1,101)]

for number in list3:
    print(number)

for number in list4:
    print(number)

#problem10+11+12
#user input for min and max value; list comprehension; add to list only if odd

import sys

min=int(sys.argv[1])
max=int(sys.argv[2])

list5=[x for x in range(min,max) if x%2!=0]

print(list5)

#problem13+14
#for loop with printing length and sequence separated by a tab

data1=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
count=0

for data in data1:
    print(f'{count:<2}{len(data):>2} {data}')
    count+=1

data2=sorted(data1, key=len, reverse=True)

for data in data2:
    print(f'{data:<2}')