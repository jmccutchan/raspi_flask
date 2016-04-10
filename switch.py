import RPi.GPIO as GPIO

LED_PIN = 11
SWITCH_PIN = 24

class Led(object):
  def __init__(self):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(SWITCH_PIN, GPIO.IN)


  def read_switch(self):
    return GPIO.input(LED_PIN)

  def set_led(self, value):
    GPIO.output(LED_PIN, value)
