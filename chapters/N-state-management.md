## Program state

Many of the programs we've written so far are *stateless* which means that the program acts only on its current input.

As the programs get more sophisticated they need to remember more *state*, allowing them to use past inputs to make decisions.

Some examples:

* Remembering a count of the number of times an event has happened.
* Keeping track of a mode (e.g. waiting for player, playing, showing score, etc).
* Tracking a position in a sequence (i.e. entering a specific button sequence).
* Remembering a high score.

### High scores

Often our program state is as simple as a single variable (e.g. a counter), for example the following program which counts the number of times a button has been pressed, and shows it when the other button is pressed.

```python
from microbit import *

count = 0
while True:
  if button_a.was_pressed():
    count += 1
  if button_b.was_pressed():
    display.show(count)
	count = 0
```

Another very common pattern is to keep track of a minimum or maximum (for example a high score). To calculate a highest score, the pattern would look something like:

```python
high_score = 0
while True:
  score = play_game()
  if score > high_score:
    high_score = score
```

For calculating a lowest score, we do the opposite. This program measures reaction time, and shows a star if you beat the previous time.

```python
from microbit import *
import random

# Our best time so far
best = 10000

while True:
  # Sleep for a random time between 1 and 2 seconds.
  sleep(1000 + random.randint(0, 1000))

  # Start the timer.
  display.show(Image.SQUARE)
  start = running_time()

  # Clear the button detection (in case they're already holding the button).
  button_a.was_pressed()

  # Wait for the next button press.
  while True:
    if button.a.was_pressed():
	  break

  # Stop the timer.
  finish = running_time()
  display.clear()

  # Check if this is the best time.
  t = finish - start
  if t < best:
    # Update the best time.
    best = t
    display.show(Image.HAPPY)
  else:
    display.show(Image.SAD)
  sleep(1000)

  # Reset.
  display.clear()
```

### Detecting sequences.

Sometimes it's useful to remember where we are in a sequence of events. For example, detecting a specific sequence of button presses, e.g. 'A' 'B' 'A' 'A' 'B'. In this case a good way to do it is to have a list of expected events, and keep track of how far we've made it through the list.

```python
LIST = [...]

def wait_for_sequence():
  for item in LIST:
    # check if the most recent event matches `item`
    if event != item:
      # Incorrect
      return False
  # We matched all events in sequence.
  return True
```

The next step is coming up with a way to detect the correct events:

```python
from microbit import *

# This function waits for a button press
# and returns true if it was the expected one.
def expect(btn):
  while True:
    if button_a.was_pressed():
      return btn == 'A'
    if button_b.was_pressed():
      return btn == 'B'

def wait_for_code(code):
  for c in code:
    if not expect(c):
      return False
  return True

while True:
  if wait_for_code('ABAAB'):
    display.show(Image.HAPPY)
  else:
    display.show(Image.SAD)
  sleep(1000)
  display.clear()
```

### Program modes

Some programs will need to operate in distinct modes at different times. When we move between these modes sequentially, this is fairly straightforward to implement:

```python
while True
  # Mode 1
  while True:
    # Do stuff for mode 1
    if finished:
      break

  # Mode 2
  while True:
    # Do stuff for mode 2
    if finished:
      break

  # ... etc
```

#### TODO: State machine diagram for linear states.

What if we need to be able to move between states? For example, mode 1 might be a menu system, and depending on which button we press, we need to move to one of modes 2, 3 or 4. At the moment, when a mode finishes, the inner loop `breaks` and it just goes onto the next mode. We need a way to signal which mode to go to next.

One way to do this is to have a mode (state) variable:

```python
mode = 1

while True
  if mode == 1:
    while True:
      # Do stuff for mode 1
      if something:
        mode = 2
	break
      if something_else:
        mode = 3
	break

  elif mode == 2:
    while True:
      # Do stuff for mode 1
      if something:
        mode = 2
	break
      if something_else:
        mode = 3
	break
      # Do stuff for mode 2

  elif mode == 3:
    # ... etc
```

To make this code clearer, we can define some constants to name the modes.

```python
MODE_MENU = 1
MODE_WAITING_FOR_PLAYER = 2
MODE_PLAYING = 3
MODE_HIGH_SCORES = 4

mode = MODE_MENU

...
if mode == MODE_PLAYING:
  # etc
```
