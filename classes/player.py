class Player:
    def __init__(self,**kwargs):
        self.name = kwargs["name"]
        self.is_human = kwargs["is_human"]


    def pick_pokemon(self):
        pokemon_picked = []

        while len(pokemon_picked) < 3:

            print("Please choose from the follow pokemon Squirtle, Charmander or Bulbasaur")

            # user inputs pokemon name

            pokemon_name = input("Which pokemon would you like to review: ").lower()

            # Display the pokemon details

            print(f"{pokemon_name} is a {dic[pokemon_name]['description']}")

            print(f"{pokemon_name} is a {dic[pokemon_name]['pokemon_type']} type pokemon")

            print(f"{pokemon_name} has the following attacks {dic[pokemon_name]['attacks']}")

            # Ask the user if they want to add the pokeon to there battle pack

            picking_pokemon = input(f"Do you want to add {pokemon_name} to your battle party? (yes/no): ")

            # If the user wants to add the pokemon it will append it to the battle pack

            if picking_pokemon.lower() == "yes":
                pokemon_picked.append(pokemon_name)
                print(f"{pokemon_name} added to battle party.")
            else:
                print(f"No worries, {pokemon_name} was not added to your battle party.")

        return pokemon_picked

    # def pick_pokemon(self):
    #     print('''
    #     please choose a pokemon numer 0 to 2

    #     [0]: squirtle

    #     [1]: charmander

    #     [2]: bulbasaur
        
    #     ''')
    #     seleceted = -1
    #     while seleceted == -1:
    #         seleceted = int(input("choose a pokemon: "))
        
# ----===========================================================

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
