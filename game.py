import time
import random

import monster
import player

default_interval = 0.05

def print_slow(*strings, interval=default_interval, end="\n", end_wait=1):
    for string in strings:
        for char in string:
            print(char, end="", flush=True)
            time.sleep(interval)
    time.sleep(end_wait)
    print(end=end)

def input_slow(text, interval=default_interval, end="\n"):
    print_slow(text, interval=interval, end=end, end_wait=0)
    result = input()
    return result

# Loops questions until given yes or no input, prints response for either input
def ask_user_yn (question, yes, no):
    # loop and a half
    answer = input_slow(question+"\n(yes/no)").lower()
    while answer != "yes" and answer != "no":
        print_slow("Sorry, please answer 'yes or 'no'")
        answer = input_slow(question+"\n(yes/no)").lower()
    if answer == "yes":
        print_slow(yes)
    else:
        print_slow(no)
    # Returning True if answer is "yes" and False if "no"
    return answer == "yes"

# Will make a function for only accepting one response
def forced_answer(question, correct, incorrect, correct_response, incorrect_response):
    answer = ""
    while answer.lower() != correct:
        answer = input_slow(question+"\n"+"("+correct+"/"+incorrect+")")
        if answer == correct:
            print_slow(correct_response)
        if answer == incorrect:
            print_slow(incorrect_response)

def choice(question, choices):
    print_slow(question)
    choices_str = "\n".join(choices)

    choice = input_slow(f"Select:\n{choices_str}", end="\n").lower()
    while choice not in choices:
        print_slow("Sorry, that choice is not available")
        choice = input_slow(f"Select:\n{choices_str}", end="\n").lower()
    
    return choice

def try_int(string):
    try:
        return int(string), True
    except:
        return 0, False

def num_choice(question, choices):
    print_slow(question,"Select a number:")

    for i in range(len(choices)):
        print_slow(f"({i + 1}) {choices[i]}", interval=0.05)

    choice, success = try_int(input())

    while not success or choice not in range(1, len(choices) + 1):
        print_slow("Sorry, that choice is not available")
        for i in range(len(choices)):
            print(f"({i + 1}) {choices[i]}")
        choice, success = try_int(input())
    return choices[choice - 1]

def hazard_select():
    result = input_slow("Pick a number between 1 and 3: ")
    return result

def main():
    #The Treasure Chest
    # open_chest1 = input_slow("You see a treasure chest next to the wall. Do you open it? ")
    # if open_chest1.lower() == "yes":
    #     print_slow("You open the chest. Inside you see the following items: ")
    #     treasure_chest = ["diamonds", "gold", "silver", "sword"]
    #     for treasure in treasure_chest:
    #         print_slow(treasure)

    # N# print_slow(f"You go {direction}")
    

    #collecting basic info from the player
    player_name = input_slow("Hello. What is your name? " )
    print_slow(f"Wow, what a great name! Nice to meet you, {player_name}." )
    new_monster = monster.Griffin()   
    enemy = player.Player(10,15,30,player_name)

    new_monster.attack(enemy,5)

    # pnoun = input_slow("What is your prefered pronoun (him, her, they)? " )
    hazard_choice = hazard_select()
    if hazard_choice == "1":
        hazard = "you trip over a beehive. Bees immediately begin to swarm around your legs, stinging you. "
    elif hazard_choice == "2":
        hazard = "you feel your feet become lodged in a patch of quicksand.\nThe shore doesn't look that far away.\nAbove you is mass of thorny brambles."
    elif hazard_choice == "3":
        hazard = "you feel a crunch beneath your feet, and the cave echoes with a large 'SNAP'."
    
    fav_clr = input_slow("What is your favorite color? " )
    location = input_slow("Pick an interesting outdoor location: ")
    # spir_aml = input_slow("What is your spirit animal? " )


    #Game begins
    print_slow(f"It is such a lovely day, you decide to go to the {location}.")
    print_slow(f"As you are walking in the {location}, you notice a large cave up ahead.")
    # enter_cave = input_slow("Would you like to enter the cave? ")

    answer = ask_user_yn("Would you like to enter the cave? ","You enter the cave. You are immediately covered in darkness.",f"You tell that cave to fuck off, and continue walking in the {location}.")

    if not answer:
        print_slow("T H E  E N D",interval=.1)
        exit()


    answer = ask_user_yn("Do you light your torch?",f"You remove your {fav_clr} lighter, and light that motherfucker up.","You do not light your torch.")


    if answer:
        print_slow("With the light from your torch surrounding you, you realize the cave is larger than you thought.")
        print_slow("A little ways into the cave you notice a fork in the path. ")
        input_slow("Do you pick up the fork? ")
        num_choice("Just kidding, it's actually a left/right juncture. Which way will you go?\n",["left","right"])
        print_slow("As you proceed down the cramped passageway, you see a crumpled shape on the ground.\nAs you get closer you realise it is a pile of clothing and bones.")
        ask_user_yn("Do you inspect the bones?","The top of the skull appears to have two puncture marks, and there are large claw marks on the wall.","You walk past the bones and continue down the dimly lit passageway.")
        
    else:
        print_slow("It is dark and scary in the cave because you can't see.")
        print_slow(f"As you stumble around in the dark, {hazard}")
        if hazard_choice == "1":
            forced_answer("Do you swat at the bees?","no","yes","As you remain calm, the bees eventually realize you pose no threat, and fly away.","You swat at the swarm of bees, but unfortunately that only seems to upset them more. The bees continue to sting you.")
        elif hazard_choice == "2":
            forced_answer("Do you reach for the brambles or swim for the shore?","reach","swim","You reach out your hand, and are just barely able to grasp a low hanging vine. Pain shoots through your hands as the spikes puncture your skin. You managed to pull yourself far enough to reach the shore.","You struggle against the thick sand, but you are unable to move in any direction.")
        elif hazard_choice == "3":
            bone_pickup = ask_user_yn("Do you pick up the mysterious object?","You reach down and pick it up. You hold it close to your face and realize it is a human jaw!","You decide to leave it be, and continue on.")
            if bone_pickup == True:
                print("Under closer inspection, you notice the skull it was attached to before you stepped on it.\nThe skull is missing most of its teeth, and there are two large puncture holes in the top of the head.")




if __name__ == "__main__":
    main()
