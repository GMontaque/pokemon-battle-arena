import re
import random


class Player:
    '''create the player class'''
    def __init__(self, **kwargs):
        # name of the player
        self.name = kwargs["name"]
        # if player is human or computer
        self.is_human = kwargs["is_human"]
        # stores the pokemon picked for each player
        self.battle_pokemon = {}

    def pick_pokemon(self):
        '''players are asked to pick 3 pokemon they wish to fight with '''
        if self.is_human:
            # loops till member chooses 3 pokemon
            while len(self.battle_pokemon) < 3:

                print("Please choose from the follow pokemon Squirtle, "
                      "Charmander or Bulbasaur")

                # user inputs pokemon name and value is checked
                while True:
                    try:
                        # input pokemon name
                        pokemon_name = input("Which pokemon would you like "
                                             "to review: ").lower()
                        # checks for no value
                        if not pokemon_name:
                            raise ValueError("Proffessor Oak: Oops doesn't "
                                             "seem like you choose a pokemon, "
                                             "please try again")
                        # checks for incorrect value format
                        elif not re.match("^[A-Za-z]+$", pokemon_name):
                            raise ValueError("Proffessor Oak: Oops don't "
                                             "think i've heard of that pokemon"
                                             ", please try again")
                            ''' checks input matches pokemon name against
                               pokedex dicitionary
                            '''
                        elif not pokedex.get(pokemon_name, None):
                            raise ValueError("Proffessor Oak: Oops thats not "
                                             "one of the pokemon you can "
                                             " choose, please try again")
                        else:
                            # once user enters a correct value, exits loop
                            break
                    except ValueError as e:
                        print(f"{e}")

                ''' Display the pokemon details i.e description,
                pokemon type and attacks
                '''
                print("-----------------------------------------")
                # Pokemon Name
                print(f"Name: {pokemon_name.capitalize()}")

                # description
                print(f"Description: {pokemon_name} is a "
                      f"{pokedex[pokemon_name]['description']}")

                # pokemon type
                print(f"Pokemon Type: "
                      f"{pokedex[pokemon_name]['pokemon_type']}")

                # pokemon attack list and values
                print(f"Attack Moves: {pokedex[pokemon_name]['attacks']}")

                print("-----------------------------------------")

                ''' Asks the user if they want
                to add the pokemon to their battle pack
                '''
                while True:
                    try:
                        # input players choice on pokemon
                        picking_pokemon = input(f"Do you want to add "
                                                f"{pokemon_name} to your "
                                                "battle party? (yes/no): ")
                        # checks for no value
                        if not picking_pokemon:
                            raise ValueError("Proffessor Oak: Oops you didn't "
                                             "respond, please try again")
                        # checks for incorrect value and format
                        elif picking_pokemon.lower() not in ['yes', 'no']:
                            raise ValueError("Proffessor Oak: Sorry but i need"
                                             " a 'YES' or 'NO' answer")
                        else:
                            # once user enters a correct value, resets loop
                            break
                    except ValueError as e:
                        print(f"{e}")

                '''
                checks user response is yes, also that pokemon_name can
                be found in pokedex and
                pokemon has not already been added to battle_pokemon
                '''
                if (picking_pokemon.lower() == "yes" and
                   pokemon_name in pokedex and pokemon_name
                   not in self.battle_pokemon):
                    # get the key in the pokedex dicitionary
                    self.selected_pokemon_name = pokedex[pokemon_name]
                    # adds selected pokemon to battle_pokemon as dictionary
                    self.battle_pokemon[pokemon_name] = (
                        self.selected_pokemon_name)
                    # confirmation to user pokemon added
                    print(f"{pokemon_name} added to battle party.")
                elif picking_pokemon.lower() == "no":
                    # if user inputs no, function loops back to beginning
                    print(f"Proffessor Oak: No worries, {pokemon_name} "
                          "was not added to your battle party.")
                else:
                    # if user inputs no, function loops back to beginning
                    print(f"Proffessor Oak: looks like you already addeds, "
                          f"{pokemon_name} why not try another pokemon.")
        else:
            # loops until 3 pokemon selected
            while len(self.battle_pokemon) < 3:
                # selects a random pokemon in pokedex
                random_pokemon = random.choice(list(pokedex.keys()))
                ''' checks pokemon is not in battle_pokemon
                before added new value
                '''
                if random_pokemon not in self.battle_pokemon:
                    # adds pokemon
                    self.battle_pokemon[random_pokemon] = (
                        pokedex[random_pokemon])
        return self.battle_pokemon

