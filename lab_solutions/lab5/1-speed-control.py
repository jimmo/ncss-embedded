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
  
def turn_around():
  pin8.write_digital(0)
  pin12.write_digital(1)

  pin0.write_analog(600)
  pin1.write_analog(423)
  sleep(550)


# Wait a little so it doesn't drive while you're holding it/switching it on then 
#  drive forwards, turn around and drive back
sleep(50)
drive_forwards()
sleep(1000)
turn_around()
drive_forwards()
sleep(1000)
stop()
