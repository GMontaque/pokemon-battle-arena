# Pokemon Battle Arena

## About the Project

![picture of initial game screem](assets/img/)

- I have taken inspiration for creating this game from the very populator Pokémon franchise, in that game a player follows the story of a new trainer building up his skills, catching new Pokémon and battling other trainers with the Pokémon he catches. The specific game that I have created is just the battle part where a player is given the option to fight against another player or they can play against the PC, before this the players or pc will choose their battle Pokémon.

- To do this a player is given the option to review a number of Pokémon. When reviewing the Pokémon it displays the Pokémon type, a description which explains the Pokémon along with their name and the attack moves they can do. This then allows the user to make an informed decision as to the Pokémon they will to have in their battle party. Once the user has chosen their Pokémon, they are taken to the battle area which is where the actually battle takes place. The players will take turn to complete an attack until one of the players Pokémon has a health of 0 (fainted). When the players Pokémon faints, they are then asked to selected another Pokémon from their party, when a player has no more Pokémon in their party the game finishes and the user can either play again against another player or pc. The other option is to exit the game completely.

[Live Website Link](https://pokemon-battle-arena-52c50ec4c2a7.herokuapp.com/)

## Target Audience

**What was the idea behind building the product?**

- To allow users to play a fun enjoyable game
- To allow users to regain some nostalgia
- Create a simple can that can be picked up and played
- To engage people
- Create a game that the user will keep returning to play
- Create a game which allows the user to make different choices which will effect the outcome of the game
- To create a game that does not get boring or repetitive
- Make new memories and to allow them to play the game with others

**Who is the user**

- The user will be somebody of any age but most likely an older person who has played Pokémon before
- The person could may have grown up with Pokémon as a child
- The person will be an avid gamer and enjoy the nostalgia of old game
- The person maybe be used to and aware of emulator games

**What are the needs/wants of the users?**

- Game must be easy to navigate
- Game must clearly state the rules and how to play
- Game should guide the member
- Game must have simple controls
- Game must be replayable
- The user is able to pick up the game with little experience
- The user is informed of errors and what to do

**What are the needs/wants of the business?**

- To create a game that users enjoy
- A game that users want to come back to and play again and again
- A game that keeps the user’s interest
- A game that taps into a person’s nostalgia
- A game that they will recommend to their friends
- A game with a level of immersion
- A game users can either play single player or with others

**How does the site meet the needs of user and business**

- The game will contain text and images in the style of the previous Pokémon games
- The names used in the game will be from the original list of Pokémon’s
- The game has been created so that it can be played again and again helping to keep the user engaged
- A description/game rules have been included so that the business can easily and effectively describe the site and explain how to use it
- A person with an interest in classic games will find the program both interesting and familiar
- The game is easy to play
- Included in the program is error handling and feedback for the user
- The program has been created to guide users to improve the play ability

## How to play the game and Game Design

**Walk through of the game**

- First the user (player 1) will be asked for their name, the player 1 will be asked if they are going to be playing against a friend (human player). If they say yes to this then they will be directed to entire the users name (player 2), if they say no to this then a pre-defined user name will be used by the game.
- Once the names have been selected the user will be shown the rules of the game, and what to expect. Once they have read through this, they will then be given the option to move to the Pokémon selection stage or they can exit the game here.
- Assuming they have type “fight” and moved to the Pokémon selection stage the players will take turns in reviewing Pokémon before being asked if the Pokémon is to be added to their battle pack. Once player 1 has chosen all their Pokémon, player 2 will be asked to choose their Pokémon. If player 2 is the PC this will be automated.
- When Pokémon selection is completed, players are taken to the battle area, firstly each player is asked to choose which Pokémon from their battle pack they wish to start with. If player 2 is a PC this is automated. After Pokémon selected begins the turn-based attacks, each player can choose from 1 of 4 attacks they can do against the other player. Multipliers have also been included being that the Pokémon’s type is taken into account, if the attacker is super effective against the defender, then the attackers attack is double. But if they are not supper effective than the normal value of the attack is done and the defenders health is deducted that amount.
- When a players Pokémon faint (0 health) they are given the option to bring out another Pokémon, and the battle will continue again. This loop will continue until one player has no Pokémon left to fight with and the game will be over.
- The player will then be taken to the next stage where they will be asked firstly if they wish to play another game, if they say yes, they will then be asked if they wish to play against a human player 2. If they say no then a PC player 2 will be used and they will then both be taken to the Pokémon selection stage to pick a new set of 3 Pokémon to add to their battle pack before going into the battle area.
- The player also has the option to completing exit the game during this next stage if they do not wish to play another game

**Game Design**

- The idea behind the design choice of the game was heavily influcenced by the pokemon games, in the pokemon games there is a character called professor oak. His role in the game is to provide the user with information and detail and guides the user through the game and and provides new and important information. I have used that in my game and created the game as a story and in a conversational style all inputs of information that the user has to make are questions presented to them by professor oak and I have contiened this theme with the error handling such as if the user enters the incorrect value.

- Also when desgining the game I have used information from the actual pokemon game such as names descripitons of pokemon, pokmeon attack moves and the pokemon types so that a person with previous knowledge of the games can pick up the game I have created easily as they will be able to tap into the same areas of knowledge.
