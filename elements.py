class Element:
    def __init__(self) -> None:
        self.elements = {}

    def add_element(self, name: str,
                    t_color: tuple[int, int, int]) -> bool:
        valid = self.validate_colors(t_color)
        if valid is True:
            r, g, b = t_color
            e_name = name
            e_color = f"\x1b[38;2;{r};{g};{b}m"
            self.elements.update({e_name: [e_name, e_color]})
        return valid

    def validate_colors(self, t_colors: tuple[int, int, int]) -> bool:
        try:
            for color in t_colors:
                if color < 0 or color > 255:
                    raise ValueError("Error: color value should be 0-255")
            return True
        except ValueError as e:
            print(e)
            return False

    def list_elements(self) -> None:
        for k, v in self.elements.items():
            print(f"- {v[1]}{v[0]}\x1b[0m")


def init_base_elements() -> dict[Element]:
    elements = {}
    all_elements = Element()
    basic_elements = Element()
    adv_elements = Element()
    player_elements = Element()
    first_elements = [["fire", (227, 59, 59)],
                      ["water", (157, 198, 252)],
                      ["earth", (135, 113, 84)],
                      ["air", (140, 222, 158)]]
    final_elements = [["light", (255, 255, 235)],
                      ["dark", (90, 70, 115)]]
    for e in first_elements:
        all_elements.add_element(e[0], e[1])
        basic_elements.add_element(e[0], e[1])
    for e in final_elements:
        all_elements.add_element(e[0], e[1])
        adv_elements.add_element(e[0], e[1])
    elements.update({"all_elements": all_elements,
                     "basic_elements": basic_elements,
                     "adv_elements": adv_elements,
                     "player_elements": player_elements})
    return elements


def create_fire() -> str:
    return "Fire element created"


def create_water() -> str:
    return "Water element created"


def create_earth() -> str:
    return "Earth element created"


def create_air() -> str:
    return "Air element creted"
