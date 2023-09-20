"""
    List for data collection.
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f'bicycle list: {bicycles}')

for i in bicycles:
    print(i.title())


## Modification: removals and inclusion for lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'List of Arrays : {motorcycles}')

motorcycles.append('tata')
print(f'New List of Arrays : {motorcycles}')

# insert at a location
motorcycles.insert(0, 'Corrido')
print(f'New List of Arrays : {motorcycles}')

# remove an item from a list
del motorcycles[3]
print(f'New List of Arrays - Del : {motorcycles}')

popped_list = motorcycles.pop()
print(f'New List of Arrays - Pop : {popped_list}')

#Removing an Item by Value
motorcycles_rem = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles_rem.remove('ducati')
print(motorcycles_rem)

