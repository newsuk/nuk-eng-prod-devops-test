from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/", methods=['GET'])
def index():
    """
    The default route
    """
    if request.method == 'GET':
        return "Welcome to the server app"

@app.route("/version", methods=['GET'])
def version():
    """
    Spits out the current version of the application
    """
    if request.method == 'GET':
        return "0.21.3"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
