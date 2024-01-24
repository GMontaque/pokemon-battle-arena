import random
import re
from tabulate import tabulate

class Battle:
    def __init__(self, p1, p2):
        # player one object
        self.attacker = p1
         # player two object
        self.defender = p2
        # pokemon from either player 1 or player 2 who is attacking
        self.attacker_pokemon = None
        # pokemon from either player 1 or player 2 who is defending
        self.defender_pokemon = None

    def fight_setup(self):
        # user inputs pokemon name and value is checked
        while True:
            battle_pokemon_names_attacker = [
                    list(self.attacker.battle_pokemon)
            ]
                                
            # display table
            print(tabulate(battle_pokemon_names_attacker, tablefmt="double_grid"))
            try:
                # asks attacking player for name of pokemon they will use
                attacker_pokemon_name = input(f"Proffessor Oak: {self.attacker.name} "
                                      "which pokemon "
                                      "do you want to fight with first: ").lower()
                # checks for no value
                if not attacker_pokemon_name:
                    raise ValueError("Proffessor Oak: Oops doesn't "
                                             "seem like you choose a pokemon, "
                                                "please try again")
                    ''' checks input matches pokemon name in players battle pack
                    '''
                elif not self.attacker.battle_pokemon.get(attacker_pokemon_name, None):
                    raise ValueError("Proffessor Oak: Oops thats not "
                                             "one of the pokemon in your battle pack"
                                             " , please try again")
                else:
                    # once user enters a correct value, exits loop
                    break
            except ValueError as e:
                print(f"{e}")

        # confirms name choice of player 1 pokemon
        print(f"Proffessor Oak: excellten choice {self.attacker.name}, you have choosen "
              f"{attacker_pokemon_name}")
        print("-----------------------------------------------")

        while True:
            if self.defender.is_human:
                battle_pokemon_names_defender = [
                    list(self.defender.battle_pokemon)
                ]
                                
                # display table
                print(tabulate(battle_pokemon_names_defender, tablefmt="double_grid"))
                try:
                    # asks defending player for name of pokemon they will use
                    defender_pokemon_name = input(f"Proffessor Oak: {self.defender.name} "
                                                "which pokemon do you want to fight "
                                                "with first: ").lower()
                    # checks for no value
                    if not defender_pokemon_name:
                        raise ValueError("Proffessor Oak: Oops doesn't "
                                                "seem like you choose a pokemon, "
                                                    "please try again")
                        ''' checks input matches pokemon name in players battle pack
                        '''
                    elif not self.defender.battle_pokemon.get(defender_pokemon_name, None):
                        raise ValueError("Proffessor Oak: Oops thats not "
                                                "one of the pokemon in your battle pack"
                                                " , please try again")
                    else:
                        # once user enters a correct value, exits loop
                        break
                except ValueError as e:
                    print(f"{e}")
            else:
                defender_pokemon_name = random.choice(list(self.defender.battle_pokemon))
                break   


        # confirms name choice of player 2 pokemon
        print(f"Proffessor Oak: excellten choice {self.defender.name}, you have choosen "
              f"{defender_pokemon_name}")
        print("-----------------------------------------------")
        # contains the dictionary result of pokemon inside the object battle_pokemon for the attacker
        self.attacker_pokemon = self.attacker.battle_pokemon[attacker_pokemon_name]
        # contains the dictionary result of pokemon inside the object battle_pokemon for the attacker
        self.defender_pokemon = self.defender.battle_pokemon[defender_pokemon_name]

    def choose_new_pokemon(self):
        fainted_pokemon_trainer = self.defender.name
        fainted_pokemon = self.defender_pokemon["name"]
        print(f"Proffessor Oak: {fainted_pokemon_trainer} looks like {fainted_pokemon} fainted ")
        current_attacking_pokemon = self.attacker_pokemon["name"]
        print(f"the attacker {current_attacking_pokemon} is alive")
        
        if len(self.defender.battle_pokemon) == 0:
            print(f"Proffessor Oak: O dear {fainted_pokemon_trainer} all your pokemon have fainted, you loose")
        elif self.defender.is_human == False:
            pokemon_random_name = random.choice(list(self.defender.battle_pokemon))
            self.defender_pokemon = self.defender.battle_pokemon[pokemon_random_name]
            print(f"Proffessor Oak: excellten choice, you have choosen "
              f"{pokemon_random_name}")
            self.battle_stadium()
        else:
            current_defender_pokemon = [
                    list(self.defender.battle_pokemon)
                ]
            while True:  
                print(tabulate(current_defender_pokemon,headers=["Pokemon Left in party"], tablefmt="double_grid"))            
                try:
                    # input asking user what attack they wish to do
                    defender_pokemon_name = input(f"Proffessor Oak: {fainted_pokemon_trainer} "
                                                  "which pokemon do you want to fight "
                                                  "with next: ")
                    # checks if value is a number and if value is either 1,2,3 or 4
                    if defender_pokemon_name in self.defender.battle_pokemon:
                        # updates input value to a number
                        # confirms name choice of defending pokemon
                        print(f"Proffessor Oak: excellten choice, you have choosen "
                        f"{defender_pokemon_name}")
                        # contains the dictionary result of pokemon inside the object battle_pokemon for the attacker
                        self.defender_pokemon = self.defender.battle_pokemon[defender_pokemon_name]
                        self.battle_stadium()
                        break
                    else:
                        raise ValueError("Proffessor Oak: Oops sorry thats not one of the options please try again")
                except ValueError as e:
                        print(f"{e}")

    def battle_stadium(self):
        print("Proffessor Oak: let the battle begin")
        print("-----------------------------------------")

        while True:  
            # represents the choosen pokemon object as choose in fight_setup
            attacker_pokemon = self.attacker_pokemon
            defender_pokemon = self.defender_pokemon
            # gets the pokemons health
            attacker_health = attacker_pokemon["health"]
            defender_health = defender_pokemon["health"]
            # generates the pokemon on screen health bar
            health_bar_attack = "="*int(attacker_health/10)
            health_bar_defend = "="*int(defender_health/10)
            
            # generates the onscreen battle and displays stats
            # displays trainer name, pokemon name, pokemon health and attack pokemon moves
            print(
                f"[ Trainer: {self.attacker.name}] \n"
                f"[ Attacker: {attacker_pokemon['name']} HP: {health_bar_attack} ({attacker_health}) ]\n"
                f"{attacker_pokemon['attacks']}\n"
                "\n"
                f"[ Trainer: {self.defender.name}]\n"
                f"[ Defender: { defender_pokemon['name']} HP: {health_bar_defend} ({defender_health}) ]\n"
            )
            
            # checks if player 2 is human or computer
            if self.attacker.is_human:
                while True:
                    try:
                        # input asking user what attack they wish to do
                        player_attack_choice = input(f"what attack do you wish to use: ")
                        # checks if value is a number and if value is either 1,2,3 or 4
                        if player_attack_choice.isdigit() and player_attack_choice in ["1","2","3","4"]:
                            # updates input value to a number
                            player_attack_choice = int(player_attack_choice)
                            break
                        else:
                            raise ValueError("Proffessor Oak: Oops sorry thats not one of the options try typing 1,2,3 or 4 ")
                    except ValueError as e:
                        print(f"{e}")
            else:
                # computer chooses random attack
                player_attack_choice = random.choice(list(attacker_pokemon["attacks"]))

            # gets the number value of the string
            attack = attacker_pokemon["attacks"][player_attack_choice][-2:]
            # gets the name of the attack
            attack_name = attacker_pokemon["attacks"][player_attack_choice][:-4]
            # prints what the attacker did
            print(f"{attacker_pokemon['name']} used {attack_name} causing {attack} damage")
            #  deducates the attack amount from the defending pokemons health
            defender_health = defender_pokemon["health"]
            # updates defending pokemon health
            new_health = defender_health - int(attack)

            # updates defending pokemons health
            defender_pokemon["health"] = new_health

            print("-----------------------------------------")

            #checks pokemon healh
            if defender_pokemon["health"] <= 0:
                # deletes fainted pokemon from battle_pokemon object
                del self.defender.battle_pokemon[defender_pokemon["name"]]
                # player with fainted pokemon chooses another
                self.choose_new_pokemon()
                break
            # flips attacker and defending to allow for turn based gameplay
            self.flip()

    def flip(self):
        # flips attacking defeding pokemon objects
        temp = self.attacker_pokemon
        self.attacker_pokemon = self.defender_pokemon
        self.defender_pokemon = temp

        # flips player objects
        temp_trainer = self.attacker
        self.attacker = self.defender
        self.defender = temp_trainer