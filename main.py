import json
import requests
import env
import query

#Probably need to create a Class and add token to __init__
def get_token(api_url,values='False'):
    data = {}
    data["grant_type"] = "client_credentials"
    data["client_id"]=env.client_id
    data["client_secret"]=env.client_secret
    url = f'https://api.petfinder.com/v2/oauth2/token'
    r = requests.post(url, data=json.dumps(data), verify=False)
    y = json.loads(r.content)
    token = y["access_token"]
    if values != 'False':
        make_request(token,values)
    else:
        dog_breed = custom_request(token,api_url)
        return dog_breed

def custom_request(token,url):
    headers = {}
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    r = requests.get(url,headers=headers)
    # print(r.url)
    pet = json.loads(r.content)
    return pet


def make_request(token,values):
    headers = {}
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    try:
        color = values['color']
        colors = True
    except KeyError as e:
        colors = False
        pass

    url = f'https://api.petfinder.com/v2/animals'
    r = requests.get(url,headers=headers, params=values)
    # print(r.url)
    pet = json.loads(r.content)
    if colors is False:
        for count,i in enumerate(pet['animals']):
            if i == None:
                print("No Matches")
            else:
                print(i['url'])
    else:
        for count,i in enumerate(pet['animals']):
            if i == None:
                print("No Matches")
            elif i['colors']['primary'] == color.title() or i['colors']['primary'] == color.lower():
                print(i['colors'])
                print(i['url'])


def create_url(pet):
    values = {k: v for k, v in pet.items() if v is not None}
    get_token('',values)



if __name__ == '__main__':
    query.pet_finder()
