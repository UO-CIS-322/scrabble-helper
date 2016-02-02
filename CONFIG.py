"""
Configuration of flask application.
Everything that could be different between running
on your development platform or on ix.cs.uoregon.edu
(or on a different deployment target) shoudl be here.
"""
DEBUG = True
# Cookie key was obtained by:
#   import uuid
#   str(uuid.uuid4())
# We do it just once so that multiple processes
# will share the same key. 
COOKIE_KEY = '0166c5c7-c4fc-4b20-9bcb-219733271fde'
PORT=5000
DICT="data/dict.txt"

