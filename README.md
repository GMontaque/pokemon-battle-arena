# Pokemon Battle Arena

## About the Project

![picture of initial game screem](assets/img/)

- I have taken inspiration for creating this game from the very popular Pokémon franchise – the aim of which is to build up your skills, catch new Pokémon and battle other trainers with the Pokémon you catch.

- The specific game that I have created is just the battle part, where a player is given the option to fight against another player, or they can play against the PC. I have included an additional feature, in that each player or PC is given the option to choose their battle Pokémon from a pre-defined list which also contains details of the Pokémon. This is important as the attacks executed depend on the Pokémon type that the player has chosen, and the Pokémon type they are fighting. This means the player will need to choose strategically.

- A player is given the option to review a number of different Pokémon. When reviewing the Pokémon, the information provided displays the Pokémon type, includes a description which explains the Pokémon along with their name and the attack moves that they can do. This then allows the user to make an informed decision as to the Pokémon they want to use in their battle party. Once the user has chosen their Pokémon, they are taken to the battle area which is where the actual battle takes place between the selected Pokémon. The battle arena first starts by each player picking an initial Pokémon to fight with, then each player will take turns to complete an attack until one of the players’ Pokémon has a health of 0 (fainted). When the players’ Pokémon faints, they are then asked to select another Pokémon from their battle party to continue the fight. When a player has no more Pokémon in their party, the game finishes and the user can either play again or exit the game. If they wish to play again, they will be asked if this is against a human player or the PC.

