class Battle:
    def __init__(self, p1, p2):
        self.attacker = p1
        self.defender = p2
        self.attacker_pokemon = None
        self.defender_pokemon = None

    def fight_setup(self):
        attacker_pokemon_name = input(f"Proffessor Oak: {self.attacker.name} "
                                      "which pokemon"
                                      "do you want to fight with first: ")
        print(f"Proffessor Oak: excellten choice, you have choosen "
              f"{attacker_pokemon_name}")
        defender_pokemon_name = input(f"Proffessor Oak: {self.defender.name} "
                                      "which pokemon do you want to fight "
                                      "with first: ")
        print(f"Proffessor Oak: excellten choice, you have choosen "
              f"{defender_pokemon_name}")
        self.attacker_pokemon = self.attacker.battle_pokemon[attacker_pokemon_name]
        self.defender_pokemon = self.attacker.battle_pokemon[defender_pokemon_name]

    def battle_stadium(self):
        print("Proffessor Oak: let the battle begin")

        while True:
            # pokemon objects
            attacker_pokemon = self.attacker_pokemon
            defender_pokemon = self.defender_pokemon
            print("attacker: ", attacker_pokemon["name"])
            print("defender: ", defender_pokemon["name"])
            print(attacker_pokemon["attacks"])
            player_attack_choice = input(f"what attack do you wish to use: ")
            attack = attacker_pokemon["attacks"][player_attack_choice]
            defender_health = defender_pokemon["health"]
            new_health = defender_health - attack
            defender_pokemon["health"] = new_health
            print(f"{defender_pokemon['name']} new health is {new_health}")

            if defender_pokemon["health"] < 0:
                break
            self.flip()

    def flip(self):
        temp = self.attacker_pokemon
        self.attacker_pokemon = self.defender_pokemon
        self.defender_pokemon = temp
