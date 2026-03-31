# import alchemy.grimoire as grimoire
from alchemy.spells import Spell
from alchemy.elements import Element, init_base_elements
# import alchemy.elements as elements
# import alchemy.potions as potions
import time
import os
import sys


# print("\033[2J\033[H\033[?25l", end="", flush=True) (clears the command
# prompt and hides the cursor)
# print("\033[2J\033[H", end="", flush=True) (clears the command prompt)
# print("\033[F\033[2K" * n, end="", flush=True) (clears n amount of lines
# starting from the current one)


ElementList = list[list[str, tuple[int, int, int]]]


class Spellbook:
    def __init__(self, owner: str, type: str, NPC: bool) -> None:
        self.owner = owner
        self.spells = []
        self.potions = []
        self.NPCmade = NPC
        self.name = type.capitalize()
        self.type = self.book_type(type)

    def book_type(self, type: str) -> None:
        if type == "fire":
            self.type = "Grimoire"
        elif type == "water":
            self.type = "Tome"
        elif type == "earth":
            self.type = "Spellbook"
        elif type == "air":
            self.type = "Codex"

    def add_spell(self, spell: Spell) -> None:
        self.spells.append(spell)
        print(f"Successfully added the spell: {spell.name}")

    def list_spells(self) -> None:
        print(f"Your {self.type} contains {len(self.spells)} spells:")
        for spell in self.spells:
            print(f"- {spell.name}: {spell.components}")

    def remove_spell(self) -> None:
        try_again = ""
        error = False
        i = 1
        print("Which spell would you like to remove?\n")
        for spell in self.spells:
            print(f"- [{i}] {spell.name}: {spell.components}")
            i += 1
        try:
            to_remove = int(input("\nSpell to remove: "))
            if to_remove > len(self.spells):
                raise ValueError
            self.spells.remove(self.spells[to_remove - 1])
        except ValueError:
            print("Error - Spell not found")
            error = True
        finally:
            if error is True:
                print()
                try_again = str.lower(input("Would you like to try again?: "))
                if try_again == "y":
                    self.remove_spell()

    def change_name(self, name: str) -> None:
        self.name = name.title()


class Mage:
    def __init__(self, name: str, focus: list) -> None:
        self.name = str.casefold(name)
        self.focus = focus
        self.spellbook = Spellbook(self.name, self.focus[0], False)
        self.level = 0
        self.m_class = "Mage"
        self.library = []
        self.known_elements = []

    def set_name(self, name: str) -> None:
        self.name = str.casefold(name)

    def you(self) -> str:
        return str.capitalize(self.name)

    def type(self) -> str:
        return (self.focus[1] + str.capitalize(self.focus[0]) + "\x1b[0m")

    def change_spellbook(self, spellbook: Spellbook) -> None:
        if spellbook not in self.library:
            self.add_spellbook(spellbook)
        self.spellbook = spellbook

    def add_spellbook(self, spellbook: Spellbook) -> None:
        self.library.append(spellbook)

    def list_library(self) -> None:
        print("You look at the current books in your library:")
        print()
        for book in self.library:
            print(f"- {book.name} ({book.type}):"
                  f"\nNumber of spells: {len(book.spells)}"
                  f"\nWriter: {book.owner}")
            print()

    def discover_e(self, element: list) -> None:
        self.known_elements.append(element)


class Player:
    def __init__(self, character: Mage, os: str) -> None:
        self.char = character
        self.char_list = []
        self.os = os

    def wipe(self) -> None:
        if self.os == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def change_mage(self, character: Mage) -> None:
        self.char = character


def intro(user: Player) -> None:
    print("\033[?25l", end="")
    print(f"Welcome, mage {user.char.you()}!")
    time.sleep(1.5)
    print("\nYou have been registered as a level "
          f"{user.char.level} {user.char.type()} {user.char.m_class}!")
    time.sleep(1.5)
    print("\nHere in your library, you will learn how to brew potions, "
          "as well spellcrafting.")
    time.sleep(1.5)
    print("\nEverything in this world has a magical element attached to it, "
          "which you will discover through your journey.")
    time.sleep(1.5)
    print("\nIf you ever hit a roadblock, remember to"
          " use the ever so helpful 'HELP' spell")
    print("We, great mages and alchemists of the council welcome you"
          " into the world of magic with open arms."
          "\nMay you make the best of your time here."
          "\n\n(Press [ENTER] to continue)")
    input("\n")
    print("\033[?25h")


