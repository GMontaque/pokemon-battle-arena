import random
import re
import time
import os
import pyfiglet
from tabulate import tabulate
from colorama import Fore, Back, Style

# global styling variables
error_colour = Back.RED + Fore.WHITE
reset_styling = Style.RESET_ALL = Style.RESET_ALL
game_notification = Back.BLUE + Fore.WHITE
proffessor_oak = (Style.RESET_ALL + Fore.GREEN + "Proffessor Oak: "
                  + Style.RESET_ALL)


class Battle:
    '''
    - This is the battle class where the pokemon battles take place

    - It contains 3 methods fight_setup which is first called
    so trainers can choose there first pokemon to fight with first.

    - choose_new_pokemon: which is called when a players pokemon
      faints (health 0)

    - battle_stadium where the battle takes palce
    '''
    def __init__(self, p1, p2):
        # player one object
        self.attacker = p1
        # player two object
        self.defender = p2
        # pokemon choosen by either player 1 or player 2 who is attacking
        self.attacker_pokemon = None
        # pokemon choosen by either player 1 or player 2 who is defending
        self.defender_pokemon = None

    def fight_setup(self):
        '''
        Players are asked to choose which pokemon they wish to fight with first
        '''
        # user inputs pokemon name and value is checked
        while True:
            battle_pokemon_names_attacker = [
                    list(self.attacker.battle_pokemon)
            ]
            # table displaying pokemon user can choose from
            print(tabulate(battle_pokemon_names_attacker,
                  tablefmt="double_grid"))
            try:
                # asks player 1 to choose a pokemon
                attacker_pokemon_name = input(
                    proffessor_oak
                    + f"{self.attacker.name.capitalize()} which"
                    " pokemon do you want to fight "
                    "with first: "
                    + reset_styling
                    ).lower().replace(" ", "")
                # checks for no value
                if not attacker_pokemon_name:
                    raise ValueError(error_colour + "Proffessor Oak: Oops "
                                     "doesn't seem like you choose a pokemon, "
                                     "please try again" + reset_styling)
                # checks input matches pokemon name in players battle pack
                elif not self.attacker.battle_pokemon.get(
                     attacker_pokemon_name, None):
                    raise ValueError(error_colour
                                     + "Proffessor Oak: Oops thats not "
                                     "one of the pokemon in your battle pack"
                                     " , please try again" + reset_styling)
                # once user enters a correct value, exits loop
                break
            except ValueError as e:
                print(f"{e}")

        # confirms name choice of player 1 pokemon
        print(proffessor_oak + "Excellent choice "
                               f"{self.attacker.name.capitalize()},"
                               " you have choosen "
                               f"{attacker_pokemon_name.capitalize()}"
                               + reset_styling)
        print("-----------------------------------------------------")
        # checks if player 2 is human or pc
        while True:
            if self.defender.is_human:
                battle_pokemon_names_defender = [
                    list(self.defender.battle_pokemon)
                ]
                # table displaying pokemon user can choose from
                print(tabulate(battle_pokemon_names_defender,
                               tablefmt="double_grid"))
                try:
                    # asks player 2 to choose a pokemon
                    defender_pokemon_name = input(
                        proffessor_oak
                        + f"{self.defender.name.capitalize()} "
                        "which pokemon do you want "
                        "to fight with first: "
                        + reset_styling).lower().replace(" ", "")
                    # checks for no value
                    if not defender_pokemon_name:
                        raise ValueError(error_colour
                                         + "Proffessor Oak: Oops doesn't "
                                         "seem like you choose a pokemon, "
                                         "please try again" + reset_styling)
                    # checks input matches pokemon name in players battle pack
                    elif not self.defender.battle_pokemon.get(
                         defender_pokemon_name, None):
                        raise ValueError(error_colour
                                         + "Proffessor Oak: Oops thats not "
                                         "one of the pokemon in your battle "
                                         "pack, please try again"
                                         + reset_styling)
                    # once user enters a correct value, exits loop
                    break
                except ValueError as e:
                    print(f"{e}")
            else:
                # player 2 is a PC player so will choose its own pokemon
                defender_pokemon_name = random.choice(list(
                    self.defender.battle_pokemon))
                break

        # confirms name choice of player 2 pokemon
        print(proffessor_oak + "Excellent choice "
                               f"{self.defender.name.capitalize()}, you "
                               "have choosen "
                               f"{defender_pokemon_name.capitalize()}"
                               + reset_styling)
        print("-----------------------------------------------------")
        ''' stores the object which relates to the pokemon name selected
        from the attacking players battle pack'''
        self.attacker_pokemon = self.attacker.battle_pokemon[
            attacker_pokemon_name]
        ''' stores the object which relates to the pokemon name selected
        from the defending players battle pack'''
        self.defender_pokemon = self.defender.battle_pokemon[
            defender_pokemon_name]

    def choose_new_pokemon(self):
        '''
        when a player pokemon faints (health 0) this function is called
        player is asked to choose a new pokemon from their battle pack
        '''
        # players name whos pokemon fainted
        fainted_pokemon_trainer = self.defender.name.capitalize()
        # name of fainted pokemon
        fainted_pokemon = self.defender_pokemon["name"].capitalize()
        print(game_notification + f" {fainted_pokemon_trainer} looks like "
                                  f"{fainted_pokemon} "
                                  "fainted " + reset_styling)
        # name of current attacking pokemon
        current_attacking_pokemon = self.attacker_pokemon["name"]
        print(game_notification + " The attacker "
                                  f"{current_attacking_pokemon.capitalize()}"
                                  " is alive " + reset_styling)
        # checks if player with fainted pokemon, has pokemon left to use
        if len(self.defender.battle_pokemon) == 0:
            # battle end message to show player has lost
            print(proffessor_oak + f"O dear {fainted_pokemon_trainer} all "
                                   "your pokemon have fainted, you loose"
                                   + reset_styling)
        # check if player with fainted pokemon is PC or human
        elif self.defender.is_human is False:
            # player confirmed as PC, auto select to choose new pokemon
            pokemon_random_name = random.choice(list(
                 self.defender.battle_pokemon))
            self.defender_pokemon = self.defender.battle_pokemon[
                    pokemon_random_name]
            # confirms choice has been made
            print(proffessor_oak + f"Excellent choice, you have choosen "
                  f"{pokemon_random_name}" + reset_styling)
            print(game_notification + f" {fainted_pokemon_trainer} has "
                                      "selected a new pokemon "
                                      + reset_styling)
            # restarts battle
            self.battle_stadium()
        else:
            # player is confirmed as human
            current_defender_pokemon = [
                    list(self.defender.battle_pokemon)
                ]
            while True:
                print(tabulate(current_defender_pokemon,
                      headers=["Pokemon Left in party"],
                      tablefmt="double_grid"))
                try:
                    # input asking user what pokemon they want to choose
                    defender_pokemon_name = input(proffessor_oak +
                                                  f"{fainted_pokemon_trainer} "
                                                  "which pokemon do you want "
                                                  "to fight with next: "
                                                  + reset_styling
                                                  ).lower().replace(" ", "")
                    # checks if value is in players battle pack
                    if defender_pokemon_name in self.defender.battle_pokemon:
                        # confirms name choice of defending pokemon
                        print(proffessor_oak + f"Excellent choice, you have"
                              f" choosen {defender_pokemon_name.capitalize()}"
                              + reset_styling)
                        ''' stores the object which relates to the pokemon
                        name selected from the defending players battle pack'''
                        self.defender_pokemon = self.defender.battle_pokemon[
                            defender_pokemon_name]
                        print(game_notification + f" {fainted_pokemon_trainer}"
                              " has selected a new pokemon " + reset_styling)
                        # restarts battle
                        self.battle_stadium()
                        break
                    else:
                        # error if user inputs incorrect value
                        raise ValueError(error_colour + "Proffessor Oak: Oops "
                                         "sorry thats not"
                                         " one of the options please "
                                         "try again" + reset_styling)
                except ValueError as e:
                    print(f"{e}")

    def battle_stadium(self):
        '''
        function used for the actual battle phase
        here players will take turns in selecting an attack
        these attacks reduce the defending pokemons health
        this process continues until a pokemon has fainted
        each player and pokemon flip after each attack
        '''
        time.sleep(3)
        os.system("clear")
        # battle area subhead
        battle_area_header = pyfiglet.figlet_format("Battle Arena",
                                                    font="slant",
                                                    justify="center")
        print(battle_area_header)
        print(proffessor_oak + "let the battle begin")
        print("-----------------------------------------------------")

        while True:
            # represents the choosen pokemon objects as choosen in fight_setup
            attacker_pokemon = self.attacker_pokemon
            defender_pokemon = self.defender_pokemon
            # gets the pokemons health
            attacker_health = attacker_pokemon["health"]
            defender_health = defender_pokemon["health"]
            # generates the pokemon on screen health bar
            health_bar_attack = "="*int(attacker_health/10)
            health_bar_defend = "="*int(defender_health/10)
            # generates the onscreen pokemon attack list
            attacker_pokemon_attacks = {}
            for i in range(1, 5):
                attacker_pokemon_attacks[i] = attacker_pokemon["attacks"][i][1]

            printed_attacks = ' '.join(f"| {key}: {value}" for key,
                                       value in
                                       attacker_pokemon_attacks.items())
            ''' generates the onscreen battle and displays stats
             displays trainer name, pokemon name, pokemon health and
             attack pokemon moves'''
            trainer = Fore.GREEN + "Trainer:" + Style.RESET_ALL
            attacker = Fore.GREEN + "Attacker:" + Style.RESET_ALL
            attacks = Fore.GREEN + "Attacks:" + Style.RESET_ALL
            defender = Fore.GREEN + "Defender:" + Style.RESET_ALL
            # onscreen battle
            print(
                f"[ {trainer} {self.attacker.name.capitalize()}] \n"
                f"[ {attacker} {attacker_pokemon['name'].capitalize()} HP: "
                f"{health_bar_attack} ({attacker_health}) ]\n"
                f"[ {attacks}  {printed_attacks} |]\n"
                "\n"
                f"[ {trainer}  {self.defender.name.capitalize()}]\n"
                f"[ {defender} {defender_pokemon['name'].capitalize()} HP: "
                f"{health_bar_defend} ({defender_health}) ]\n"
            )
            # checks if player 2 is human or computer
            if self.attacker.is_human:
                while True:
                    try:
                        # input asking user what attack they wish to do
                        player_attack_choice = input(game_notification +
                                                     f" What attack do you "
                                                     "wish to use: "
                                                     + reset_styling
                                                     ).replace(" ", "")
                        # checks if value is a number and if value
                        # is either 1,2,3 or 4
                        if (player_attack_choice.isdigit() and
                           player_attack_choice in ["1", "2", "3", "4"]):
                            # updates input value to a number
                            player_attack_choice = int(player_attack_choice)
                            break
                        else:
                            raise ValueError(error_colour + "Proffessor Oak: "
                                             "Oops sorry thats not one of the "
                                             "options try typing 1,2,3 or 4 "
                                             + reset_styling)
                    except ValueError as e:
                        print(f"{e}")
            else:
                # computer chooses random attack
                player_attack_choice = random.choice(list(
                    attacker_pokemon["attacks"]))

            # gets the number value of the string
            attack = attacker_pokemon["attacks"][player_attack_choice][1][-2:]
            # gets the name of the attack
            attack_name = attacker_pokemon["attacks"][
                player_attack_choice][1][:-4]
            #  deducates the attack amount from the defending pokemons health
            defender_health = defender_pokemon["health"]
            attack_type = attacker_pokemon["attacks"][player_attack_choice][0]
            defender_weakness = defender_pokemon["x2_attack"]
            # checks if attack is super effective against defender
            if attack_type in defender_weakness:
                # updates defending pokemon health
                new_health = defender_health - (int(attack)+40)
                # prints what the attacker did
                print(game_notification
                      + f" {attacker_pokemon['name'].capitalize()} used"
                      f" {attack_name} causing "
                      f"{(int(attack)+40)} damage as it "
                      "was super effective " + reset_styling)
            else:
                # updates defending pokemon health
                new_health = defender_health - int(attack)
                # prints what the attacker did
                print(game_notification
                      + f" {attacker_pokemon['name'].capitalize()} used"
                      f" {attack_name} causing {attack} "
                      "damage " + reset_styling)

            # updates defending pokemons health
            defender_pokemon["health"] = new_health

            print("-----------------------------------------------------")

            # checks pokemon healh
            if defender_pokemon["health"] <= 0:
                # deletes fainted pokemon from battle_pokemon object
                del self.defender.battle_pokemon[defender_pokemon["name"]]
                # player with fainted pokemon chooses another
                self.choose_new_pokemon()
                break
            time.sleep(1)
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
