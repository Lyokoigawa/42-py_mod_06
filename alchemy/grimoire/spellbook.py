from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    valid_output = validate_ingredients(ingredients)
    if "INVALID" in valid_output:
        return f"Spell rejected: {spell_name}, ({valid_output})"
    elif "VALID" in valid_output:
        return f"Spell recorded: {spell_name} ({valid_output})"
