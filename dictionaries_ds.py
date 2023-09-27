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