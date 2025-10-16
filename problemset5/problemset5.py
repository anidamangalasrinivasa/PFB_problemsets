#!/usr/bin/env python3

#1-6
favorites={'book':'Genes in Conflict','song':'Behag varnam','tree':'Weeping willow'}
print(favorites['book'])

fave_book='book'
print(favorites[fave_book])

print(favorites['tree'])

favorites['organism']='viruses'
fave_org='organism'
print(favorites[fave_org])

for things in favorites:
    print(things,':',favorites[things])

#7-8

keys_=favorites.keys()
input1=input(f'Choose a key:{keys_} ')

if input1 in favorites:
    print(f'Favorite {input1} is {favorites[input1]}')

#9
favorites['organism']='snails'
input2=input(f'Enter a favorite organism: ')

favorites['organism']=str(input2)
print(f'New favorite organism is {favorites['organism']}')