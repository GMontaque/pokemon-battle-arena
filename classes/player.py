import re
import random
import copy
import time
import os
from tabulate import tabulate
from colorama import Fore, Back, Style

# global styling variables
error_colour = Back.RED + Fore.WHITE
reset_styling = Style.RESET_ALL = Style.RESET_ALL
game_notification = Back.BLUE + Fore.WHITE
proffessor_oak = (Style.RESET_ALL + Fore.GREEN + "Proffessor Oak: "
                  + Style.RESET_ALL)


class Player:
    '''create the player class'''
    def __init__(self, **kwargs):
        # name of the player
        self.name = kwargs["name"]
        # stores value if player is human or PC
        self.is_human = kwargs["is_human"]
        # stores the pokemon picked for each player
        self.battle_pokemon = {}

    def pick_pokemon(self):
        '''players are asked to pick 3 pokemon they wish to fight with '''
        # resets all pokemon health to full
        for name, entry in pokedex.items():
            entry['health'] = 240
        # checks if player picking is human
        if self.is_human:
            # loops till member chooses 3 pokemon for battle pack
            while len(self.battle_pokemon) < 3:
                print("-----------------------------------------------------")
                print(game_notification + " Please choose from the follow "
                      + Style.RESET_ALL)
                pokemon_names = [
                    ["Squirtle", "Charmander", "Bulbasaur"],
                    ["Grimer", "Pikachu", "Abra"],
                    ["Rattata", "Sandshrew", "Hitmonlee"],
                    ["Dratini"]
                ]
                # display pokemon player can choose from in a table
                print(tabulate(pokemon_names, tablefmt="double_grid"))

                # user inputs pokemon name and value is checked
                while True:
                    try:
                        # input pokemon name
                        pokemon_name = input(proffessor_oak + "Which pokemon "
                                             "would you like to review: "
                                             ).lower().replace(" ", "")
                        # checks for no value
                        if not pokemon_name:
                            raise ValueError(error_colour + "Proffessor Oak: "
                                             "Oops doesn't seem like you "
                                             "choose a pokemon, please "
                                             "try again" + reset_styling)
                        # checks for incorrect value format
                        elif not re.match("^[A-Za-z]+$", pokemon_name):
                            raise ValueError(error_colour+"Proffessor Oak: "
                                             "Oops don't think i've heard of "
                                             "that pokemon, please try again"
                                             + reset_styling)
                            ''' checks input matches pokemon name against
                               pokedex dicitionary
                            '''
                        elif not pokedex.get(pokemon_name, None):
                            raise ValueError(error_colour+"Proffessor Oak: "
                                             "Oops thats not one of the "
                                             "pokemon you can  choose, "
                                             "please try again"
                                             + reset_styling)

                        # once user enters a correct value, exits loop
                        break
                    except ValueError as e:
                        print(f"{e}")

                ''' Display the pokemon details i.e description,
                pokemon type and attacks
                '''
                print("-----------------------------------------------------")
                # styling for pokemon player card names
                name_tag = Fore.GREEN + "Name:" + Style.RESET_ALL
                description_tag = Fore.GREEN + "Description:" + Style.RESET_ALL
                type_tag = Fore.GREEN + "Pokemon Type:" + Style.RESET_ALL
                attack_moves_tag = (Fore.GREEN + "Attack Moves:"
                                    + Style.RESET_ALL)
                # prints pokemon player card name
                print(f"{name_tag} {pokemon_name.capitalize()}")

                # prints pokemon player card description
                print(f"{description_tag} {pokemon_name} is a "
                      f"{pokedex[pokemon_name]['description']}")

                # prints pokemon player card pokemon type
                print(f"{type_tag} "
                      f"{pokedex[pokemon_name]['pokemon_type']}")
                # prints pokemon player card attacks
                attack_pokemon_list = []
                for i in range(1, 5):
                    attack_pokemon_list.append(pokedex[
                        pokemon_name]['attacks'][i][1])

                # pokemon attack list and values
                print(f"{attack_moves_tag} {', '.join(attack_pokemon_list)}")

                print("-----------------------------------------------------")

                ''' Asks the user if they want
                to add the pokemon to their battle pack
                '''
                while True:
                    try:
                        # inputs asks for a yes or no answer
                        picking_pokemon = input(proffessor_oak
                                                + f"Should I add"
                                                f" {pokemon_name.capitalize()}"
                                                " to your battle pack? "
                                                "(yes/no): "
                                                ).lower().replace(" ", "")
                        # checks for no value
                        if not picking_pokemon:
                            raise ValueError(error_colour+"Proffessor Oak:"
                                             " Oops you didn't respond, "
                                             "please try again"
                                             + reset_styling)
                        # checks for incorrect value and format
                        elif picking_pokemon.lower() not in ['yes', 'no']:
                            raise ValueError(error_colour+"Proffessor Oak: "
                                             "Sorry but i need a 'YES' or "
                                             "'NO' answer" + reset_styling)
                        # once user enters a correct value, resets loop
                        break
                    except ValueError as e:
                        print(f"{e}")

                '''
                checks if user response was yes and also that pokemon_name
                can be found in pokedex and that the
                pokemon has not already been added to battle_pokemon
                '''
                if (picking_pokemon.lower() == "yes" and
                   pokemon_name in pokedex and pokemon_name
                   not in self.battle_pokemon):
                    # get the key in the pokedex dicitionary
                    self.selected_pokemon_name = pokedex[pokemon_name]
                    # adds selected pokemon to battle_pokemon as dictionary
                    self.battle_pokemon[pokemon_name] = (
                        copy.deepcopy(self.selected_pokemon_name))
                    # confirmation to user pokemon added
                    print(game_notification + f" {pokemon_name.capitalize()}"
                          " added to battle party. " + reset_styling)
                    print("-------------------------------------------------"
                          "---")
                elif picking_pokemon.lower() == "no":
                    # if user inputs no, loops back to beginning
                    print(proffessor_oak + "No worries, why not try again")
                    print(game_notification + f" {pokemon_name.capitalize()} "
                          "was not added to your battle party."
                          + reset_styling)
                else:
                    # prints if user has already added pokemon to battle pack
                    print(error_colour + "Proffessor Oak: looks like you "
                          f"already added, {pokemon_name.capitalize()} "
                          "why not try another pokemon." + reset_styling)
            os.system("clear")
        else:
            # PC player choose 3 pokemon
            print(game_notification + f" Player {self.name} is choosing his"
                  " pokemon " + reset_styling)
            # loops until 3 pokemon selected
            while len(self.battle_pokemon) < 3:
                # selects a random pokemon in pokedex
                random_pokemon = random.choice(list(pokedex.keys()))
                ''' checks pokemon is not in battle_pokemon
                before adding a new value
                '''
                if random_pokemon not in self.battle_pokemon:
                    # adds pokemon
                    self.battle_pokemon[random_pokemon] = (
                        copy.deepcopy(pokedex[random_pokemon]))
            time.sleep(3)
            # confimration message PC picked pokemon
            print(game_notification + f" Pokemon selection complete "
                  + reset_styling)
            time.sleep(2)
        return self.battle_pokemon

