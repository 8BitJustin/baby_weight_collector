from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

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


def avg():
    average = db.session.query(func.avg(Data.guess_)).scalar()
    average = round(average, 1)
    print(average)
    return average


@app.route("/")
def index():
    avg()
    return render_template("index.html", average=avg())


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        name = request.form['name']
        guess = request.form['guess']
        print(name, guess)
        if db.session.query(Data).filter(Data.name_ == name).count() == 0:
            data = Data(name, guess)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        return render_template("index.html", text="Name already used, please "
                                                  "use another")


if __name__ == "__main__":
    app.run(debug=True)
