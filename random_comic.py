import requests
import json
import random
from flask import Flask, render_template , request

app = Flask(__name__)
# line 6 turns  this into a flask framework application 


VOTED = {}
@app.route("/vote/<int:id>/<string:vote>",methods=['GET'])
def cast_vote(id,vote):

    if (vote != "good" and vote!= "bad"):
        raise ValueError("Invalid input")
    if id in VOTED:
        if vote == "good":
            VOTED[id]["good"] +=1
        elif vote == "bad":
            VOTED[id]["bad"] +=1
    else:
        if vote == "good":
            VOTED[id]= {
                "good":1,
                "bad":0
            }
        elif vote == "bad":
            VOTED[id] = {
                "good":0,
                "bad":1
            }
        
    return VOTED[id]
    

@app.route("/")
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
    

# print(get_random_comic())



if __name__ == '__main__':
    app.run(debug=True)