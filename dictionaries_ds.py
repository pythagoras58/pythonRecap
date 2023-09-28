player_numbers = {
    "Messi": 10,
    "Ronaldo": 7,
    "Neymar": 11,
    "Ramos": 4,
    "Silva": 2
}

free_agents = dict({"De Gea": 1, "Mamoudu": 2})

print(f"Dictionary of Players: {player_numbers}")
print(f'Type of : {type(free_agents)}')
print(f'Type of : {type(player_numbers)}')

#  operations and methods
print(f'Messi is number : {player_numbers["Messi"]}')
print(f'Neymar is number : {player_numbers.get("Neymar")}')

fruit_price = {"Apple":[5,4,3], "Banana": 4}
print(f'Apple List: {fruit_price["Apple"][1]}')

#  methods
fruit_price["Banana"] = 10 # update the value of a dictionary
print(fruit_price)

# add an item to the dictionary
fruit_price["Orange"] = 40
print(fruit_price)


# delete or remove an item
del fruit_price["Orange"]
print(fruit_price)