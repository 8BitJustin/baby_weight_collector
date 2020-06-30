from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        guesser = request.form['name']
        guess = request.form['guess']
        print(guesser, guess)
        return render_template("success.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
