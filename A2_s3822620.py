# COSC1519 Introduction to Programming
# Student name: Prottay Karim
# Student number: S3822620
# Practical group:
# Friday 2:30pm (online)

# Game Introduction
# Declaring variables used later in game
player_health = 10
monster_health = 10
enemies = 'sea monster'.title()
weapons = ['cannons', 'guns', 'arrows', 'mortars']

# Asking for player name and age
name = input("Welcome to the Caribbeans! What is your name captain?\n").title()
age = float(input("What is your age?"))
# loop to check for age and bots
if age < 3.5:
    print("You are lying!")
    exit()
elif age < 7:
    print("Welcome to the game")
elif age < 15.5:
    print("Hope you like this game")
elif age > 15.5:
    print("Aren't you a bit old to play this game?")
else:
    question = input("Are you a robot?(Y/N").lower().strip()
    if question == 'n':
        print("Continue!")
    else:
        print("Please start over and verify properly")
        exit()
# Asking player to choose their character
# making sure it handles unexpected type of user input
print("")
try:
    character_num = int(input("Choose your secretary!(Enter a number)\n1. Wood Legs\n2. Black Beard\n3. Sea Lord\n"))
except ValueError:
    print("Please enter 1, 2 or 3")
    exit()
# Chained condition to select player's character
if character_num == 1:
    character_name = "Wood Leg"
elif character_num == 2:
    character_name = "Black Beard"
else:
    character_name = "Sea Lord"
# Story introduction
print("Welcome", name, "I am your secretary", character_name, "The Pirate\nLet us begin!")
# easing users to the game by simple typing practice
# allowing users to fill up food list
foods = []
characters = [name, character_name, 'Sailors']
food_choice = input("What is your favorite food?")
snack_choice = input("What else?")
print("Me Too!!")
foods.append(food_choice)
foods.append(snack_choice)
# nested conditional to print everyone's food
for food in foods:
    for character in characters:
        print(character, "ate a", food)

print("Now that everyone is full.\n Let's Begin!")
print("\nIt's a stormy night in the caribbean sea and Captain", name, "\nis commanding the ship. "
                                                                      "Suddenly,", character_name,
      "notices that the \nwaves are getting higher!")
print("")
# Adventure Begins
print("One of the sailor screams out that he sees a monster!\nIn front of the ship you see a huge", enemies)

option = True
# This loop asks the player for options and forces them to input Fight.
while True:
    first_option = int(input("What do you want to do?\n1. Retreat!\n2. Fight!\n"))
    if first_option == 2:
        option = True
        break
    else:
        print("Oh no! The monster will attack you from behind")
        option = False
print("Here are your weapons: ")
# Simple loop to print weapons list
for weapon in weapons:
    print(weapon.title())
print("")
# Loop to fighting, using items on list and continue till health drops to 0.
while monster_health > 0 and player_health > 0:
    print("Your current health level is: ", player_health)
    print("The monster's health is: ", monster_health)
    weapon_choice = input("Choose your weapon!\nWrite the name of your weapon:\n").lower().strip()
    if weapon_choice in weapons:
        monster_health = monster_health - 5
        player_health = player_health - 3
    else:
        player_health = player_health - 5
# Ending
# Nested conditions to allow leading to alternate endings
if player_health == 0:
    print("Ship has sustained critical damage")
    print("Game Over!")
elif monster_health == 0:
    print("The monster is dead!")
    choice = input("Do you want to go leave or check the remains?(leave/check)\n").lower().strip()
    if choice == "check":
        print("You have checked the dead monster and \n", character_name, " notice a pot of gold in it's mouth")
        choice = input("Do you want to send someone to bring it to you?(yes/no)\n").lower().strip()
        if choice == "yes":
            print("A sailor goes in to bring the gold but he dies!!")
            print("It's not good to be greedy children! Look you've just killed a man")
            print("Game Over!")
        else:
            print("You continue your journey through the caribbeans again! Congratulations")
            print("Game Over!")
    else:
        print("You continue your journey through the caribbeans again! Congratulations")
        print("Game Over!")
else:
    print("Both of you have died in the fight!")
# Ending and exiting game
print("Thank you for playing!")
input("\nPress <enter> to exit!\n")
exit()
