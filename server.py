import re
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "are no fun"

@app.route('/')
def index():
    return render_template('index.html')

# submit form
@app.route('/process', methods=["POST"])
def submit_form():
    # checks to make sure route is working
    print(request.form)
    # assign variables to session
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

# display data after submit
@app.route('/result')
def display_data():
    # passes session variables from the form to /result to be displayed
    return render_template('result.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])


if __name__ == "__main__":
    app.run(debug=True)