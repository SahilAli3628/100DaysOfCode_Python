print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

      ''')

print("Welcome to the Treasure Island!!!\nLet's begin with out adventure!\nYour mission is to find the treasure, but be careful... because many have tried and lost their lives!!!\n")

print("You are walking down the path through the jungle which leads to the treasure, but you came across a crossroad")
direction = input("Do you go left or right? (left/right): ").lower()

if direction == 'right':
    print("You chose unwisely! you fell in a hole and broke your legs. With no way out of the hole, you died there GAME OVER!!!")
elif direction == 'left':
    print("As you carry on down the road, you come across a wide river with rapid currents. Looks like there is a boat that makes trips across the river frequently, but it just left from your side of the river")
    swim_or_wait = input("Do you swim across the river or do you wait for the boat? (swim/wait): ").lower()
    if swim_or_wait == 'swim':
        print("Sadly, you were attacked by a hover of angry trouts and were killed in your attempt to swim across the river. GAME OVER!!!")

    elif swim_or_wait == 'wait':
        print("You successfully crossed the river by the boat and continued on your journey. As you were moving along, the jungle got thicker and fog settled in making it harder to see what's coming ahead\nAfter a while, you come across a building... a stronghold of sorts which has 3 doors.\nFrom your research about this treasure island, you know that the treasure lies behind one of these doors.")

        door = input("Which door will you choose? (red/yellow/blue): ").lower()
        if door == 'red':
            print("You walk in the room with red door\nThe room had boobytraps that set the whole room on fire!\nYou burned to death. GAME OVER!!!")
        elif door == 'blue':
            print("You walk in the room with blue door\nThe room had boobytraps that set free a pack of wild beasts!\nYou were eaten by wild beasts with no chance to escape. GAME OVER!!!")
        elif door == 'yellow':
            print("Congratulations!!! You win!!!\nThe treasure is all yours!")
        else:
            print("You tried to outsmart the game master?! I strike you down with my fury!! GAME OVER!!!")
    
    else:
        print("You tried to outsmart the game master?! I strike you down with my fury!! GAME OVER!!!")
else:
    print("You tried to outsmart the game master?! I strike you down with my fury!! GAME OVER!!!")
