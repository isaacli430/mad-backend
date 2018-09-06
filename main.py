from sanic import Sanic, response
from sanic.blueprints import Blueprint
from datetime import datetime
import json

# initialize the app
app = Sanic(__name__)

# global variable class
class GlobalVars:
    def __init__(self):
        self.e400 = response.json({"status": "ERROR", "code": 400, "message": "BAD REQUEST"})

gvars = GlobalVars()

@app.route('/post', methods=["POST"])
async def main(request):
    curr_time = datetime.utcnow()
    data = request.raw_args

    # checks to see if there are student, time and class parameters
    for check in ["student", "class"]:     
        if check not in data.keys():
            return gvars.e400

    with open("stuff.json") as f:

        l_data = json.load(f)

        # checks to see if the class exists
        if data["class"] not in l_data.keys():
            return gvars.e400
        curr_class = l_data[data["class"]]

        # creates a datetime object for the class start time
        start_time = datetime.time(curr_class["start_time"]["hour"], curr_class["start_time"]["minute"], 0)


    return response.json({"status": "OK", "code": 200, "args": request.raw_args})


app.run(host="0.0.0.0", port=8000)