class Spell:
    def __init__(self, name: str,
                 creator: str,
                 components: list[str]) -> None:
        self.name = str.title(name)
        self.creator = creator.capitalize()
        self.components = components
        self.cost = len(components)

    def cast(self, target: str) -> None:
        print(f"\nUsed {self.cost} mana to cast {self.name} on {target}!")
