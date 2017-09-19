#! /usr/bin/python

# Scratch Hue Helper app
# ----------------------
# (c) 2015 Chris Proctor
# Distributed under the MIT license.
# Project homepage: http://mrproctor.net/scratch

import json
import requests
from flask import Flask
import logging
import os
import sys
from os import path
import pycraft_minetest as pcmt
import time

# It's not generally good practice to disable warnings, but this is one of 
# the first scripts students will run, so I am prioritizing a reduction of
# any unnecessary output
import warnings
warnings.filterwarnings("ignore")




app = Flask("Scratch_Pycraft")
app.logger.removeHandler(app.logger.handlers[0])

loggers = [app.logger, logging.getLogger('phue'), logging.getLogger('werkzeug')]
# No logging. Switch out handlers for logging.
# handler = logging.FileHandler('scratch_hue_extension.log')
handler = logging.NullHandler()
formatter = logging.Formatter('%(asctime)s - %(name)14s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
for logger in loggers:
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


jobs = set()

@app.route('/poll')
def poll():
    return "\n".join(["_busy {}".format(job) for job in jobs])


@app.route('/reset_all')
def reset_all():
    return "OK"


@app.route('/crossdomain.xml')
def cross_domain_check():
    return """
<cross-domain-policy>
    <allow-access-from domain="*" to-ports="3316"/>
</cross-domain-policy>
"""


# PYCRAFT FUNCTIONS:
@app.route('/sphere/<string:block>/<int:radius>/<int:x>/<int:y>/<int:z>')
def sphere(block, radius, x, y, z):
    print(block, radius, x, y, z)
    pcmt.sphere(pcmt.getblock(block), radius, x, y, z)
    return "OK"
    

@app.route('/cube/<string:block>/<int:side>/<int:x>/<int:y>/<int:z>')
def cube(block, side, x, y, z):
    print(block, side, x, y, z)
    pcmt.cube(pcmt.getblock(block), side, x, y, z)
    return "OK"
    




print(" * The Scratch helper app for controlling Hue lights is running. Have fun :)")
print(" * See mrproctor.net/scratch for help.")
print(" * Press Control + C to quit.")


done = False
while not done:
    try:
        app.run('0.0.0.0', port=3316)
    except:
        print("trying again")
        time.sleep(1)
    else:
        print("scratch_pycraft done")
        done = True