[Live Website Link](https://pokemon-battle-arena-52c50ec4c2a7.herokuapp.com/)

## Target Audience

**What was the idea behind building the product?**

- To allow users to play a fun enjoyable game.
- To allow users to regain some nostalgia and engage people.
- Create a simple game that can be picked up and played.
- Create a game that the users will want to keep returning to play.
- Create a game which allows the user to make different choices which will affect the outcome of the game, l add a level of difficulty and require greater skill to play successfully
- To create a game that does not get boring or repetitive.
- Make new memories and to allow them to play the game with others.

**Who is the user?**

- The user will be somebody of any age but most likely an older person who has played Pokémon before
- The person may have grown up with Pokémon as a child.
- The person will be an avid gamer and enjoy the nostalgia of old games.
- The person maybe be used to and aware of emulator games.

**What are the needs/wants of the users?**

- The game must be easy to navigate.
- The game must clearly state the rules and how to play.
- The game should guide the member.
- The game must have simple controls.
- The game must be replayable.
- The user is able to pick up the game with little experience.
- The game is fun to play and has varying levels of difficulty
- The game challenges the user

**What are the needs/wants of the business?**

- To create a game that users enjoy
- A game that informs the player of errors and what to do.
- A game that users want to come back to and play again and again.
- A game that keeps the users interested
- A game that taps into a person’s nostalgia
- A game that they will recommend to their friends.
- A game with a level of immersion
- A game users can either play single player or with others.

**How does the site meet the needs of the user and business?**

- The game will contain content which will link directly to content from the previous Pokémon games.
- The names used in the game will be from the original list of Pokémon’s.
- The game has been created so that it can be played again and again helping to keep the user engaged.
- A description/game rules have been included so that the business can easily and effectively describe the site and explain how to use it
- A person with an interest in classic games will find the program both interesting and familiar.
- The game is easy to play.
- Included in the program is error handling and feedback for the user.
- The program has been created to guide users to improve the play ability.

## How to play/ Game Flow

**Walk through of the game**

- When the game starts the user (player 1) will be asked for their name, player 1 will be asked if they are going to be playing against a friend (human player). If they say yes to this, they will be directed to enter the users name (player 2), if they say no, a pre-defined username will be used by the game which will be the PC player.

- After the names have been selected, the user will be shown the rules of the game, and what to expect. Once they have read through this, they will be given the option to move to the Pokémon selection stage or they can exit the game here.

- Assuming they have typed in the word “fight”, they are taken to the Pokémon selection stage. Here, players will take turns in reviewing Pokémon before being asked if the Pokémon is to be added to their battle pack. Once player 1 has chosen all their Pokémon, player 2 will be asked to choose their Pokémon. If player 2 is the PC this will be automated.

- When the Pokémon selection is completed, players are taken to the battle arena. In the battle arena each player is asked to choose which Pokémon from their battle pack they wish to start the battle with. If player 2 is a PC this is automated. After Pokémon selection, the turn-based attacks begin. Each player can choose from 1 of 4 attacks they can execute against the other player. Multipliers have also been included in the game that will add 40 hit points to the attacking Pokémon’s attack depending on the type of the defending Pokémon’s - as this is taken into account. If the attacker is super effective against the defender, then the attack will be increased by the 40 hit points mentioned. But if they are not super effective the normal value of the attack is applied and the defender’s health is deducted by that amount.

- When a players Pokémon faint (0 health) they are given the option to bring out another Pokémon, and the battle will continue again. This loop will repeat until one player has no Pokémon left to fight with and the game will be over.

- The player will then be taken to the next stage where they will be asked if they wish to play another game. If they say yes, they will then be asked if they wish to play against a human player. If they say no then player 2 will become a non-human player (PC) and they will then both be taken to the Pokémon selection stage to pick a new set of 3 Pokémon to add to their battle pack before going into the battle arena.

- The player also has the option to completely exit the game during the game restart stage if they do not wish to play another game

## Design choice

The design choice of the game was heavily influenced by the Pokémon games. The Pokémon games has character called Professor Oak. His role in the game is to provide the user with information, details about the game and about Pokémon as well as explaining different aspects of the game. He will guide the user through the game and provides new and important information as required.

I have used this theme in my game tool and created the game as a story. It has a conversational style, meaning that most inputs of information that the user has to provide are answers to questions presented to them by Professor Oak. I have continued this theme with the error handling. For example: if the user enters an incorrect value, they will receive a message from Professor Pak informing them of the error they have made. Another example of this conversational style is Or, when the game first loads. A function called ‘game start’ is called from the run.py file, and the player is greeted with a message from Professor Oak and asked for information regarding players and names.

Once that is completed the function ‘play game’ is called. This function is the core of the game and controls most of the game. In this function the player objects are created and each player picks their Pokémon. Then, the battle phase is entered and finally the game restart function is called once the battle phase is completed.

The creation of the player object is done in a separate file called player.py. The reason for this is that there are a certain number of methods and data which solely relate to the player. It also means that once created, the player object can be passed around and then important information pulled and used from that.

The battle phase was also created in a separate file called battle.py and a class was used in order to group related methods together – as explained with the ‘player object’. In order to run the battle and the different methods which relate to it such as health reduction, it is cleaner and simpler to have that all in one file. It means each player object need only to be passed to the battle class and the game will run.

Finally, when the Battle phase is completed, we return to the run.py file. The restart’ function is called which asks the user if they wish to play again or exit the game. If they wish to play again some details are taken and then ’play game’ is called again and the game restarts.

When designing the game, I have used information from the actual Pokémon game such as names descriptions of Pokémon, Pokémon attack moves and the Pokémon types so that a person with previous knowledge of the games can pick up the game I have created easily as they will be able to tap into the same areas of knowledge. I have done the same with the Pokémon attacks and how damage is inflicted against another Pokémon by taking the Pokémon’s type into account.

## Flowchart

- This flow chart shows the user journey from start to finish
  ![picture of initial game screem](assets/img/)

- This flow chart specifically shows the battle sections of the game
  ![picture of initial game screem](assets/img/)

- This flow chart specifically shows the Pokémon selection section
  ![picture of initial game screem](assets/img/)

## Data Model

When planning out the project I had decided that not all my code would be written within my run.py file. This is because I was looking to create and to simplify the layout of the game by grouping together related code. This led to the creation of two extra files each of which contains a class to be used in the game.
The game begins in the run.py file. Here, I created a function called “play game” which introduces the player to the game and asks the player for some information, including their name and their opponent’s name - or a PC player is selected. Once they have read the rules, they are taken to a second function called ’play game’
The majority of the game is run within this function. Firstly, a player variable is created for each player and this variable stores as a value an instance of the player class that is created in the player.py file.

When planning the game there were certain actions that related purely to the player, so I grouped all these together inside the player class, as it made it easier to plan and run the game. The other benefit of this approach is that the entire player object can then be passed to different functions and different parts of the object can be extracted and used. For example, each player is made to choose 3 Pokémon they wish to battle with. The selection process to do this is done within the player class as a method called ‘pick Pokémon’. This is stored in a battle pack which is unique to each player.

Once the selection process is complete the next stage of the game is the battle stage, I created another file for this and within that, created the battle class. This class contains a number of different methods. The battle class was created to group together all the methods relating to the battle section of the game. Within the battle class, you will find fight set up, choose new Pokémon, battle stadium and flip.

Once the battle stage is finished, the final section of the game is a function called game Restart which was included in the run.py file. Here the player is given the option to play again or end the game. This, together with the other 2 functions were included in the main run.py as they are the core 3 functions, one starts the game, one runs the game and one restarts the game.

## Colour and Font Scheme

- Colour for user input and name
- Colour for Pokémon NPC text
- Colour for loading text
- Colour for wrong answers
- Colour for game notifications
- Colour for end game

## Features

- Welcome page

  - This screen will be the first thing that the player sees when they load up the game, it contains the name of the game to clearly indicate to the player the type of game that they have loaded up. It also contains a message from an in-game character called Professor Oak who welcomes them to the game.

- Player 1 User input name and validation

  - The user is asked to enter their name which will be used throughout the game
  - When asking for their name, validation has been added to make sure they enter a string value
  - Error feedback is provided to the user if they raise an error

- Player 2 selection - human or computer

  - Player 1 is asked if they have a friend to play with
  - if the user states ‘no’ in response, then a PC player will be automatically selected as player 2
  - If they respond ‘yes’, they are prompted to input player 2’s name
  - A variable called human is also created and is used later on in the function to automate computer choices

- Game Rules

  - Once both players have been chosen, they are shown the rules of the game
  - The rules contain information about the Pokémon selection progress.
  - The rules also contain information about the battle arena.
  - The rules go through the importance of selecting your Pokémon and depending on your Pokémon type, the attacks can be amplified.
  - Finally, it contains information about how to restart the game or exit the game.

- Each player reviewing and picking Pokémon for their battle pack.

  - This is the Pokémon selection phase.
  - A player can input any 1 of the 10 Pokémon and get back a detailed information sheet about that Pokémon. The information sheet will contain their name, description, type of Pokémon and attack moves. There is also important information about weakness to other Pokémon types.
  - A player can review as many Pokémon as they wish, after each Pokémon’s information sheet, they will be given a choice to add the Pokémon to the battle pack

- Players adding Pokémon to battle pack

  - Adding a Pokémon to a players battle pack is linked with reviewing the Pokémon
  - After a player inputs a Pokémon’s name and receives the detailed information sheet, they are asked if they wish to add the Pokémon to their battle pack
  - If they say ‘yes’, the Pokémon is added and this is confirmed by a on screen message
  - If they type ‘no’, they are taken back to the reviewing stage
  - An error catch has also been included so that the user is unable to select the same Pokémon twice to add to their battle pack. Each Pokémon must be unique

- PC adding Pokémon to battle pack

  - If the player has chosen not to play against a human player, then the PC will automatically choose their own battle pack Pokémon
  - This is confirmed on screen for the user to see that their opponent has selected their Pokémon
  - The variable “human” is used here to check that player 2 is not human

- Entering the battle arena

  - When entering the battle arena there is an on-screen message that first appears from the in-game character Professor Oak informing them they have entered the battle arena.
  - Each player is then asked which Pokémon they wish to start the battle arena with
  - Once both players have chosen their starting Pokémon the battle will start
  - If the user is playing against the computer this selection will be done automatically due to the “human” variable

- Pokémon fight in battle arena display

  - The image attached show the screen that will appear to the user when the battle has started
  - Included in the image is the attack Pokémon and player at the top along with the attacking Pokémon’s health bar
  - Below the attacking Pokémon and player is the same information for the defending Pokémon and player

- Health reduction

  - Under the on-screen battle arena, the attacking player will be asked what attack they wish to execute
  - They have the option to choose 1 of 4 attacks
  - The player selects the attack by inputting the attack number. The attack hit point value will be the amount of damage that will be taken off the defending Pokémon’s health
  - This attack can be increased by 40 if the defending Pokémon is weak to the attack move type, i.e fire type is weak to water
  - Then the attack and defender will switch and the new attacker will then be given the same options and can then attack
  - This process of flipping will continue until one of the players’ Pokémon has fainted (health is 0)

- Selection of a new Pokémon

  - When a player’s Pokémon has fainted, it triggers a method called ‘Choose new Pokémon’
  - In the method there is first a check to see if the player with the fainted Pokémon has any Pokémon left in their battle pack as after each Pokémon faints it is removed from the battle pack so it can’t be used again
  - If there are no Pokémon left for the player to use, the game ends
  - If the player has a Pokémon left which they can use, they are asked which Pokémon they wish to fight with next
  - Then the battle restarts with the player whose Pokémon did not faint having the first attack

- Restart and end game

  - When all Pokémon in a players battle pack have fainted (health 0) it will trigger the restart game function
  - Here player 1 is asked if they want to play another game
  - If player 1 inputs ‘no’ then the game ends and the in-game character Professor Oak confirm this in a goodbye message, asking them to come back soon
  - If player 1 inputs ‘yes’, they are asked if they want to play against a human player
  - If player 1 states ‘no’ a PC player is inputted as player 2
  - If player 1 has stated yes to a human player, player 2 is prompted for their name and then both player 1 and 2 are taken to the review Pokémon stage to add new Pokémon to their battle pack.
  - This is the same if player 2 is the computer, but they will select their own Pokémon for their battle pack

## Future Implementations

- Add in accuracy as a factor to if the attacking Pokémon lands their attack
- Attacks cannot be used infinitely
- A Pokémon’s accuracy can be reduced or increased
- A user can swap out Pokémon mid battle
- Health potions can be used on the players fighting Pokémon

## Technologies and Languages

- Python - Object Oriented Coding Lanugage
- Gitpod – a cloud development environment
- GitHub – a code hosting platform for version control, collaboration and editing websites
- VS Code Desktop – IDE used to code the program
- Heroku - used to deploy the program
- Re – regular expression
  - This was imported and used to check that the user input only contains letters
- Random
  - This was used when the pc needed to select an option at random
- Copy and deepcopy
  - A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
- tabulate
  - used to create tables in python
- Colorama
  - Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning)
