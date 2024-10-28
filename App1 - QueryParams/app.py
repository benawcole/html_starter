import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

from example_routes import apply_example_routes
apply_example_routes(app)

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.

# from example_routes import apply_example_routes
# apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

# == actual code ==

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name']
    return f"Hello {name}!\n"

@app.route('/submit', methods=['POST'])
def introduction():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"\n'

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f"I am waving at {name}\n"

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    number_of_vowels = len([x for x in text if x.lower() in 'aeiou'])
    return f"There are {number_of_vowels} vowels in \"{text}\""

@app.route('/sort_names', methods=['POST'])
def sort_names():
    text = request.form['text']
    sorted(text.split(','))
    print(",".join(sorted(text.split(','))))
    return ",".join(sorted(text.split(',')))

@app.route('/names', methods=['GET'])
def add():
    names = request.form['names']
    old_names = 'Alice,Bob,Charlie'
    return names