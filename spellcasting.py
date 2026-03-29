# import alchemy.grimoire as grimoire
from alchemy.elements import Element
# import alchemy.elements as elements
# import alchemy.potions as potions
import time
import os


# print("\033[2J\033[H\033[?25l", end="", flush=True) (clears the command
# prompt and hides the cursor)
# print("\033[2J\033[H", end="", flush=True) (clears the command prompt)
# print("\033[F\033[2K" * n, end="", flush=True) (clears n amount of lines
# starting from the current one)


ElementList = list[list[str, tuple[int, int, int]]]


class Spellbook:
    def __init__(self, owner: str, type: str) -> None:
        self.owner = owner
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


class Mage:
    def __init__(self, name: str, focus: list) -> None:
        self.name = str.casefold(name)
        self.focus = focus
        self.spellbook = Spellbook(self.name, self.focus)
        self.level = 0
        self.m_class = "Mage"

    def set_name(self, name: str) -> None:
        self.name = str.casefold(name)

    def you(self) -> str:
        return str.capitalize(self.name)

    def type(self) -> str:
        return (self.focus[1] + str.capitalize(self.focus[0]) + "\x1b[0m")


class Player:
    def __init__(self, character: Mage, os: str) -> None:
        self.char = character
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
    print("\nEverything in this world has a magical element attached to it,"
          "which you will discover through your journey.")
    time.sleep(1.5)
    print("\nIf you ever hit a roadblock, remember to"
          " use the ever so helpful 'HELP' spell")
    print("We, great mages of the council welcome you"
          " into the world of magic with open arms."
          "\nMay you make the best of your time here."
          "\n\n(Press [ENTER] to continue)")
    input("\n")
    print("\033[?25h")


def first_boot(e_list: Element, user: Player) -> None:
    # valid_foci = {"fire": "\x1b[38;2;227;59;59mfire\x1b[0m",
    #               "water": "\x1b[38;2;157;198;252mwater\x1b[0m",
    #               "earth": "\x1b[38;2;135;113;84mearth\x1b[0m",
    #               "air": "\x1b[38;2;140;222;158mair\x1b[0m"}
    username = None
    valid_input = False
    while username == "" or username is None:
        user.wipe()
        if username == "":
            print("Name cannot be empty!\n")
        username = str.casefold(input("What is your name: "))
    print()
    while True:
        focus = str.casefold(input("What is your magical focus: "))
        if focus in e_list.elements:
            user.wipe()
            user.change_mage(Mage(username, e_list.elements[focus]))
            return
        if valid_input is False:
            user.wipe()
            valid_input = True
        else:
            user.wipe()
        print("That is not one of the valid basic magical foci:")
        e_list.list_elements()


def empty_mage() -> Mage:
    empty_mage = Mage("effigy", ["none", "\x1b[0m"])
    return empty_mage


# def main(user: Player, all_elements: Element) -> None:
#    command = ""
#    while True:


if __name__ == "__main__":
    user = Player(empty_mage(), os.name)
    all_elements = Element()
    basic_elements = Element()
    first_elements = [["fire", (227, 59, 59)],
                      ["water", (157, 198, 252)],
                      ["earth", (135, 113, 84)],
                      ["air", (140, 222, 158)],]
    for e in first_elements:
        all_elements.add_element(e[0], e[1])
        basic_elements.add_element(e[0], e[1])
    first_boot(basic_elements, user)
    print()
    intro(user)
    user.wipe()


# print("This is \x1b[38;2;142;194;21mLIME GREEN\x1b[0m text")
# print("This is \x1b[48;2;194;21;139mROSA\x1b[0m background")
# \x1b[ starts the sequence
# 38;2; or 48;2; are foreground and background respectively
# x;y;z are the colors from 0 to 255
