import requests
import json
import random


def get_random_comic():
    response = requests.get("https://xkcd.com/info.0.json")
    receive = response.content
    values = json.loads(receive.decode('utf-8'))
    r = random.randint(1,values["num"])
    new_url= "https://xkcd.com/" + str(r) + "/info.0.json"
    new_response = requests.get(new_url)
    new_receive = new_response.content
    new_value = json.loads(new_receive.decode('utf-8'))
    return new_value
    
    
get_random_comic()
