from sanic import Sanic
from sanic.response import html
from sanic.blueprints import Blueprint
import json

class GlobalVars:
    def __init__(self):
        pass

app = Sanic(__name__)

gvars = GlobalVars()

@app.route('/post', methods=["POST"])
async def main(request):
    return json({ "received": True, "message": request.args["message"][0] })


app.run(host="0.0.0.0", port=8000)