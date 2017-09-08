import time
import RPi.GPIO as GPIO
import random
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#_______________________________
# Defs
class Container:
  #GPIO address pins
  pin_addresses = [4, 5, 6, 12, 13, 16, 17, 18]	
  pins = []

  def __init__(self):
    value = 0;
    for address in self.pin_addresses:
      value += 1
      self.pins.append(Pin(value,address))
    print("Pins setup")

  def allOn(self, duration):
    for pin in self.pins:
      pin.on()
    time.sleep(duration)

  def allOff(self, duration):
    for pin in self.pins:
      pin.off()
    time.sleep(duration)

  def random():
    print("random")
    
  def cleanUp(self):
    GPIO.cleanup()
    print("Pins clean")

  def toString(self):
    result = '';
    for pin in self.pins:
      result += pin.toString() + '\n'
    return result

class Pin:
  value = '';
  state = 'off';
  address = '';

  def __init__(self, value, address):
    self.value = value
    self.address = address
    GPIO.setup(address,GPIO.OUT)
    print("Address: " + str(self.address) + " , Value: " + str(self.value) + " , State: " + self.state)

  def set(self, value):
    self.value

  def on(self):
    self.state = 'on';
    GPIO.output(self.address, True)

  def off(self):
    self.state = 'off';
    GPIO.output(self.address, False)

#_______________________________
# Main
print("--Start")
c = Container()
c.allOn(2)
c.allOff(1)
c.cleanUp()
print("--End")
