# import alchemy.grimoire as grimoire
# import alchemy.elements as elements
# import alchemy.potions as potions
import time
import os


# print("\033[2J\033[H\033[?25l", end="", flush=True) (clears the command
# prompt and hides the cursor)
# print("\033[2J\033[H", end="", flush=True) (clears the command prompt)
# print("\033[F\033[2K" * n, end="", flush=True) (clears n amount of lines
# starting from the current one)


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
    def __init__(self, name: str, focus: str):
        self.name = str.casefold(name)
        self.focus = str.casefold(focus)
        self.spellbook = Spellbook(self.name, self.focus)
        self.level = 0
        self.m_class = "Mage"

    def you(self) -> str:
        return str.capitalize(self.name)

    def type(self) -> str:
        return str.capitalize(self.focus)


def intro(user: Mage) -> None:
    print("\033[?25l", end="")
    print(f"Welcome, mage {user.you()}!")
    time.sleep(1.5)
    print("\nYou have been registered as a level "
          f"{user.level} {user.type()} {user.m_class}!")
    time.sleep(1.5)
    print("\nHere in your library, you will learn how to brew potions,"
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
    input("")
    print("\033[?25h")


def first_boot() -> Mage:
    valid_foci = {"fire": "\x1b[38;2;227;59;59mfire\x1b[0m",
                  "water": "\x1b[38;2;157;198;252mwater\x1b[0m",
                  "earth": "\x1b[38;2;135;113;84mearth\x1b[0m",
                  "air": "\x1b[38;2;140;222;158mair\x1b[0m"}
    valid_input = False
    print("\033[2J\033[H", end="", flush=True)
    username = str.casefold(input("What is your name: "))
    print()
    while True:
        focus = str.casefold(input("What is your magical focus: "))
        if focus in valid_foci:
            return (Mage(username, valid_foci[focus]))
        if valid_input is False:
            print("\033[F\033[2K", end="", flush=True)
            valid_input = True
        else:
            print("\033[F\033[2K" * 2, end="", flush=True)
        print("That is not one of the valid basic magical foci:")
        print(f"- {valid_foci['fire']}")
        print(f"- {valid_foci['water']}")
        print(f"- {valid_foci['earth']}")
        print(f"- {valid_foci['air']}")
        

# def command(user: Mage) -> None:


if __name__ == "__main__":
    user = first_boot()
    print()
    intro(user)
    os.system('clear')


# print("This is \x1b[38;2;142;194;21mLIME GREEN\x1b[0m text")
# print("This is \x1b[48;2;194;21;139mROSA\x1b[0m background")
# \x1b[ starts the sequence
# 38;2; or 48;2; are foreground and background respectively
# x;y;z are the colors from 0 to 255
