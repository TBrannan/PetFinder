
def type():
    import main
    dict = {}
    pet = main.get_token(f'https://api.petfinder.com/v2/types')
    for count,i in enumerate(pet['types']):
        d = {str(count): i['name']}
        dict.update(d)
    return dict

def breeds(type):
    import main
    dict = {}
    pet = main.get_token(f'https://api.petfinder.com/v2/types/{type}/breeds')
    for count,i in enumerate(pet['breeds']):
        d = {str(count): i["name"]}
        dict.update(d)
    return dict

def option(type,option):
    import main
    dict = {}
    pet = main.get_token(f'https://api.petfinder.com/v2/types/{type}')
    for count,i in enumerate(pet['type'][f'{option}']):
        d = {str(count): i}
        dict.update(d)
    return dict
