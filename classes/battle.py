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
                                      "which pokemon"
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
        self.defender_pokemon = self.attacker.battle_pokemon[defender_pokemon_name]

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
            # input asking user what attack they wish to do
            player_attack_choice = input(f"what attack do you wish to use: ")
            # gets attack value deducates the amount from the defending pokemons health
            attack = attacker_pokemon["attacks"][player_attack_choice]
            defender_health = defender_pokemon["health"]
            new_health = defender_health - attack
            # updates defending pokemons health
            defender_pokemon["health"] = new_health
            # prints new defending pokemon health
            print(f"{defender_pokemon['name']} new health is {new_health}")

            if defender_pokemon["health"] < 0:
                break
            # flips attacker and defending to allow for turn based gameplay
            self.flip()

    def flip(self):
        # flips attacking defeding pokemon objects
        temp = self.attacker_pokemon
        self.attacker_pokemon = self.defender_pokemon
        self.defender_pokemon = temp
