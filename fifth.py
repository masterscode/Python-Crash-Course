import datetime as Time

# import datetime as date
# print(dir(Time))

#try continue statement

listings = ['amen', 'jane', 'algo', 'patience']


'''
for item in listings:
    if item == 'algo': continue
    print(f'the total number of items in listings are {len(listings)}, and the items in listings are: {item}')
'''

from datetime import date   
datelistings = dir(date)
for d in datelistings:
    print(d)