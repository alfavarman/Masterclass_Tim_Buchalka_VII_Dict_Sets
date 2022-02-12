available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

chart = []
current_choice = None
while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
        chart.append(available_parts[current_choice])
    elif current_choice == 'C'.casefold():
        if not chart:
            print("Your chart is empty!")
        else:
            print(f"In Your chart: {chart}")
    else:
        print("Please Select from: ")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("C: To See The Chart")
        print("0: EXIT")
    current_choice = input("> ")
