import alchemy.grimoire as grimoire


def spellcrafting(name: str, ingredients: str) -> str:
    from alchemy.grimoire.spellbook import record_spell as record
    return f"{record(name, ingredients)}"



if __name__ == "__main__":
    print()
    print("=== Circular Curse Breaking ===")
    print()
    print("Testing ingredient validation:")
    print("grimoire.validate_ingredients(\"fire air\"):",
          grimoire.validate_ingredients("fire air"))
    print("grimoire.validate_ingredients(\"dragon scales\"):",
          grimoire.validate_ingredients("dragon scales"))
    print()
    print("Testing spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"):",
          grimoire.record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\", \"shadow\"):",
          grimoire.record_spell("Dark Magic", "shadow"))
    print()
    print("Testing late import technique:")
    print("record_spell(\"Lightning\", \"air\"):",
          spellcrafting("Lightning", "air"))
    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
