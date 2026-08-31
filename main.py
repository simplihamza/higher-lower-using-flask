from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 10)
print(number)
@app.route('/')
def welcome():
    return f'<h1>Guess a number between 0 and 9: </h1> <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Guess a Number">'


if __name__ == '__main__':
    app.run(debug=True)

# TODO-3: Create a new route that captures a number from the URL itself
#  (e.g. visiting "/3" or "/7"). Look into Flask's route "converters",
#  specifically how to tell Flask that a piece of the URL should be
#  captured as an integer and passed into your view function as a
#  parameter, rather than treated as a fixed literal path.

# TODO-4: Inside that new route's function, compare the captured number
#  against your randomly generated number from TODO-2. You'll need three
#  distinct outcomes: guess is too high, too low, or exactly correct,
#  using the same kind of three-way comparison structure you've used in
#  earlier exercises. For each outcome, return a different HTML string
#  with a distinct <h1> message, a distinct text color (inline CSS via
#  a 'style' attribute), and a different GIF for each outcome.

# TODO-5: Test all three scenarios manually by visiting different URLs
#  in your browser (e.g. yoursite/2, yoursite/5, yoursite/9), and confirm
#  each one shows the correct message, color, and GIF, and that guessing
#  correctly (matching the number printed in your console from TODO-2)
#  shows the "correct" outcome.