# pokedex dicitionary stores all the pokemon the user can choose from


pokedex = {
    "squirtle": {"name": "squirtle",
                 "description": "This Tiny Turtle Pokémon draws its"
                 " long neck into its shell to launch incredible "
                 "Water attacks with amazing range and accuracy. "
                 "The\n blasts can be quite powerful."
                 "to make jokes and enjoys a good swin",
                 "pokemon_type": "water",
                 "health": 240,
                 "attacks": {1: ["normal", "Tackle: 10"],
                             2: ["water", "Surf: 20"],
                             3: ["ground", "Mud Shot: 30"],
                             4: ["water", "Hydro Pump: 40"]},
                 "x2_attack": {"grass", "electric"}},
    "charmander": {"name": "charmander",
                   "description": "A flame burns on the tip of its "
                   "tail from birth. It is said that a Charmander "
                   "dies if its flame ever goes out.",
                   "pokemon_type": "fire",
                   "health": 240,
                   "attacks": {1: ["electric", "Thunder Punch: 10"],
                               2: ["fire", "Flamethrower: 20"],
                               3: ["dragon", "Dragon Breath: 30"],
                               4: ["fire", "Overheat: 40"]},
                   "x2_attack": {"water", "ground"}},
    "bulbasaur": {"name": "bulbasaur",
                  "description": "It bears the seed of a plant on "
                  "its back from birth. The seed slowly develops. "
                  "Researchers are unsure whether to classify "
                  "Bulbasaur as a plant or animal. Bulbasaur are "
                  "extremely tough and very difficult to capture "
                  "in the wild.",
                  "pokemon_type": "grass",
                  "health": 240,
                  "attacks": {1: ["normal", "Tackle: 10"],
                              2: ["grass", "Leaf Storm: 20"],
                              3: ["normal", "Body Slam: 30"],
                              4: ["grass", "Solar Bean: 40"]},
                  "x2_attack": {"fire", "ice"}},
    "grimer": {"name": "grimer",
               "description": "A Sludge Pokémon. Born from sludge, these "
               "Pokémon\n specialize in Sludge attacks.",
               "pokemon_type": "posion",
               "health": 240,
               "attacks": {1: ["ground", "Mud Slap: 10"],
                           2: ["posion", "Sludge Bomb: 20"],
                           3: ["ghost", "Shadow Punch: 30"],
                           4: ["posion", "Memento: 40"]},
               "x2_attack": {"ground", "psychic"}},
    "pikachu": {"name": "pikachu",
                "description": "the Mouse Pokémon. It can generate electric "
                "attacks\n from the electric pouches located in both "
                "of its cheeks",
                "pokemon_type": "Electric",
                "health": 240,
                "attacks": {1: ["ground", "dig: 10"],
                            2: ["electric", "Thunder Punch: 20"],
                            3: ["normal", "Quick Attack: 30"],
                            4: ["electric", "Thunder: 40"]},
                "x2_attack": {"ground"}},
    "abra": {"name": "abra",
             "description": "a Psychic Power Pokémon. It sleeps eighteen "
                            "hours a day, but employs telekinesis even while "
                            "sleeping.",
             "pokemon_type": "psychic",
             "health": 240,
             "attacks": {1: ["grass", "Energy Ball: 10"],
                         2: ["psychic", "Dream Eater: 20"],
                         3: ["fighting", "Drain Punch: 30"],
                         4: ["psychic", "Psychic: 40"]},
             "x2_attack": {"ghost", "dark"}},
    "rattata": {"name": "rattata",
                "description": "A Forest Pokémon, Rattata. It likes cheese, "
                "nuts,\n fruits, and berries. It also comes out "
                "into open fields to steal food\n from stupid travelers",
                "pokemon_type": "normal",
                "health": 240,
                "attacks": {1: ["normal", "Quick Attack: 10"],
                            2: ["normal", "Pluck: 20"],
                            3: ["ground", "Dig: 30"],
                            4: ["normal", "Cut: 40"]},
                "x2_attack": {"fighting", "psychic"}},
    "sandshrew": {"name": "sandshrew",
                  "description": "the Mouse Pokémon. Sandshrew hates moisture"
                  " and lives in holes it digs in dry places. It protects "
                  "itself by curling into a ball.",
                  "pokemon_type": "ground",
                  "health": 240,
                  "attacks": {1: ["fighting", "Focus Punch: 10"],
                              2: ["ground", "Sand Tomb: 20"],
                              3: ["bug", "Fury Cutter: 30"],
                              4: ["ground", "Dig: 40"]},
                  "x2_attack": {"water", "grass"}},
    "hitmonlee": {"name": "hitmonlee",
                  "description": "the Kicking Pokémon. This nimble Pokémon "
                  "launches\n lethal kicks from almost any position.",
                  "pokemon_type": "fighting",
                  "health": 240,
                  "attacks": {1: ["ground", "Bulldoze: 10"],
                              2: ["fighting", "Focus Blast: 20"],
                              3: ["normal", "Body Slam: 30"],
                              4: ["fighting", "Close Combat: 40"]},
                  "x2_attack": {"psychic", "flying"}},
    "dratini": {"name": "dratini",
                "description": "the Dragon Pokémon. Dratini sheds its skin as "
                "it\n grows, often doing so while hidden behind large "
                "powerful waterfalls.",
                "pokemon_type": "dragon",
                "health": 240,
                "attacks": {1: ["water", "Chilling Water: 10"],
                            2: ["dragon", "Draco Meteor: 20"],
                            3: ["ice", "Ice Beam: 30"],
                            4: ["dragon", "Outrage: 40"]},
                "x2_attack": {"dragon", "ice"}}
}
