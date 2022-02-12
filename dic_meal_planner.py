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

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"Selected: {selected_item}")
        ingredients = recipes[selected_item]
        print(ingredients)
        for ingredient in ingredients:
            if ingredient not in pantry:
                print(f"missing: {ingredient}")
            else:
                print(f"{ingredient} available: {pantry[ingredient]}")

            # if ingredient in pantry:
            #     print(f"Pantry has {ingredient}")
            # else:
            #     print(f"Missing: {ingredient}")