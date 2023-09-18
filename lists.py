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