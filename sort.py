import time as Time
import RPi.GPIO as GPIO
import random as Random
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

  def allOn(self, delay):
    for pin in self.pins:
      pin.on(delay)
    Time.sleep(delay)

  def allOff(self, delay):
    for pin in self.pins:
      pin.off()
    Time.sleep(delay)

  def randomBlinkAll(self, delayBetween = 0.25, delayBlink = 0.25, count = 1):
    while(count):
      print(count)
      pin = Random.choice(self.pins)
      pin.blink(delayBlink)
      count -= 1
      Time.sleep(delayBetween)    

  def randomBlink(self, onDelay = 0.25, offDelay = 0):
    print("random")
    pin = getRandomPin()
    pin.on(onDelay)
    pin.off(offDelay)


  def wave(self, delayBetween = 0.06):
    pins = self.pins
    offset = Random.choice(range(len(pins)))
    print("Target Pin: " + str(offset))
    for index,value in enumerate(pins):
      index = index + offset;
      if 0 <= index and index < len(pins):
	pins[index].on(delayBetween)
        Time.sleep(delayBetween)
    
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
  state = 'off';  #TODO change state to bool
  address = '';

  def __init__(self, value, address):
    self.value = value
    self.address = address
    GPIO.setup(address,GPIO.OUT)
    print("Address: " + str(self.address) + " , Value: " + str(self.value) + " , State: " + self.state)

  def set(self, value):
    self.value

  def on(self, delay = 0.25):
    self.state = 'on';
    GPIO.output(self.address, True)
    Time.sleep(delay)

  def off(self, delay = 0):
    self.state = 'off';
    GPIO.output(self.address, False)
    Time.sleep(delay)
  
  def blink(self, delay):
    self.on(delay)
    self.off()

#_______________________________
# Main
print("--Start")
c = Container()
c.allOn(0.006)
c.allOff(0)
#c.randomBlink(0.06, 0.06, 40)
c.wave()
c.cleanUp()
print("--End")
