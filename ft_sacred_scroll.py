import alchemy


def primordial_knowledge(element: int) -> None:
    if element == 0:
        print("alchemy.elements.create_fire(): ", end="")
        print(alchemy.elements.create_fire())
    elif element == 1:
        print("alchemy.elements.create_water(): ", end="")
        print(alchemy.elements.create_water())
    elif element == 2:
        print("alchemy.elements.create_earth(): ", end="")
        print(alchemy.elements.create_earth())
    elif element == 3:
        print("alchemy.elements.create_air(): ", end="")
        print(alchemy.elements.create_fire())
    else:
        print("Trying to access unknown sacred knowledge. "
              "Turn back, lest you know what you're doing...")
    

def read_scroll(element: int) -> None:
    try:
        if element == 0:
            print("alchemy.create_fire(): ", end="")
            print(alchemy.create_fire())
        elif element == 1:
            print("alchemy.create_water(): ", end="")
            print(alchemy.create_water())
        elif element == 2:
            print("alchemy.create_earth(): ", end="")
            print(alchemy.create_earth())
        elif element == 3:
            print("alchemy.create_air(): ", end="")
            print(alchemy.create_air())
        else:
            print("Trying to access unknown sacred knowledge. "
                  "Turn back, lest you know what you're doing...")
    except AttributeError:
        print("AttributeError - not exposed")


if __name__ == "__main__":
    print()
    print("=== Sacred Scroll Mastery ===")
    print()
    print("Testing direct module access:")
    for i in range(4):
        primordial_knowledge(i)
    print()
    print("Testing package-level access (controlled by __init.py):")
    for i in range(4):
        read_scroll(i)
    print()
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
