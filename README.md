# lbu-scrabble-club-testing

This repo contains implementations of classes for a Scrabble Club member, and for the Leaderboard.

There is a basic test class for `Member`, with one test. The mission is to increase the test 
coverage for each. It should be reasonably easy to get coverage for `Member` to 100%. Some magic 
would be needed to test the display methods in `Leaderboard`, but even without that, 70% or more is possible.

The classes are believed to be correct. Probably.

## Requirements

See `requirements.txt`, which should provide `coverage` and `pytest` (and its 
coverage plug-in). The simplest approach is to build a virtual environment from this.

## Running Tests

Running the tests from PyCharm should "just work". From the command line (this should work
without a virtual environment, as `unittest` is in the standard library):

    $ python3 -m unittest discover tests

Alternatively, with the virtual environment:

    $ python3 -m pytest tests

would do much the smae thing.

## Seeing Coverage

These need the virtual environment. Or if you do this in a Codespace you may well find that
`pytest` is in the default system install.

With `pytest`:

    $ python3 -m pytest --cov=scrabble_club --cov-report=term-missing tests/

With `coverage`:

    $ coverage run -m scrabble_club.member
    $ coverage report -m 

Note that the numbers used to work out the percentages refer to lines of code. 
So the current test (if you trace
it through) does give a promising start. The commands above will point out which
lines are untested.

