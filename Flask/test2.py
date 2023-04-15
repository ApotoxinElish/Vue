from flask import Flask, make_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def run():
    res = {
        "code": 0,
        "msg": "OK",
        "data": {
            "test": "测试页面",
        },
    }
    return make_response(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False, threaded=True)
