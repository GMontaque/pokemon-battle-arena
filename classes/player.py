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
        # self.battle_pokemon = {
        #     "s": {"name": "squirtle",
        #             "description": "turtle like pokemon that likes "
        #                     "to make jokes and enjoys a good swin",
        #                     "pokemon_type": "water",
        #                     "health": 120,
        #                     "attacks": {"s1": 20, "s2": 30, "s3": 40, "s4": 50}},

        #     "c": {"name": "charmander",
        #         "description": "fire like pokemon that likes "
        #                     "can have a temper so be careful not to anger",
        #                     "pokemon_type": "fire",
        #                     "health": 120,
        #                     "attacks": {"c1": 20, "c2": 30, "c3": 40, "c4": 50}},

        #     "b": {"name": "bulbasaur",
        #         "description": "green type pokemon that can be found "
        #                     "in the surroudning forests enjoing the sun",
        #                     "pokemon_type": "earth",
        #                     "health": 120,
        #                     "attacks": {"b1": 20, "b2": 30, "b3": 40, "b4": 50}}
        # }

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
                #description
                print(f"{pokemon_name} is a "
                      f"{pokedex[pokemon_name]['description']}")

                # pokemon type
                print(f"{pokemon_name} is a "
                      f"{pokedex[pokemon_name]['pokemon_type']} type pokemon")

                # pokemon attack list and values
                print(f"{pokemon_name} has the following attacks "
                      f"{pokedex[pokemon_name]['attacks']}")

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
                 "description": "turtle like pokemon that likes "
                 "to make jokes and enjoys a good swin",
                 "pokemon_type": "water",
                 "health": 120,
                 "attacks": {"s1": 20, "s2": 30, "s3": 40, "s4": 50}},

    "charmander": {"name": "charmander",
                   "description": "fire like pokemon that likes "
                   "can have a temper so be careful not to anger",
                   "pokemon_type": "fire",
                   "health": 120,
                   "attacks": {"c1": 20, "c2": 30, "c3": 40, "c4": 50}},

    "bulbasaur": {"name": "bulbasaur",
                  "description": "green type pokemon that can be found "
                  "in the surroudning forests enjoing the sun",
                  "pokemon_type": "earth",
                  "health": 120,
                  "attacks": {"b1": 20, "b2": 30, "b3": 40, "b4": 50}}
}
