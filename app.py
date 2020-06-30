from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:C0d!ng01' \
                                      '@localhost/birth_weight'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    name_ = db.Column(db.String(20), unique = True)
    guess_ = db.Column(db.Float)

    def __init__(self, name_, guess_):
        self.name_ = name_
        self.guess_ = guess_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        name = request.form['name']
        guess = request.form['guess']
        print(name, guess)
        data = Data(name, guess)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
