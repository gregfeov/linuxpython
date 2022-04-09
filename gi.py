import eel
from random import randint
from syslib import *
eel.init("web")


# Exposing the random_python function to javascript
@eel.expose
def random_python():
    return h256(str(randint(1, 100)))


# Start the index.html file
eel.start("g.html",port=8082,host="192.168.1.64")