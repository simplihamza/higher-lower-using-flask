from flask import Flask

app = Flask(__name__)
@app.route('/')
def welcome():
    return f'<h1>Guess a number between 0 and 9: </h1>'

if __name__ == '__main__':
    app.run(debug=True)




# TODO-1: Import 'random' at the top of the file, and generate a random
#  number between 0 and 9 (inclusive) once, when the app starts, store it
#  in a variable at the top level of the file (not inside a function),
#  so it stays the same across every request until you restart the server.

# TODO-2: Add a print statement showing the random number right after
#  generating it, purely for your own testing/debugging, so you know
#  the "answer" while testing your routes without needing to guess blindly.

# TODO-3: Update your home route's returned HTML to include a GIF, using
#  an <img> tag with a 'src' pointing to a Giphy URL of your choice.
#  Think about how you'd combine two separate HTML strings (the <h1> and
#  the <img>) into one return statement, Python lets you concatenate
#  adjacent string literals just by placing them next to each other
#  across multiple lines.

# TODO-4: Create a new route that captures a number from the URL itself
#  (e.g. visiting "/3" or "/7"). Look into Flask's route "converters",
#  specifically how to tell Flask that a piece of the URL should be
#  captured as an integer and passed into your view function as a
#  parameter, rather than treated as a fixed literal path.

# TODO-5: Inside that new route's function, compare the captured number
#  against your randomly generated number from TODO-1. You'll need three
#  distinct outcomes: guess is too high, too low, or exactly correct,
#  think about the comparison operators and control flow structure
#  you've used many times before for this kind of three-way branching
#  (your leap year and prime-checking exercises used similar structures).

# TODO-6: For each of the three outcomes, return a different HTML string
#  containing an <h1> with a distinct message, a distinct text color
#  (using inline CSS, e.g. a 'style' attribute on the <h1> tag), and a
#  different GIF for each outcome (too high, too low, correct). You can
#  use the GIF URLs already given, or find your own three GIFs on Giphy.

# TODO-7: Test all three scenarios manually by visiting different URLs
#  in your browser (e.g. yoursite/2, yoursite/5, yoursite/9), and confirm
#  each one shows the correct message, color, and GIF, and that guessing
#  correctly (matching the number printed in your console from TODO-2)
#  shows the "correct" outcome.