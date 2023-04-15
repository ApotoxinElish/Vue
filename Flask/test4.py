from flask import Flask, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r"/*")


@app.route("/", methods=["GET", "POST"])
def run():
    getJson = request.get_json()
    username = str(getJson.get("username"))
    password = int(getJson.get("password"))

    if username == "admin" and password == 123:
        res = {
            "code": 0,
            "msg": "OK",
            "data": {
                "test": "测试页面",
            },
        }
    else:
        res = {
            "code": 999,
        }
    return make_response(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False, threaded=True)
