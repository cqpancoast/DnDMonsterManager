from monstermanager.roll import roll


# Represents a monster and its various stats and characteristics
class Monster:

    """ DATA CONTAINED:
        - String name
        - int health
        - int max_health
        - int armor_class
        - {String, int} stats
        - {String, {String, String}} attacks
        - [String] tags
        - String note
    """

    # Totally new monster constructor
    def __init__(self):

        self.name = input("name: ")
        mh_input = input("max health (# or XdX+X): ")
        if "d" in mh_input:
            self.max_health = roll(mh_input)
            print("  rolled max health: " + str(self.max_health))
        else:
            self.max_health = int(mh_input)
        self.health = self.max_health
        self.ac = int(input("armor class: "))
        self.speed = input("base speed: ")

        self.attacks = {}
        user_response = "y"
        while user_response == "y":
            user_response = input("Would you like to add an attack? (y/n) \n>> ")
            if user_response != "y":
                print("Got it; we'll be done with attacks then.")
            else:
                attack_name = input("What should this attack be named? \n>> ")
                self.attacks[attack_name] = {}
                self.attacks[attack_name]["damage roll"] = input("How much damage? (XdX+X format) \n>> ")
                self.attacks[attack_name]["damage type"] = input("What kind of damage? \n>> ")
                self.attacks[attack_name]["description"] = input("Attack description? \n>> ")
                self.attacks[attack_name]["attack mod"] = int(input("Attack bonus? \n>> +"))

        self.tags = []
        user_response = "y"
        while user_response == "y":
            user_response = input("Would you like to add a tag? (y/n) \n>> ")
            if user_response != "y":
                print("Got it; we'll be done with tags then.")
            else:
                self.tags.append(input("Input tag to add: \n>> "))

        self.note = input("Any notes? \n>> ")

    def edit(self):
        print("If you don't want to edit a field, simply press enter to move along.")
        name_input = input("name: " + self.name + " -> ")
        if name_input.replace(" ", "") != "":
            self.name = name_input
        mh_input = input("max health: " + str(self.max_health) + " (# or XdX for reroll) -> ")
        if mh_input.replace(" ", "") != "":
            if "d" in mh_input:
                self.max_health = roll(mh_input)
                print("  rolled max health: " + str(self.max_health))
            else:
                self.max_health = int(mh_input)
        health_input = input("health: " + str(self.health) + " -> ")
        if health_input.replace(" ", "") != "":
            self.health = int(health_input)
        ac_input = input("armor class: " + str(self.ac) + " -> ")
        if ac_input.replace(" ", "") != "":
            self.ac = int(ac_input)
        speed_input = input("speed: " + self.speed + " -> ")
        if speed_input.replace(" ", "") != "":
            self.speed = speed_input

        attack_choice = "y"
        while attack_choice == "y":
            print("Would you like to add an attack or remove an attack? (a/r/n)")
            for attack in self.attacks:
                print("- " + attack)
            attack_input = input(">> ")
            if attack_input == "a":
                attack_name = input("What should this attack be named? \n>> ")
                self.attacks[attack_name] = {}
                self.attacks[attack_name]["damage roll"] = input("How much damage? (XdX+X format) \n>> ")
                self.attacks[attack_name]["damage type"] = input("What kind of damage? \n>> ")
                self.attacks[attack_name]["description"] = input("Attack description? \n>> ")
                self.attacks[attack_name]["attack mod"] = int(input("Attack bonus? \n>> +"))
            elif attack_input == "r":
                print("Which attack would you like to remove?")
                for attack in self.attacks:
                    print(attack)
                attack_to_rm = input(">> ")
                if attack_to_rm in self.attacks:
                    self.attacks.pop(attack_to_rm)
                else:
                    print("Sorry, that attack doesn't exist.")
            else:
                attack_choice = "n"

        tag_choice = "y"
        while tag_choice == "y":
            tag_input = input("Would you like to add a tag or remove a tag? (a/r/n) \n>> ")
            if tag_input == "a":
                self.tags.append(input("What tag are you adding? \n>> "))
            elif tag_input == "r":
                self.tags.remove(input("Which tag would you like to remove? \n>>"))
            else:
                tag_choice = "n"

        note_input = input("note: " + self.note + " -> ")
        if note_input.replace(" ", "") != "":
            self.note = note_input

    def has_tag(self, tag):
        return tag in self.tags

    def set_tag(self, tag):
        if tag in self.tags:
            return
        else:
            self.tags.append(tag)

    def is_named(self, name):
        return name == self.name

    def is_hit(self, hit_value):
        return hit_value > self.ac

    def print_info(self):
        print("\nname: " + self.name +
              "\nhealth: " + str(self.health) + "/" + str(self.max_health) +
              "\narmor class: " + str(self.ac) +
              "\nspeed: " + str(self.speed))
        print("attacks: ")
        for attack in self.attacks:
            print("- " + attack)
            print("  - " + self.attacks[attack]["damage roll"]
                  + " " + self.attacks[attack]["damage type"])
            print("  - +" + str(self.attacks[attack]["attack mod"]) + " atk bonus")
            print("  " + self.attacks[attack]["description"])
        print("tags: ")
        for tag in self.tags:
            print("- " + tag)
        print("note: " + self.note)

    def print_name_and_health(self):
        print(self.name + " - " + str(self.health) + "/" + str(self.max_health) + "hp")

    def take_damage(self, damage_string):

        damage_set = damage_string.split(" ")
        if len(damage_set) != 2:
            print("Sorry; I don't understand. No damage will be dealt.")
            return
        base_damage = int(damage_set[0])
        damage_type = damage_set[1]

        if self.has_tag(damage_type + " immune"):
            damage_done = 0
            print(self.name + " is immune to " + damage_type + " damage.")
        elif self.has_tag(damage_type + " resistant"):
            damage_done = (base_damage / 2).__floordiv__()
            print(self.name + " is resistant to " + damage_type + " damage.")
        elif self.has_tag(damage_type + " weak"):
            damage_done = base_damage * 2
            print(self.name + " is weak to " + damage_type + " damage.")
        else:
            damage_done = base_damage

        self.health -= damage_done
        print(self.name + " just took " + str(damage_done) + " damage...")
        if self.health < 0:
            print("...and is totally fuckin' dead.")
            self.set_tag("dead")
        else:
            print("...and seems to still be standing.")

    def deal_with_attack(self, player_attack_roll):
        if self.ac <= player_attack_roll:
            self.take_damage(input("The PC hit! How much damage was done (and what kind)? \n>> "))
        else:
            print(self.name + " has avoided taking harm.")

    def attack(self):
        print("Which attack would you like this monster to preform?")
        for attack in self.attacks:
            print("- " + attack)
        attack_choice = input(">> ")
        for attack in self.attacks:
            if attack == attack_choice:
                if input("Does " + str(roll("1d20") + self.attacks[attack]["attack mod"]) +
                         " break the PC's armor class? (y/n) \n>> ") \
                        != "y":
                    print(self.name.upper() + "'s " + attack.upper() + " attack has failed!")
                    return
                print("\n" + attack.upper() + ":")
                print(str(roll(self.attacks[attack]["damage roll"])) + " " + self.attacks[attack]["damage type"])
                print(self.attacks[attack]["description"])
                return
        print("Sorry, that's not a valid attack. No attack was rolled.")

