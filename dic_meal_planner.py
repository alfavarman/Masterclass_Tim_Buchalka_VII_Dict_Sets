from menu_content import pantry, recipes

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    print("Please Choose From The Menu:\n"
          "----------------------------")
    for key, value in display_dict.items():
        print(f"{key}: {value}")
    choice = input(": ")
    ingredients_to_buy = {}
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        ingredients = recipes[selected_item]
        print(f"Selected: {selected_item}\nRequires: {ingredients}\n")
        for ingredient, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(ingredient, 0)
            if required_quantity >= quantity_in_pantry:
                ingredients_to_buy[str(ingredient)] = required_quantity
        print(f"Those ingredients are missing please buy: {ingredients_to_buy}")
                #pass # print(f"{ingredient} in stock")
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