- Time
  - This module provides various time-related functions
- OS.sytem
  - Used to clear the terminal by passing it the value "clear"
- pyfiglet
  - Takes ASCII text and renders it in ASCII art fonts

## Testing

### Play Test

- To test my game further i also sent it to a few friends who grew playing pokemon
  - [Website Testing](websiteTesting.md)

### Validator

- Run.py

  - [Website Testing](websiteTesting.md)

- Player.py

  - [Website Testing](websiteTesting.md)

- Battle.py

  - [Website Testing](websiteTesting.md)

### Bug and errors

- When testing my project in Heroku after a recent push of new code, I was shown the below error message. The error message appeared stating that there was an error in a string that was nested inside an F String, the issue was being caused as I had used double quote for the F string and I had used double quotes for an element inside the F String. To resolve this issue, I changed the quotes around the “name” word to single quotation marks and this solved the issue. I had to do this for a number of lines of code.

[Website Testing](websiteTesting.md)

[Website Testing](websiteTesting.md)

[Website Testing](websiteTesting.md)

- An error that I came across was occurring when the user input a value in some circumstances a user could enter the correct result but the game would not accept the value and throw an error. Initially, this was solved by adding “lower()” to the ends of the input which meant all values were lower case, so there was no issue if the user used capital letters. This did not completely solve the issue as, for example, a user, when asked to input a number, could still find there was an issue due to including whitespace.
  If the user inputted a value but pressed the space bar before pressing enter to submit the code the game would flag an error due to the extra whitespace. To solve this, I added in the replace method which removed all white space and would then only return the actual value. This was possible because I had not used a double value with space in-between in any part of my game.

