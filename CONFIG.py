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
COOKIE_KEY = '48436e9a-ca70-451d-8e28-010c7787de40'
PORT=5000
DICT="data/dict.txt"

