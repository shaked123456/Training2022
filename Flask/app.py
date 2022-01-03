from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Test :P"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True, port="2222")
=======
    app.run(debug=True, "Intentional mistake)
>>>>>>> c8562df4d42ac3158fad8ac8ab4e3707bb5b5aef