[Website Testing](websiteTesting.md)

- Each player is meant to select 3 unique Pokémon which they add to their own battle pack and which they use these to fight against the other player. An issue I was facing was that when both players chose the same Pokémon and executed an attack, both players would lose the same health, not just the defender. I found this error only appeared when I used organic Pokémon selection where the user had to choose. If I used pre-selected data in battle_pokemon, this error did not occur
  On further testing, I found that the issue was happening because when I was presetting the values in battle_pokemon, it would create two objects but when manually adding values to the battle Pokémon it was counting them as one object shared between both players. To solve this issue, I had to import “copy” and used the method “deepcopy” when adding a Pokémon to battle_pokemon.

[Website Testing](websiteTesting.md)

[Website Testing](websiteTesting.md)

### Manual Testing

| Feature test                                                                                                       | Test carried out                                                                                                                               | Expected outcome                                                                                                                                                                 | pass |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Player 1 username input                                                                                            | Various input values passed to the input                                                                                                       | Player 1 name should only be accepted if user inputs a string value                                                                                                              | Pass |
| Player 1 asked if they are playing against a human or PC                                                           | Player 1 is presented with an input field only yes or no answers accepted                                                                      | Input field only accepts yes and no value so does not proceed until it has one of those                                                                                          | Pass |
| Player 2 username input                                                                                            | Various input values passed to the input                                                                                                       | Player 2 name should only be accepted if user inputs a string value                                                                                                              | Pass |
| PC auto selected as player 2                                                                                       | Entered the value of no into the input when asked if playing against human                                                                     | Player 2 is automatically given the pre-selected PC name and the variable human has a value of false                                                                             | Pass |
| Rules appear on screen after player selection                                                                      | Run the game and complete player selection                                                                                                     | Once player selection is completed, rules automatically appear                                                                                                                   | Pass |
| Players asked if they are ready to pick Pokémon                                                                    | Onscreen input appears and user inputs a value of fight or exit                                                                                | If user inputs exit, game ends. If user inputs fight, user is taken to Play_game function                                                                                        | Pass |
| An instance of the player class is created and stored as a value of player 1 and the pick Pokémon method is called | User inputs the value fight which calls play_game function and inside that function the instance object is created which contains pick_pokemon | The player object is created and the pick_pokemon function will be called. The User is then greeted with a print statement showing the Pokémon to select from and an input field | Pass |
| User inputs Pokémon name, Pokémon details appear                                                                   | Typed in different names and then typed in different Pokémon names in input field                                                              | When user inputs incorrect name they are informed of this, if user inputs correct name Pokémon details appear                                                                    | Pass |
| User asked if they wish to add a selected Pokémon to their party                                                   | Input field appears looking for a yes or no answer                                                                                             | If user presses yes Pokémon added to battle pack and if no user taken to initial screen asking for Pokémon name                                                                  | Pass |
| Pokémon picker to loop until user has selected 3 Pokémon for battle pack                                           | Input 5 Pokémon names but only add Pokémons 1, 4 and 5                                                                                         | Pokémon picker should only complete once user has added 3 Pokémon even if they are not the first 3 names reviewed                                                                | Pass |
| When player 2 is the PC, player 2 will automatically select battle Pokémon                                         | Change the variable human to false                                                                                                             | Pick Pokémon is called and as human has a value of false this automatically runs the pick Pokémon method                                                                         | Pass |
| Method called first Pokémon in the battle class is called                                                          | Each player inputs a Pokémon name from their battle pack                                                                                       | An input field appears with a table above it showing the 3 Pokémon that player picked and asks the player to input a Pokémon name                                                | Pass |
| first Pokémon method picker validation                                                                             | Enter Pokémon name from player battle pack as well as other values                                                                             | Code should only proceed when user inputs a Pokémon name in that players battle pack, otherwise an error message should appear                                                   | Pass |
| Battle phase begins, screen shows each player’s name, Pokémon and Pokémon health                                   | Input an initial Pokémon for player 1 and 2                                                                                                    | Battle area should appear which shows each players names, Pokémon they have chosen and full health                                                                               | Pass |
| Attacker chooses an attack and defender health is reduced                                                          | Attacker inputs a number between 1 and 4                                                                                                       | When attacker inputs a number the attack value amount should then be reduced from the defender health                                                                            | Pass |
| Player 1 attack validation                                                                                         | Enter a number value as well as other data type                                                                                                | Error message should appear if user enters any other value other than 1 to 4                                                                                                     | Pass |
| After each attack, attacker and defender player and Pokémon, are switched                                          | Have the players Pokémon fight each other                                                                                                      | After each attack is completed and the defender’s health is deducted, player and Pokémon are repeatedly switched until defender Pokémon faints.                                  | Pass |
| Current Defender Pokémon faints, choose new Pokémon method called                                                  | Make defender Pokémon lose the battle                                                                                                          | When defender Pokémon has fainted battle phase should be paused and choose new Pokémon called                                                                                    | Pass |
| Human defender player asked to pick new Pokémon from battle pack                                                   | Human player Pokémon is made to lose the battle                                                                                                | A check is completed to see if the player whose Pokémon fainted is human before asking them to input the name of the next Pokémon to battle with                                 | Pass |
| Human player new Pokémon selection validation                                                                      | Tried to input a Pokémon name in player battle pack and random letter and number values                                                        | If any value is entered in the input other than the Pokémon in the players battle pack,an error is printed. Input will only accept and proceed with correct Pokémon name         | Pass |
| PC defender player picks new Pokémon from battle pack                                                              | PC player Pokémon is made to lose the battle                                                                                                   | A check is completed to see if the player whose Pokémon fainted is the PC, and then PC will also select next Pokémon to fight with                                               | Pass |
| All Pokémon of a player have fainted, game should end                                                              | When in the battle phase, ensured one player lost all battles                                                                                  | When a player has no Pokémon left to fight with, end game function should be called and break out of battle class                                                                | Pass |
| End game function called                                                                                           | Ensure a player loses the game                                                                                                                 | End game function is called and player 1 is asked if they wish to play again                                                                                                     | Pass |
| Player 1 in end game function is shown an input to play again or quit                                              | A player is made to lose the game                                                                                                              | When a player has no Pokémon left to battle with end game function is called and an input appears for player 1 asking to play again                                              | Pass |
| Player 1 end game validation                                                                                       | Tried to input a variety of values                                                                                                             | If any value is entered in the input other than yes or no, error is outputted                                                                                                    | Pass |
| Game ends                                                                                                          | End game function is called and value inputted                                                                                                 | Inside the end game function, the user inputs No and the game ends with a goodbye message                                                                                        | Pass |
| Check player wants to restart game                                                                                 | End game function is called and value inputted                                                                                                 | Inside end game function, user inputs yes which then triggers a second input to appear on screen                                                                                 | Pass |
| Confirmation if player 2 is human or PC before game restart                                                        | Player 1 given an input choice of yes or no                                                                                                    | Player 1 is shown an input which accepts a value of yes or no. If player 1 inputs ‘no’, player 2 is updated as PC,. If player 1 inputs ‘yes’, player 2 is asked for their name.  | Pass |
| Player 2 name input validation for human player                                                                    | Tried to input a variety of values                                                                                                             | Player 2 name should only be accepted if user inputs a string value for player name                                                                                              | Pass |
| Player 2 selection confirmed, game restarts and players taken to choose battle Pokémon function                    | Confirm game to restart and select player 2                                                                                                    | After player 2 has been chosen, play_game function is called and players asked to choose pokemon in battle pack                                                                  | Pass |

