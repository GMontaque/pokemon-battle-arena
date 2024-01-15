import random

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
        # asks attacking player for name of pokemon they will use
        attacker_pokemon_name = input(f"Proffessor Oak: {self.attacker.name} "
                                      "which pokemon "
                                      "do you want to fight with first: ")
        # confirms name choice of defending pokemon
        print(f"Proffessor Oak: excellten choice, you have choosen "
              f"{attacker_pokemon_name}")
        # asks defending player for name of pokemon they will use
        defender_pokemon_name = input(f"Proffessor Oak: {self.defender.name} "
                                      "which pokemon do you want to fight "
                                      "with first: ")
        # confirms name choice of defending pokemon
        print(f"Proffessor Oak: excellten choice, you have choosen "
              f"{defender_pokemon_name}")
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
        else:
            defender_pokemon_name = input(f"Proffessor Oak: {fainted_pokemon_trainer} "
                                      "which pokemon do you want to fight "
                                      "with next: ")
            # confirms name choice of defending pokemon
            print(f"Proffessor Oak: excellten choice, you have choosen "
              f"{defender_pokemon_name}")
            # contains the dictionary result of pokemon inside the object battle_pokemon for the attacker
            self.defender_pokemon = self.defender.battle_pokemon[defender_pokemon_name]
            self.battle_stadium()
        

    def battle_stadium(self):
        print("Proffessor Oak: let the battle begin")

        while True:
            # pokemon objects same as in fight_setup
            attacker_pokemon = self.attacker_pokemon
            defender_pokemon = self.defender_pokemon
            print("attacker: ", attacker_pokemon["name"])
            print("defender: ", defender_pokemon["name"])
            # prints attacking pokemon attacks
            print(attacker_pokemon["attacks"])
            # checks if player 2 is human or computer
            if self.attacker.is_human:
                # input asking user what attack they wish to do
                player_attack_choice = input(f"what attack do you wish to use: ")
            else:
                # computer chooses random attack
                player_attack_choice = random.choice(list(attacker_pokemon["attacks"]))
            # gets attack value deducates the amount from the defending pokemons health
            attack = attacker_pokemon["attacks"][player_attack_choice]
            defender_health = defender_pokemon["health"]
            new_health = defender_health - attack
            # updates defending pokemons health
            defender_pokemon["health"] = new_health
            # prints new defending pokemon health
            print(f"{defender_pokemon['name']} new health is {new_health}")
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