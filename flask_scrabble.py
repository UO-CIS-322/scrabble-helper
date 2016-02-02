"""
Simple Flask web site 
"""

import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging
import sys

# Our own modules
from letterbag import LetterBag
import find

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG

#### 
# Word list is global data, read once at
# beginning of execution
####

wordsfile = open(CONFIG.DICT)  
WORDS = [ line.strip() for line in wordsfile ]

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
  return flask.render_template('scrabble.html')

###############
# AJAX request handlers 
#   These return JSON, rather than rendering pages. 
###############
@app.route("/_check")
def _check():
  tray = request.args.get("tray", "", type=str)
  pattern = request.args.get("pattern", "XXX", type=str)
  matches = find.search(WORDS, pattern, tray)
  ### Matches returns a list of words
  return jsonify(result={ "words": " ".join(matches) })

#############

app.secret_key = CONFIG.COOKIE_KEY

# Set up to run from cgi-bin script, from
# gunicorn, or stand-alone.
#
if __name__ == "__main__":
    # Standalone, with a dynamically generated
    # secret key, accessible outside only if debugging is not on
    import uuid
    app.debug=CONFIG.DEBUG
    app.logger.setLevel(logging.DEBUG)
    if app.debug: 
        print("Accessible only on localhost")
        app.run(port=CONFIG.PORT)  # Accessible only on localhost
    else:
        print("Opening for global access on port {}".format(CONFIG.PORT))
        app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    # Running from cgi-bin or from gunicorn WSGI server, 
    # which makes the call to app.run.  Gunicorn may invoke more than
    # one instance for concurrent service. 
    app.debug=False

