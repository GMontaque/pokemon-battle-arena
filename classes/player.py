import re

class Player:
    '''create the player class'''
    def __init__(self,**kwargs):
        self.name = kwargs["name"]
        self.is_human = kwargs["is_human"]


    def pick_pokemon(self):
        '''players are asked to pick 3 pokemon they wish to fight with '''
        # stores the pokemon picked for each player
        pokemon_picked = []

        # loops till member chooses 3 pokemon
        while len(pokemon_picked) < 3:

            print("Please choose from the follow pokemon Squirtle, Charmander or Bulbasaur")

            # user inputs pokemon name and value is checked
            pokemon_name_input = True
            while pokemon_name_input:
                try:
                    # input pokemon name
                    pokemon_name = input("Which pokemon would you like to review: ").lower()
                    # checks for no value
                    if not pokemon_name:
                        raise ValueError("Proffessor Oak: Oops doesn't seen like you choose a pokemon, please try again")
                    # checks for incorrect value format
                    elif not re.match("^[A-Za-z]+$", pokemon_name):
                        raise ValueError("Proffessor Oak: Oops don't think i've heard of that pokemon, please try again")
                    # checks input matches pokemon names in dicitionary 
                    elif not dic.get(pokemon_name, None):
                        raise ValueError("Proffessor Oak: Oops thats not one of the pokemon you can choose, please try again")
                    else:
                        # once user enters a correct value, resets loop
                        pokemon_name_input = False    
                except ValueError as e:
                    print(f"{e}")

            # Display the pokemon details i.e description, pokemon type and attacks

            print(f"{pokemon_name} is a {dic[pokemon_name]['description']}")

            print(f"{pokemon_name} is a {dic[pokemon_name]['pokemon_type']} type pokemon")

            print(f"{pokemon_name} has the following attacks {dic[pokemon_name]['attacks']}")

            # Asks the user if they want to add the pokemon to there battle pack

            picking_pokemon = input(f"Do you want to add {pokemon_name} to your battle party? (yes/no): ")

            # If the user selects "yes" it will add the pokemon to the battle pack
            if picking_pokemon.lower() == "yes":
                pokemon_picked.append(pokemon_name)
                print(f"{pokemon_name} added to battle party.")
            else:
                # if user inputs no, function loops back to beginning
                print(f"No worries, {pokemon_name} was not added to your battle party.")

        return pokemon_picked

# ----===========================================================
# dictionary of all the pokemon user can choose
dic = {
    "squirtle":{"description":"turtle like pokemon that likes to make jokes and enjoys a good swin",
    "pokemon_type":"water",
    "attacks":{"s1":20,"s2":30,"s3":40,"s4":50}},

    "charmander":{"description":"fire like pokemon that likes can have a temper so be careful not to anger",
    "pokemon_type":"fire",
    "attacks":{"c1":20,"c2":30,"c3":40,"c4":50}},

    "bulbasaur":{"description":"green type pokemon that can be found in the surroudning forests enjoing the sun",
    "pokemon_type":"earth",
    "attacks":{"b1":20,"b2":30,"b3":40,"b4":50}}
}

# ----===========================================================
