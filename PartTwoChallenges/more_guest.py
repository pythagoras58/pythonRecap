"""
You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
    • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
    end of your program, informing people that you found a bigger table.
    • Use insert() to add one new guest to the beginning of your list.
    • Use insert() to add one new guest to the middle of your list.
    • Use append() to add one new guest to the end of your list.
    • Print a new set of invitation messages, one for each person in your list.
"""

guest_list = ['Agya yaw', 'Ruth', 'Pearl']

print(f'The officially invited people are: {guest_list}')
print('====Bigger Table Found=====')

guest_list.insert(0,'Amoah')
guest_list.insert(2,'Danso')
guest_list.append('Randy')

print(f'The invited people are: {guest_list}')