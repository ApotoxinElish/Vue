from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def run():
    return make_response("OK")
