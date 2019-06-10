import os
import pickle
import monster_manager

# Creates storage file if there isn't one
cwd = os.getcwd()
storage_filename = "bin_scenes"
if storage_filename not in os.listdir(cwd):
    open(storage_filename, "x")
    pickle.dump({}, open(storage_filename, "wb"))


# SCENE SELECTION
def scene_select():
    scenes = pickle.load(open(storage_filename, "rb"))
    if len(scenes) == 0:
        print("You don't have any scenes right now! Let's make a new one:")
        scene_create()
    else:
        print("Please select a scene: (Type o for options.)")
        for scene_name in scenes:
            print("- " + scene_name)
        user_choice = input(">> ").lower()
        if user_choice == "q":
            print("Goodbye! \n\n")
            # Lets this fxn run to completion
        elif user_choice == "n":
            print("Okay, let's make a new scene then.")
            scene_create()
        elif user_choice == "d":
            scene_delete()
        elif user_choice == "o":
            print("Options:" +
                  "\n- n: create a new scene"
                  "\n- d: delete an existing scene"
                  "\n- o: options (you've figured this one out)"
                  "\n- q: quit program")
        elif user_choice not in scenes:
            print("Invalid scene name; try again. Type o for options.")
            scene_select()
        else:
            print("Alright; let's begin!")
            monster_manager.dndmm_main(user_choice, scenes[user_choice])  # ACTIVATES MAIN
            print("\nWelcome back to scene selection.")
            scene_select()


# SCENE CREATION
def scene_create():
    new_scene_name = input("What shall the name of this here scene be?\n"
                           ">> ").lower()
    if new_scene_name in ["n", "d", "o", "q", "nvm"]:
        print("Stop trying to break my program!\n")
        scene_create()
    else:
        scenes = pickle.load(open(storage_filename, "rb"))
        scenes[new_scene_name] = []
        pickle.dump(scenes, open(storage_filename, "wb"))
        print(new_scene_name + ". It has a woody sound. I like it.")
        scene_select()


# SCENE DELETION
def scene_delete():
    print("Which scene would you like to delete?")
    scenes = pickle.load(open(storage_filename, "rb"))
    for scene in scenes:
        print("- " + scene)
    user_choice = input(">> ").lower()
    if user_choice == "nvm":
        print("Aight thas cool")
        scene_select()
    elif user_choice in scenes:
        del scenes[user_choice]
        pickle.dump(scenes, open(storage_filename, "wb"))
        print("Done and done.")
        scene_select()
    else:
        print("Sorry, that's not a valid response. Please choose a scene, "
              "or type \"nevermind\".")
        scene_delete()


# Runs this shit
print("Welcome to this text-based D&D Monster Manager!\n"
      "You are currently in the scene select menu. "
      "Type d to delete a scene, n to create a new one, or q to quit.\n")
scene_select()

