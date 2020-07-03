# Baby Weight Collector

Simple webapp that takes a receives a user's input regarding their guess for what my son's weight will be upon his birth.

### How does it work?

It's rather simple, well, the concept at least. User accesses the link to the [site](https://koweightcollector.herokuapp.com/), and they will be presented with some text, total guesses integer, average of guesses integer, two input boxes, a submit button and current guesses button.

The user inputs their first/last name, and what they belive the baby's weight to be. Once they click submit, this information is sent to the database created with SQLAlchemy and stored. They are then presented with a Thank You screen, which goes back to the initial screen after a few seconds.

### Details

A step by step series of steps to detail how the app works.

The user inputs their name and weight guess

```
The weight input is limited to a minimum of 4, and max of 11. This is to ensure nobody inputs an obsene number to throw off the average. It's set up with a 0.1 step, so it only accepts numbers like, 4.5, 7.0, 10.1, etc.
```

The user then submits via the submit button

```
The data provided (name and weight) are then sent to the database table, and the user is sent to the completion page, which automatically goes back to the initial screen after four seconds.
```

Duplicate names and weights are not allowed

```
Conditional statements have been implemented to check that both the user name provided and their weight are not already in the db. If either are, a warning will show advising the name/weight has been used, and another needs to be picked.
```

On the main screen are two values that change with each submission, total guesses and the average weight of the current guesses

```
I wanted to put some fun information up front for the user, so I coded the total guesses value (which is pulled from the database that reflects the total of submissions in the database), and the average of those guesses (using sqlalchemy's func method).
```

And finally, the Current Guesses button

```
Clicking this will bring the user to another page that shows a small table, displaying the user's that have guessed, and what their guess was.
```

## Actual Process

Story time!

So, I'm always looking for project ideas that I can utilize Python with, but none ever seem to be captivating enough to keep me interested. When I found out the wife and I were expecting months ago, I knew I wanted to do something, but just didn't know what.

Fast forward to two weeks ago. I recalled one of the lessons on the Udemy Python Mega Course where a web app database was created to store a user's height, and email them about it. I decided to use some of the instruction here and build a web app that family and friends could have fun with.

The Baby Weight Collector idea was born.

In the beginning, it was to be a simple bit of text asking for a name and guess, and there would be a table underneath to show current guesses.

After some designing, I went with a one page approach that kept everything front and center. I started with just the HTML and CSS first to get the look out of the way.

Once the pages were done, I went into Python to make sure the main page would load to the success page upon submission. After the mechanics were in place, it was time to work on the database.

Using SQLAlchemy, a table was able to be built and after some coding, user submissions were able to be stored within the database.

For the most part, if I wanted something simple, this would have been completed. However I wanted to show information on the main page (total and average). These weren't specifically reviewed in the lecture, so I was happy to research and get this to work myself.

Through many print statements, I was able to pull the total and average, but the tough part was getting this to show on the HTML page. It felt like an eternity, but the simplist resolution can sometimes be right there and you not even know it (I actually had a moment in front of my computer where I was mad, stormed away, told the wife I was taking a shower, got to the bathroom, looked in the mirror, went back to my computer, wrote one line of code in maybe 3 seconds, and it worked. Crazy.).

Here, I figured I was finished. The page looked good. Inputs worked as instructed, the count and average values displayed correctly, everything was good. But...something still felt like it was missing.

Yeah, the table.

At this point, I didn't want to shove it on the main page, it needed it's own. So, I made another page to display the guesses. I added a button the the main page at first, and tested clicking would take the user to the blank guesses page. Once that worked, I added a Back button to the guesses page that...well...took the user back to the main page. As weird as it was, getting this button to work was confusing.

Once those worked, it was time to try to get the table to work. Well, at least get the data from the db to show on the page, I'd work on the table after.

This took a couple of hours, but it turned out to be another simple bit of code. Ended up using a Python for x in x to create the td and tr's. Once that brought in the data, I was able to do some basic styling with the CSS.

Then I uploaded to Heroku.

The last thing I did, was out of convenience. The Heroku site stores data, but it's a pain in the A to access/view. I want to be able to view the table in the db, so I ended up linking the Heroku db to PGAdmin4, so now I can view the table, and remove any accidental guesses and such. :)

The end!

## Deployment

Deployed through Heroku

## Built With

- [Python](https://www.python.org/) - Programming language
- [HTML](https://html.com/) - Basic structuring language
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS) - Basic styling language
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Python Web Application Framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python library, used to help Python and databases communicate

## Authors

- **Justin Olson** - Creator/Designer/Coder - [Portfolio Site](https://jolsondigital.netlify.app/)

## Acknowledgments

- Inspired by my son Kaden
- Parts modeled by the Udemy Python Mega Course
