from sanic import Sanic, response
from sanic.blueprints import Blueprint
import json

class GlobalVars:
    def __init__(self):
        pass

app = Sanic(__name__)

gvars = GlobalVars()

@app.route('/post', methods=["POST"])
async def main(request):
    return response.json({ "received": True, "args": request.raw_args})


app.run(host="0.0.0.0", port=8000)