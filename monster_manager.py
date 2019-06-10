# MONSTER MANAGER
# Manage your monsters in a bazillion easy steps!
import pickle
from monstermanager.Monster import Monster
from monstermanager.roll import roll
from copy import deepcopy


# MAIN — KEY HANDLER
def dndmm_main(scene_name, monsters):

    # Auto-save
    save(scene_name, monsters)

    # Show all active monsters
    print("\n")
    if len(monsters) > 0:
        print(scene_name.upper() + " monsters:")
        print_monsters(monsters)
    else:
        print("No monsters. (Only options that don't crash program are n, r, and q.)")

    # Accept user input
    user_input = input(">> ")

    if user_input in ["o", "options", "option"]:
        print("Options:"
              "\n- n to create a new monster"
              "\n- e to edit a monster"
              "\n- c to copy a monster"
              "\n- k to kill (remove) a monster"
              "\n- d to have a monster take damage"
              "\n- a to have a monster attack"
              "\n- ar to have a monster attempt to evade a PC attack"
              "\n- i to get info about a particular monster"
              "\n- r (and then the roll string) to roll dice"
              "\n- q to exit to scene selection")

    elif user_input in ["n", "new"]:
        monsters.append(Monster())

    elif user_input in ["c", "copy"]:
        print("Which monster would you like to copy?")
        copied_monster = deepcopy(choose_monster(monsters))
        copied_monster.edit()
        monsters.append(copied_monster)

    elif user_input in ["k", "kill"]:
        print("Select a monster to kill: ")
        monsters.remove(choose_monster(monsters))

    elif user_input in ["e", "edit"]:
        print("Which monster would you like to edit?")
        choose_monster(monsters).edit()

    elif user_input in ["d", "dmg", "damage"]:
        print("Which monster would you like to take damage?")
        choose_monster(monsters).take_damage(input("Enter \"[damage amount] [damage type]\" \n>> "))

    elif user_input in ["ar", "attack roll"]:
        print("Which monster is trying to evade an attack?")
        choose_monster(monsters).deal_with_attack(int(input("Enter PC attack: \n>> ")))

    elif user_input in ["a", "atk", "attack"]:
        print("Which monster would you like to perform an attack?")
        choose_monster(monsters).attack()

    elif user_input in ["i", "info"]:
        print("Which monster do you want info on?")
        choose_monster(monsters).print_info()

    elif user_input in ["r", "roll"]:
        print(roll(input("How much? \n>> ")))

    elif user_input not in ["q", "quit"]:
        print("Invalid command. Type \"o\" for options.")

    if user_input in ["q", "quit"]:
        print("See ya later!")
    else:
        dndmm_main(scene_name, monsters)


# *** HELPER FXNS *** #
# CHOOSE A MONSTER
def choose_monster(monsters):
    print_monsters(monsters)
    monster_choice = input(">> ")
    for monster in monsters:
        if monster.is_named(monster_choice):
            return monster
    print("Sorry, that's not a valid monster. Try again.")
    return choose_monster(monsters)


# PRINT MONSTERS
def print_monsters(monsters):
    for monster in monsters:
        monster.print_name_and_health()


# SCENE SAVING
def save(scene_name, monsters):
    storage_filename = "bin_scenes"
    scenes = pickle.load(open(storage_filename, "rb"))
    scenes[scene_name] = monsters
    pickle.dump(scenes, open(storage_filename, "wb"))