# pokedex dicitionary stores all the pokemon the user can choose from


pokedex = {
    "squirtle": {"name": "squirtle",
                 "description": "This Tiny Turtle Pokémon draws its"
                 " long neck into its shell to launch incredible "
                 "Water attacks with amazing range and accuracy. "
                 "The blasts can be quite powerful."
                 "to make jokes and enjoys a good swin",
                 "pokemon_type": "water",
                 "health": 240,
                 "attacks": {"Water Gun": 20, "Aqua Tail": 30,
                             "Surf": 40, "Whirlpool": 50}},
    "charmander": {"name": "charmander",
                   "description": "A flame burns on the tip of its "
                   "tail from birth. It is said that a Charmander "
                   "dies if its flame ever goes out.",
                   "pokemon_type": "fire",
                   "health": 240,
                   "attacks": {"Ember": 20, "Fire Fang": 30,
                               "Flamethrower": 40, "Inferno": 50}},
    "bulbasaur": {"name": "bulbasaur",
                  "description": "It bears the seed of a plant on "
                  "its back from birth. The seed slowly develops. "
                  "Researchers are unsure whether to classify "
                  "Bulbasaur as a plant or animal. Bulbasaur are "
                  "extremely tough and very difficult to capture "
                  "in the wild.",
                  "pokemon_type": "grass",
                  "health": 240,
                  "attacks": {"Vine Whip": 20, "Razor Leaf": 30,
                              "Seed Bomb": 40, "Leaf Storm": 50}},
    "grimer": {"name": "grimer",
               "description": "A Sludge Pokémon. Born from sludge, these "
               "Pokémon specialize in Sludge attacks.",
               "pokemon_type": "posion",
               "health": 240,
               "attacks": {"Poison Gas": 20, "Sludge": 30, "Gunk Shot": 40,
                           "Acid Spray": 50}},
    "pikachu": {"name": "pikachu",
                "description": "the Mouse Pokémon. It can generate electric "
                "attacks from the electric pouches located in both "
                "of its cheeks",
                "pokemon_type": "Electric",
                "health": 240,
                "attacks": {"Thunder Shock": 20, "Thunder Wave": 30,
                            "ThunderBolt": 40, "Electro Ball": 50}},
    "abra": {"name": "abra",
             "description": "a Psychic Power Pokémon. It sleeps eighteen "
                            "hours a day, but employs telekinesis even while "
                            "sleeping.",
             "pokemon_type": "psychic",
             "health": 240,
             "attacks": {"Confusion": 20, "Psychic": 30, "Dream Eater": 40,
                         "Guard Split": 50}},
    "rattata": {"name": "rattata",
                "description": "A Forest Pokémon, Rattata. It likes cheese, "
                "nuts, fruits, and berries. It also comes out into open fields"
                " to steal food from stupid travelers",
                "pokemon_type": "normal",
                "health": 240,
                "attacks": {"Tackle": 20, "Quick Attack": 30, "Take Down": 40,
                            "Facade": 50}},
    "sandshrew": {"name": "sandshrew",
                  "description": "the Mouse Pokémon. Sandshrew hates moisture"
                  " and lives in holes it digs in dry places. It protects "
                  "itself by curling into a ball.",
                  "pokemon_type": "ground",
                  "health": 240,
                  "attacks": {"Sand Attack": 20, "Bulldoze": 30,
                              "Mud Slap": 40, "Dig": 50}},
    "Hitmonlee": {"name": "Hitmonlee",
                  "description": "the Kicking Pokémon. This nimble Pokémon "
                  "launches lethal kicks from almost any position.",
                  "pokemon_type": "fighting",
                  "health": 240,
                  "attacks": {"Low sweep": 20, "Double kick": 30,
                              "Sucker punch": 40, "Axe kick": 50}},
    "dratini": {"name": "dratini",
                "description": "the Dragon Pokémon. Dratini sheds its skin as "
                "it grows, often doing so while hidden behind large "
                "powerful waterfalls.",
                "pokemon_type": "dragon",
                "health": 240,
                "attacks": {"Twister": 20, "Dragon tail": 30,
                            "Dragon rush": 40, "Outrage": 50}}
}
