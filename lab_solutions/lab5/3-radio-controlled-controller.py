from microbit import *
import radio

CHANNEL = 19

# Movement functions


is_forwards = True
radio.config(channel=CHANNEL)
radio.on()
radio.send('FORWARDS')
while True:
  if button_a.was_pressed():
    is_forwards = not is_forwards
    radio.send('FORWARDS' if is_forwards else 'REVERSE_LEFT')
    display.show(Image.ARROW_N if is_forwards else Image.ARROW_SW)
