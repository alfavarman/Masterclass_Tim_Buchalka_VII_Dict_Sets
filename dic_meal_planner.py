from menu_content import pantry, recipes

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    print("Please Choose From The Menu:"
          "----------------------------")