def first_boot(e_list: Element, user: Player) -> None:
    username = None
    valid_input = False
    while username == "" or username is None:
        user.wipe()
        if username == "":
            print("Name cannot be empty!\n")
        username = str.casefold(input("What is your name: "))
    user.wipe()
    print(f"Wonderful! Glad to meet you, {str.capitalize(username)}")
    print()
    while True:
        if valid_input is False:
            print("Here are your starting magical foci:")
        print()
        e_list.list_elements()
        print()
        focus = str.casefold(input("What is your magical focus: "))
        if focus in e_list.elements:
            user.wipe()
            user.change_mage(Mage(username, e_list.elements[focus]))
            user.char.change_spellbook(Spellbook(user.char.name,
                                                 user.char.focus[0],
                                                 False))
            return
        if valid_input is False:
            valid_input = True
        user.wipe()
        print("That is not one of the valid basic magical foci:")


def empty_mage() -> Mage:
    empty_mage = Mage("effigy", ["none", "\x1b[0m"])
    return empty_mage


def main(user: Player, all_elements: dict[Element]) -> None:
    command = ""
    valid_commands = ["add_element",
                      "check_element",
                      "add_spell",
                      "check_spell",
                      "remove_spell",
                      "check_stats",
                      "help",
                      "quit"]
    while True:
        command = str.casefold(input("What will you do?: "))
        user.wipe()
        if command in valid_commands:
            if command == "add_element":
                n_ele_name = ""
                # n_ele_colors = ""
                print("Adding a new element...\n")
                elements["all_elements"].list_elements
                print("\nPlease don't try to reinvent one of the already "
                      "existing elements... This is for both "
                      "your and our safety!")
                while n_ele_name == "":
                    n_ele_name = str.casefold(input(""))
            if command == "add_spell":
                spellname = ""
                spellcomp = ""
                while spellname == "":
                    spellname = input("What's the name of the spell "
                                      "you'd like to create?: ")
                    if spellname == "":
                        user.wipe()
                        print("The spell must have a name!")
                while spellcomp == "":
                    spellcomp = str.split(input("What do you cast it "
                                                "with?: "), " ")
                    if spellcomp == "":
                        user.wipe()
                        print("The spell must have components!")
                user.char.spellbook.add_spell(Spell(spellname,
                                                    user.char.name,
                                                    spellcomp))
            if command == "check_spell":
                user.char.spellbook.list_spells()
            if command == "remove_spell":
                if len(user.char.spellbook.spells) > 0:
                    user.char.spellbook.remove_spell()
                else:
                    print("Your spellbook has no spells! "
                          "Create one using 'add_spell'")
            if command == "check_stats":
                print("This is a WIP")
                print()
            if command == "help":
                print("HELP SPELL! The current available commands are:")
                print()
                print(" 'add_element' - Allows you to create a new element!")
                print(" 'check_element' - Checks which elements you've "
                      "discovered so far")
                print(" 'add_spell' - Allows you to add a spell to your "
                      "current spellbook!")
                print(" 'check_spell' - Checks the spells on your current "
                      "spellbook")
                print(" 'remove_spell' - Removes a spell from your current "
                      "spellbook")
                print(" 'check_stats' - Checks your stats (level, spells "
                      "created, spells casted, etc...)")
                print(" 'help' - Brings up the command list (Hi!)")
                print(" 'quit' - Quits this plane of existance "
                      "(Please don't go :c)")
                print()
                print("Spell manipulation tip: To prevent maigc thievery, "
                      "it is forbidden to write on Spellbooks you don't own.")
            if command == "quit":
                print("Good night...")
                sys.exit(1)
        else:
            print(f"Invalid command {command}. Use 'help' if you're stuck")
        print()


if __name__ == "__main__":
    try:
        user = Player(empty_mage(), os.name)
        elements = init_base_elements()
        first_boot(elements["basic_elements"], user)
        # intro(user)
        user.wipe()
        main(user, elements)
    except KeyboardInterrupt:
        user.wipe()
        print("See you later!")


# print("This is \x1b[38;2;142;194;21mLIME GREEN\x1b[0m text")
# print("This is \x1b[48;2;194;21;139mROSA\x1b[0m background")
# \x1b[ starts the sequence
# 38;2; or 48;2; are foreground and background respectively
# x;y;z are the colors from 0 to 255
