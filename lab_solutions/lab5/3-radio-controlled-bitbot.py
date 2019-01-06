from microbit import *
import radio

CHANNEL = 19

# Movement functions

def drive_forwards(speed):
  pin8.write_digital(0)
  pin12.write_digital(0)

  pin0.write_analog(speed/100*1023)
  pin1.write_analog(speed/100*1023)
  
def reverse_arc_left():
  pin8.write_digital(1)
  pin12.write_digital(1)

  pin0.write_analog(700)
  pin1.write_analog(400)


is_driving_forwards = True
radio.config(channel=CHANNEL)
radio.on()
# Stopped at first then moving forwards or reversing to the left
while True:
  msg = radio.receive()
  if msg is not None:
    if msg == 'FORWARDS':
      display.show(Image.ARROW_N)
      drive_forwards(50)
    elif msg == 'REVERSE_LEFT':
      display.show(Image.ARROW_SW)
      reverse_arc_left()
