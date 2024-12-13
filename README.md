# TrainNet
Automated DC model train controller for the Raspberry Pi using the AutomationHAT

# Notes
This is for a short shuttle-style layout where the train changes direction at either end, rather than a looped layout.
Note that if approximately 15 seconds elapse since the last detector was triggered, the system will shut itself off and cut the power to the tracks. - i might remove this in future.
If the two detectors give an output of "0" at the same time the system will shut off and cut power.

# Prerequisites
This control system requires a few things
- A Raspberrry Pi (tested and working on 2b)
- Flask and AutomationHAT's libraries installed (make sure you install Flask first!)
- The AutomationHAT itself
- 2x MH Infrared detectors
- 0-12VDC power supply
- Some wires
- A lot of patience

# Set up
Make sure that the HAT is plugged into the Pi's GPIO port and wire the two terminals from your train set's power supply to the COM relay terminals on relays 1 and 2 respectively.
The Normally Open (NO) terminal from Relay 1 should be wired to the rail closest to you, with the Normally Closed (NC) terminal wired to the rail furthest from you. Relay 2's NO terminal should be wired to the farthest rail, and the NC terminal should be wired to Relay 3's COM terminal. Lastly, Relay 3's NO terminal should be connected to the rail closest to you. Relay 3's NC terminal should be left free. This completes the wiring of the track to the computer system.

We now need to connect our two IR detectors to the HAT. Note that the detectors I have used send an output of 1 by default when nothing is in front of them, and 0 when there is something there, so you may need to change the setting in appblueprint.py (tutorial comingsoon)
The power and ground connections of the two sensors can be connected to the 5v and GND connectors on the HAT respectively. The outputs of the sensors can be connected to inputs 1 and 2 on the HAT. I personally recommend the sensor on the left-hand side of the layout be connected to Input 2 and the right-hand side connected to Input 1. You now need to make sure you have AutomationHAT's libraries mounted, navigate to where you saved this project and run  app.py with "flask run" (actual formatting coming soon)
Once it has started, navigate to 127.0.0.1:5000 in a browser and make sure the train is next to one of the IR detectors and click "Start". The system should start and the train should move back and forth between the two sensors automatically. To stop the system, simply click "Stop". In future I hope to pretty-up the UI and add features like being able to see the location/ status in real time.
