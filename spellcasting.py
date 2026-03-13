import alchemy.grimoire as grimoire
import alchemy.elements as elements
import alchemy.potions as potions


# print("\033[2J\033[H\033[?25l", end="", flush=True) (clears the command prompt and hides the cursor)
# print("\033[2J\033[H", end="", flush=True) (clears the command prompt)
# print("\033[F\033[2K" * n, end="", flush=True) (clears n amount of lines starting from the current one)


class Spellbook:
    def __init__(self, owner: str, type: str) -> None:
        self.owner = owner

    def book_type(self, type: str) -> None:
        if type == "fire":
            self.type == "Grimoire"
        elif type == "water":
            self.type == "Tome"
        elif type == "earth":
            self.type == "Spellbook"
        elif type == "air":
            self.type == "Codex"


class Mage:
    def __init__(self, name: str, focus: str):
        self.name = str.casefold(name)
        self.focus = str.casefold(focus)
        self.spellbook = Spellbook(self.name, self.focus)

    def you(self) -> str:
        return str.capitalize(self.name)


def first_boot() -> Mage:
    valid_foci = ["fire", "water", "earth", "air"]
    valid_input = False
    print("\033[2J\033[H", end="", flush=True)
    print()
    username = str.casefold(input("What is your name: "))
    print()
    while True:
        focus = str.casefold(input("What is your magical focus: "))
        for i in valid_foci:
            if focus == i:
                return (Mage(username, focus))
        if valid_input is False:
            print("\033[F\033[2K", end="", flush=True)
            valid_input = True
        else:
            print("\033[F\033[2K" * 2, end="", flush=True)
        print("That is not one of the valid magical foci (fire, water, earth, air)")


if __name__ == "__main__":
    user = first_boot()
    print()
    print(f"Welcome, mage {user.you()}!")
    