## Deploying the Website to GitHub Pages

- The website was deployed to GitHub Pages using the following steps:
- In the GitHub repository, go to the "Settings" tab.
- From the left-side menu, select 'Pages.'
- In the source section drop-down menu, choose the 'main' branch.
- Click 'Save.'
- Upon successful publishing, a live link will be displayed in a green banner.

### To deploy on Heroku:

- Log in to Heroku - or set up a new account.
- From the dashboard, click 'Create new app'.
- Name your app - it will need to be unique. Select Region, then 'Create'.
- Click on the 'Settings' tab.
- Scroll down to Config Vars and click 'Reveal Config Vars'.
- In the 'Key' field enter 'PORT', and in the 'Value' field enter '8000'.
- If there is a credentials file, this will also need to be entered into the Config Vars setting.
- Staying within 'Settings', scroll down to Buildpacks and click on 'Add Buildpacks'.
- Select 'python' first and click 'Save changes'.
- Then do the same again and this time select 'nodejs' and click 'Save changes'.
- Ensure the buildpacks are in the order of python first and nodejs second.
- Scroll to the top and select 'Deploy'.
- In 'Deployment method' select 'GitHub' and confirm you want to connect.
- Enter your GitHub repository into the search bar, and then 'Connect'.
- Under 'Automatic deploys', click on 'Enable Automatic Deploys' if you want the app to update every time you push changes to GitHub.
- Finally, click on 'Deploy Branch' under 'Manual deploy' to deploy your app. Once completed, you will be able to view your deployed link.

### Cloning the Repository

- Click on the "Code" button located near the top right corner of the page.
- Copy the HTTPS or SSH URL displayed.
- Open your terminal (or Git Bash on Windows) and navigate to your desired directory.
- Enter "git clone" followed by a space, and paste the copied URL.
- Press enter to execute the command, creating a local copy of the GitHub repository.
- You now have the GitHub repository cloned to your local machine.

## Credit and Content

**Youtube Courses**

- Bro Code

  - Python Course - https://www.youtube.com/watch?v=XKHEtdqhLK8&ab_channel=BroCode

- Tech With Tim

  - Python Object Oriented Programming - https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim

- Clear Code

  - The complete guide to Python - https://www.youtube.com/watch?v=mDKM-JtUhhc&ab_channel=ClearCode

- Codecademy

  - Learn Python 3 - https://www.codecademy.com/catalog/language/python
