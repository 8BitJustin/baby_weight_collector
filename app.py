from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
# Config login for local database
# *** Use for TESTING ***
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:********' \
                                        '@localhost/birth_weight'

# *** Use for PRODUCTION ***
# 9/11/2020 Update - Removed from Heroku (including DB). To use again,
# a new DB will need to be created, which will generate a new URI.
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     'postgres://ifoemhpwhwdfeq:ddf3a55c5523c6e32cbd1f7c9255573a043317cf321a' \
#     'd18d2221ca2e4f5ef487@ec2-34-206-31-217.compute-1.amazonaws.com:5432/d4' \
#     '9ubohr81ma7k'

db = SQLAlchemy(app)


class Data(db.Model):
    """
    Data model which creates table within database
    """
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(20), unique=True)
    guess_ = db.Column(db.Float)

    def __init__(self, name_, guess_):
        self.name_ = name_
        self.guess_ = guess_


def avg():
    """
    Accesses database using query, finds the average between current guesses
    :return: The average of guesses
    """
    average = db.session.query(func.avg(Data.guess_)).scalar()
    average = round(average, 1)
    return average


def count():
    """
    Accesses the number of total 'id' within database
    :return: Total amount of guesses
    """
    user_count = db.session.query(func.count(Data.id)).scalar()
    return user_count


# def toast():
#     """
#     Provides windows notification
#     :return: Toaster popup notification
#     """
#     toaster = ToastNotifier()
#     toasted = toaster.show_toast("Guess Kaden's Weight",
#                                  "Another guess has been made!",
#                                  icon_path=None,
#                                  duration=5,
#                                  threaded=True)
#     return toasted


@app.route("/")
def index():
    """
    Index page. Utilizes both count and avg functions
    :return: The index.html file, and both the average and count to display
    within the index.html file
    """
    user_count = db.session.query(func.count(Data.id)).scalar()
    if user_count == 0:
        return render_template("index.html", average=0, count=0)
    else:
        count()
        avg()
        return render_template("index.html", average=avg(), count=count())


@app.route("/success", methods=['POST'])
def success():
    """
    Success page. If method is POST (which it will be when utilized),
    name and guess variables are created. If they do not match what is in
    the database, they are added to the database.
    :return: Either the success.html (if name/guess aren't already in the
    db, or the index.html will refresh with an error message
    """

    if request.method == 'POST':
        name = request.form['name']
        guess = request.form['guess']
        user_count = db.session.query(func.count(Data.id)).scalar()

        if db.session.query(Data).filter(Data.name_ == name).count() == 1:
            return render_template("index.html",
                                   text="Name already used, please "
                                        "use another", average=avg(),
                                   count=count())
        elif db.session.query(Data).filter(Data.guess_ == guess).count() == 1:
            return render_template("index.html",
                                   text="Guess already used, please "
                                        "use another", average=avg(),
                                   count=count())
        else:
            if user_count == 0:
                data = Data(name, guess)
                db.session.add(data)
                db.session.commit()
                return render_template("success.html")
            else:
                count()
                avg()
                data = Data(name, guess)
                db.session.add(data)
                db.session.commit()
                # toast()
                return render_template("success.html")


@app.route("/guesses", methods=['GET'])
def guesses():
    rows = db.session.query(Data)
    if rows.count() == 0:
        return render_template('guesses.html')
    else:
        return render_template('guesses.html', rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
