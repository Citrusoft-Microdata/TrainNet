#!/usr/bin/env python3
import appblueprint
from flask import Flask, jsonify, render_template, request
app = Flask("Train Automation Portal")
import time
running = False
import automationhat

class bcolors:
    WARNING = '\033[91m'
    OKCYAN = '\033[92m'

location = ("null")

if automationhat.is_automation_hat():
    automationhat.light.power.write(1)
countdown = int(240)
delay = float(0.75)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/south")
def southSide():
    print(bcolors.OKCYAN + "Tram at South end.")
    automationhat.relay.three.off()
    time.sleep(delay)
    automationhat.relay.one.on()
    automationhat.relay.two.on()
    location = ("north")
    return "<h1>Train Moving Towards the North End</h1>"

@app.route("/changeroute")
def changeroute():
    appblueprint.changeRoute()

@app.route("/north")
def northSide():
    print(bcolors.OKCYAN + "Tram at North end.")
    automationhat.relay.one.off()
    automationhat.relay.two.off()
    time.sleep(delay)
    automationhat.relay.three.on()
    location = ("south")
    return "<h1>Train Moving Towards the South End</h1>"

@app.route("/stop")
def quitInputFail():
    running = False
    print(bcolors.WARNING + "ERROR: input failure")
    automationhat.relay.one.off()
    automationhat.relay.two.off()
    automationhat.relay.three.off()
    return("<h1>System has stopped.</h1>")
#    uinput = input("Restart? (Y/N)")
#    if uinput == ("n"):
#    running = ("false")
#    else:
#        print("Restarting...")
ncountdown = int(1)

@app.route("/location")
def position():
    return ("<h1>"+appblueprint.location+"</h1>")
#    if appblueprint.location == ("north"):
#        return("<h1>Tram is at the North end</h1>")
#    elif appblueprint.location == ("south"):
#        return("<h1>Tram is at the South end</h1>")
#    else:
#        return("<h1>Location is unkown: failure imminent.</h1>")
@app.route("/start")
def start():
#    running = True
    appblueprint.appstart()
    return("<h1>System is starting...</h1>")

#if running == True:
'''#three apostrophes here
    while running == True:
#    running = ("true")
        if(automationhat.input.one.read() == False):
            if( automationhat.input.two.read() == False):
                quitInputFail()
                break
        if(automationhat.input.one.read() == False):
            northSide()
            ncountdown = (countdown)
        if(automationhat.input.two.read() == False):
            southSide()
            ncountdown = countdown
        time.sleep(0.0625)
        ncountdown = (ncountdown - 1)
        if (ncountdown == 0):
            quitInputFail()
            break
'''#three apostrophes here
