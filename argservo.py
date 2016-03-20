#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
from sys import argv

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 200  # Min pulse length out of 4096
servoMax = 1200  # Max pulse length out of 4096



def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
#while (True):
try:
#       for x in xrange(0, 16):
#               pwm.setPWM(x, 0, servoMin)
#               time.sleep(.3)
#               pwm.setPWM(x+1, 0, servoMin)
#               time.sleep(.2)
#               pwm.setPWM(x, 0, servoMax)
#               pwm.setPWM(x+1, 0, servoMax)
        if str(argv[2]) == "on":
                pwm.setPWM(int(argv[1]), 0, servoMax)
        elif str(argv[2]) == "off":
                pwm.setPWM(int(argv[1]), 0, servoMin)

except KeyboardInterrupt:
        sys.exit()
