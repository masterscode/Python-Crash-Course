#a list is a collection which is ordered and changeable. allows duplicate members

#create list

numbers = [2,3,4,5,6,77,8,5]
fruits = ['apples', 'oranges', 'grapes', 'pears']
#use constructor
'''
anotherNumbers = list((2,3,4,5,6,77,8,5))
print(anotherNumbers)
'''

# print(len(fruits))

'''append or add to list'''
fruits.append('mangoes')
# print(fruits)

'''remove from list'''
fruits.remove('grapes')
print(fruits)

'''insert into position'''
fruits.insert(len(fruits), 'strawberry')
print(fruits)
