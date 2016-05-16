"""
Simple Flask web site 
"""

# import flask
# from flask import render_template
# from flask import request
# from flask import url_for
# from flask import jsonify # For AJAX transactions

import json
import logging
import sys

# Our own modules
from letterbag import LetterBag
import find

###
# Globals
###
# app = flask.Flask(__name__)
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

# @app.route("/")
# @app.route("/index")
# def index():
#   return flask.render_template('scrabble.html')

# ###############
# # AJAX request handlers 
# #   These return JSON, rather than rendering pages. 
# ###############
# @app.route("/_check")
# def _check():
#   tray = request.args.get("tray", "", type=str)
#   pattern = request.args.get("pattern", "XXX", type=str)
#   matches = find.search(WORDS, pattern, tray)
#   ### Matches returns a list of words
#   return jsonify(result={ "words": " ".join(matches) })

#############

# We want to profile just the 'find' functionality on a
# number of test cases.  I'll generate seven trays and
# patterns from an actual scrabble bag, excluding blanks.
# I get 14 by reading columns as well as rows. 
#
trays = ["yetosuk", "ieenaar", "pnosoii", "zrjrbut",
         "dlhdoai", "mawytac", "cerauis", "myipzdc",
         "aeenrle", "wteojhr", "yonsrda", "tsaobou",
         "auaiuai", "ckritis" ]

# I have a couple pictures of scrabble boards from actual
# games, from which I'll make some patterns
#
boardwords = [ "wham", "air", "vipers", "tie", "pica", "eel",
               "sensors", "equal", "pram", "spade", "ide",
               "of", "flit", "tin", "keg", "yo", "radio",
               "bough", "jilt", "sub", "toucan", "candor",
               "fie", "zee", "go", "vixen", "giant", "town",
               "be", "ere", "ye", "town" ]

# Now for each word on the board, we look for ways to prefix it,
# ways to suffix it, and ways to cross it, with each hand.  That should
# take a while!
#
# Takes *too* long.  I'll limit number of trays and words to speed it
# up to about 15 seconds, which should be sufficient for profiling

TRAYLIMIT = 5
WORDLIMIT = 10

for tray in trays[:TRAYLIMIT]:
  print("\nTray: {}".format(tray))
  for word in boardwords[:WORDLIMIT]:
    prefixed = find.search(WORDS, "_"+word, tray)
    if len(prefixed) > 0:
      print("_{} => {}".format(word, prefixed))
    suffixed = find.search(WORDS, word+"_", tray)
    if len(suffixed) > 0:
      print("{}_ => {}".format(word, suffixed))


