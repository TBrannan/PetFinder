import json
import requests
import env
import animal_colors


def get_token(values):
    data = {}
    data["grant_type"] = "client_credentials"
    data["client_id"]=env.client_id
    data["client_secret"]=env.client_secret
    url = f'https://api.petfinder.com/v2/oauth2/token'
    r = requests.post(url, data=json.dumps(data), verify=False)
    y = json.loads(r.content)
    token = y["access_token"]
    make_request(token,values)


def make_request(token,values):
    headers = {}
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    #Need to add try here to catch if no color is selected
    color = values['color']

    url = f'https://api.petfinder.com/v2/animals'
    r = requests.get(url,headers=headers, params=values)
    print(r.url)
    pet = json.loads(r.content)
    for count,i in enumerate(pet['animals']):
        if i['colors']['primary'] == color.title() or i['colors']['primary'] == color.lower():
            print(i['url'])
            print(i['colors'])


def pet_finder():
    pet = {}
    pet["type"] = input("What type of animal are you looking for?\n: ")

    q1 = input("Do you know what breed?\n: ")
    if q1.lower() == "y" or q1.lower() == "yes":
        pet["breed"] = input("What is the breed?\n: ")
    else:
        pet["breed"] = None

    q2 = input("Do you know what color?\n: ")
    if q2.lower() == 'y' or q2.lower() == 'yes':
        pet["color"] = colors(pet["type"])
    else:
        pet["color"] = None

    zipcode = "0"
    while len(zipcode) != 5:
        zipcode = input("Please enter 5 digit your zipcode\n: ")

    pet["location"] = zipcode
    pet["distance"] = 50

    create_url(pet)

def create_url(pet):
    values = {k: v for k, v in pet.items() if v is not None}
    get_token(values)


def colors(type):
    dog_colors = animal_colors.dog_colors
    color = '0'
    if type == 'dog':
        try:
            while int(color) not in range(1,16):
                for a,b in zip(dog_colors,dog_colors.values()):
                    print(f'{a}: {b}')
                color = input("\nPlease select the number associated with the color you would like\n :")
            else:
                colorboi = dog_colors[color]
                confirm = input(f"Is {colorboi} the color you want?\n :")
                if confirm.lower() == 'y' or confirm.lower() =='yes':
                    selected_color = dog_colors[color]
                    return selected_color
                else:
                    colors()
        except ValueError as e:
            print("Please select an integer")
            colors()
    elif type == 'cat':
        return cat_color()

def cat_color():
    cat_colors = animal_colors.cat_colors
    color = '0'
    try:
        while int(color) not in range(1,31):
            for a,b in zip(cat_colors,cat_colors.values()):
                print(f'{a}: {b}')
            color = input("\nPlease select the number associated with the color you would like\n :")
        else:
            colorboi = cat_colors[color]
            confirm = input(f"Is {colorboi} the color you want?\n :")
            if confirm.lower() == 'y' or confirm.lower() =='yes':
                selected_color = cat_colors[color]
                return selected_color
            else:
                cat_colors()
    except ValueError as e:
        print("Please select an integer")
        cat_color()


pet_finder()
