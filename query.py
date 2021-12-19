import animal

#User inputs
def pet_finder():
    pet = {}

    #What animal
    animal_choice = animal.type()
    print(animal_choice)
    pet["type"] = question(animal_choice,"animal")

    #What breed
    breed_q = input("Would you like to search for a specific breed?\n: ")
    if breed_q.lower() == 'y' or breed_q.lower() =='yes':
        breeds = animal.breeds(pet["type"])
        pet["breed"] = question(breeds,"breed")
    else:
        pet["breed"] = None

    #What color
    color_q = input("Would you like to search for a specific color?\n: ")
    if color_q.lower() == 'y' or color_q.lower() =='yes':
        color = animal.option(pet["type"],"colors")
        pet["color"] = question(color,"color")
    else:
        pet["color"] = None

    #What gender
    color_q = input("Would you like to search for a specific gender?\n: ")
    if color_q.lower() == 'y' or color_q.lower() =='yes':
        gender = animal.option(pet["type"],"genders")
        pet["gender"] = question(gender,"gender")
    else:
        pet["gender"] = None

    #Get zipcode
    zipcode = "0"
    while len(zipcode) != 5:
        zipcode = input("Please enter 5 digit your zipcode\n: ")
        pet["location"] = zipcode
        pet["distance"] = 50

    #confirm correct choices
    for correct_values in pet.items():
        print(f'{correct_values[0]}: {correct_values[1]}')
    final = input("Are these choices correct?\n: ")
    if final.lower() == 'y' or final.lower() =='yes':
        import main
        main.create_url(pet)
    else:
        pet_finder()

#Turn choices into dictionary
def question(dict, query):
    try:
        for a,b in zip(dict,dict.values()):
            print(f'{a}: {b}')
        user_input = input(f"What type of {query} are you looking for?\n: ")
        return dict[user_input]
    except KeyError:
        print("Please enter a valid number")
        question(dict,query)
