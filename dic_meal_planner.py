from menu_content import pantry, recipes


def add_missing_ingredient(data: dict, product: str, amount: int) -> None:
    """
    add value to dictionary

    :param data: dictionary that function add products to
    :param product: (key) str name of product
    :param amount: (value) int number of product
    :return:
    """
    data[product] = amount


# menu_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
menu_dict = {}                                  # dict to display menu
for index, key in enumerate(recipes):
    menu_dict[str(index + 1)] = key
ingredients_to_buy = {}                         # dict to collect missing ingredients
while True:
    print("Please Choose From The Menu:\n"
          "----------------------------")
    for key, value in menu_dict.items():        # function to print menu_dict as menu
        print(f"{key}: {value}")
    choice = input(": ")                        # user select choice from menu
    if choice == "0":                           # 0 to EXIT program
        break
    elif choice in menu_dict:
        selected_item = menu_dict[choice]       # value of selected key stored in variable
        ingredients = recipes[selected_item]    # use value of key from menu_dict as the dict'
                                                # 'recipes' key to store value in variable
        print(f"Selected: {selected_item}\nRequires: {ingredients}\n")
        for ingredient, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(ingredient, 0)
            if required_quantity >= quantity_in_pantry:
                add_missing_ingredient(ingredients_to_buy, ingredient, required_quantity)
        print(f"Those ingredients are missing please buy:\n {ingredients_to_buy}")
        # pass # print(f"{ingredient} in stock")
        # else:
        #     quantity_to_order = required_quantity
        #     print(f"{ingredient} is not enough, please buy at last: 1{quantity_to_order}")
        # for ingredient in ingredients:
        #     if ingredient not in pantry:
        #         print(f"missing: {ingredient}")
        #     else:x
        #         print(f"{ingredient} available: {pantry[ingredient]}")

        # if ingredient in pantry:
        #     print(f"Pantry has {ingredient}")
        # else:
        #     print(f"Missing: {ingredient}")
