from microbit import *

# Movement functions

def stop():
  pin8.write_digital(0)
  pin12.write_digital(0)

  pin0.write_analog(0)
  pin1.write_analog(0)

def drive_forwards():
  pin8.write_digital(0)
  pin12.write_digital(0)

  pin0.write_analog(600)
  pin1.write_analog(600)
  
def turn_left():
  pin8.write_digital(1)
  pin12.write_digital(0)

  pin0.write_analog(423)
  pin1.write_analog(600)
  sleep(280)

def turn_right():
  pin8.write_digital(0)
  pin12.write_digital(1)

  pin0.write_analog(600)
  pin1.write_analog(423)
  sleep(280)

def turn_around():
  pin8.write_digital(0)
  pin12.write_digital(1)

  pin0.write_analog(600)
  pin1.write_analog(423)
  sleep(550)

def detect_garage():
  pin16.write_digital(0)
  return pin2.read_analog() < 300

# Wait a little bit so the bot doesn't move while you're switching it on
#  then drive forwards until it's in the garage
sleep(50)
drive_forwards()
while not detect_garage():
  sleep(10)
stop()
