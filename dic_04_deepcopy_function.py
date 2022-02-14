from menu_content import recipes, pantry


def deepcopy_1lvl(obct: dict or list) -> dict or list:
    """
    deep copy of objects in first level.

    :param obct: dict or list to copy
    :return: copied list or dict
    """

    if type(obct) is dict:
        obct_copy = {}
        for key, value in obct.items():
            new_value = value.copy()
            obct_copy[key] = new_value
        return obct_copy
    elif type(obct) is list:
        obct_copy = []
        for value in obct:
            new_value = value.copy()
            obct_copy.append(new_value)
        return obct_copy
    else:
        ValueError(f'{obct} is not list either dict type')


recipes_copy = deepcopy_1lvl(recipes)
print(type(recipes))
print(id(recipes), recipes)
print(id(recipes_copy), recipes_copy)
recipes_copy['Butter chicken']['ginger'] = 300
print(recipes["Butter chicken"]["ginger"])
print(recipes_copy["Butter chicken"]["ginger"])

print()
pantry_copy = deepcopy_1lvl(pantry)
print(type(pantry))
print(id(pantry), pantry)
print(id(pantry_copy), pantry_copy)
# pantry_copy["Butter chicken"]["ginger"] = 300
# print(pantry["Butter chicken"]["ginger"])
# print(pantry_copy["Butter chicken"]["ginger"])
