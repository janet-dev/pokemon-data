"""
Retrieve multiple Pokemon and save their names and moves to a file.
Use a list to store 6 Pokemon IDs.
Then in a 'for' loop call the API to retrieve the data for each Pokemon.
Save their names and moves into a file called 'pokemon.txt'
"""

import requests

pokemon_ids = []  # initialise the Pokemon ID list

"""
The 'try' block lets you test a block of code for errors.
The 'except' block lets you handle the error.
"""
try:
    print('Please choose 6 First Generation Pokemon IDs (1-151)')
    for i in range(0, 6):
        # range is 0-6, but not including 6!
        retrieve = int(input('Type in your Pokemon ID: '))
        if 0 < retrieve < 152:
            pokemon_ids.append(retrieve)
            # list.append(element) i.e. add 'retrieve' to 'pokemon_ids' list
        else:
            print('Invalid ID')
except ValueError:
    print('Invalid ID')

for pokemon in pokemon_ids:
    # get info on the 6 pokemon
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)
    response = requests.get(url)
    pokemon = response.json()
    # used .json() to transfer data as text
    ident = str(pokemon['id'])  # id was an integer!
    name = pokemon['name']

    moves = pokemon['moves']
    for move in moves:
        move_list = move['move']['name']
        poke_list = ident + ' ' + name + ' ' + move_list + '\n'
        # can only do this with strings
        # .write() will only except 1 argument, so had to do
        # styling here for command below

        # used 'a' for append, instead of overwrite 'w+'
        with open('pokemon.txt', 'a') as pokemon_file:
            pokemon_file.write(poke_list)
print('Open pokemon.txt to see what Pokemon data you have.')

"""
Sample of pokemon.txt file:

------------------------------------------------
List of Pokemon with their IDs, names and moves:
------------------------------------------------
Id|Pokemon | Skill
-------------------------
1 bulbasaur grassy-terrain
1 bulbasaur confide
2 ivysaur swords-dance
2 ivysaur cut

"""
