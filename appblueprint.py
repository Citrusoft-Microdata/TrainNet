#!/usr/bin/env python3
from flask import Flask
#app = Flask(Train Automation Portal)
import time

import automationhat

class bcolors:
    WARNING = '\033[91m'
    OKCYAN = '\033[92m'
location = ("null")

if automationhat.is_automation_hat():
    automationhat.light.power.write(1)
countdown = int(240)
delay = float(0.75)

#@app.route("/")
def index():
    return "<h1>Hi</h1>"

def changeRoute():
    automationhat.output.one.toggle()

#@app.route("/south")
def southSide():
    print(bcolors.OKCYAN + "Tram at South end.")
    automationhat.relay.three.off()
    time.sleep(delay)
    automationhat.relay.one.on()
    automationhat.relay.two.on()
    location = ("south")
    running = ("true")
#@app.route("/north")
def northSide():
    print(bcolors.OKCYAN + "Tram at North end.")
    automationhat.relay.one.off()
    automationhat.relay.two.off()
    time.sleep(delay)
    automationhat.relay.three.on()
    location = ("north")
    running = ("true")

def quitInputFail():
    print(bcolors.WARNING + "ERROR: input failure")
    automationhat.relay.one.off()
    automationhat.relay.two.off()
    automationhat.relay.three.off()
#    uinput = input("Restart? (Y/N)")
#    if uinput == ("n"):
    running = ("false")
#    else:
#        print("Restarting...")
ncountdown = int(1)





def appstart():
#    return("<h1>System has started...</h1>")
    while True:
#    running = ("true")
        if(automationhat.input.one.read() == False):
            if( automationhat.input.two.read() == False):
                quitInputFail()
                break
        if(automationhat.input.one.read() == False):
            northSide()
            location = ("south")
            ncountdown = (countdown)
        if(automationhat.input.two.read() == False):
            southSide()
            ncountdown = countdown
            location = ("north")
        time.sleep(0.0625)
#        ncountdown = (ncountdown - 1)
#        if (ncountdown == 0):
#            quitInputFail()
#            break
#        return("<h1>System has started</h1>")
