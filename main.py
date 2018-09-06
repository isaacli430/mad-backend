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
    data = request.json
    return json({ "received": True, "message": request.json })


app.run(host="0.0.0.0", port=8000)