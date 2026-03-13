def validate_ingredients(ingredients: str) -> str:
    input_mats = ingredients.split(" ")
    valid_counter = 0
    valid_mats = ["fire", "water", "earth", "air"]
    for v_mat in valid_mats:
        for i_mat in input_mats:
            if i_mat == v_mat:
                valid_counter += 1
    if valid_counter == len(input_mats):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
