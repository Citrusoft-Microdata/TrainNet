import time
import automationhat
countdown = int(5)

while True:
    automationhat.output.one.on()
    time.sleep(5.0)
    automationhat.output.one.off()
    time.sleep(5.0)
    countdown = countdown - 1
    if countdown == 0:
        break
