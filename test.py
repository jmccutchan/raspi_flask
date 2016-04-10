import time
from switch import Led



light= Led()

switch = light.read_switch()

print('Switch: {0}'.format(switch))


print('Blinking LED (Ctrl-C to stop) ....')
while True:
  light.set_led(True)
  time.sleep(0.1)
  light.set_led(False)
  time.sleep(0.1)



