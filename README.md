# Higher Lower

A Flask app for a number-guessing game. On startup it picks a random number
between 0 and 9 and shows a home page prompting the player to guess it.

## Features

- Flask app with a single route (`/`) that returns an HTML page with a
  heading asking the player to guess a number between 0 and 9, and a GIF.
- A random target number (0-9) is generated once when the app starts and
  printed to the console for debugging.

## How to Run

1. Install dependencies:
   ```
   pip install flask
   ```
2. Run the app:
   ```
   python main.py
   ```
3. Visit `http://127.0.0.1:5000/` in your browser.

## Practice File

`playground.py` is a scratch file used to practice concepts before building
`main.py`: a basic Flask route, and Python decorators (a delay decorator, an
HTML-emphasis decorator that wraps a return value in `<em>` tags, a timing
decorator comparing execution speed, and a logging decorator that prints a
function's arguments and return value). Most of it is commented out; the
active example is the logging decorator applied to a simple summing function.

## Known Issues / Limitations

- There is no way to actually submit a guess yet. The route that would
  capture a guessed number from the URL and compare it against the target
  (with distinct too-high / too-low / correct responses) is not implemented.

## What I Learned

- How to serve HTML (including an embedded image) from a Flask view
  function using an f-string.
- How to generate a random number once at module load time so it stays
  fixed for the lifetime of the running server, rather than regenerating
  on every request.
- Python decorators: how `func(*args)` and a `wrapper` function let you
  add behavior (logging, timing, wrapping output in HTML tags) around an
  existing function without changing its code, practiced in `playground.py`
  before applying similar ideas here.
