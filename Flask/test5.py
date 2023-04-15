from flask import Flask, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r"/*")


@app.route("/", methods=["GET", "POST"])
def run():
    host = request.headers.get("Host")
    print(host)

    return make_response("ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False, threaded=True)
