## Ultrasonic distance sensing

The bit:bots include an ultrasonic distance sensor which connects to the header at the front. *Note: make sure you use the angle:bit to connect your micro:bit so that the USB cable does not get in the way.*

These ultrasonic sensors work by measuring the echo time ("time of flight") of an untrasonic sound pulse. Sound travels at approximately 340 metres/second, or in other words, 1 centimetre every 29.4 microseconds. That's too fast to measure with a stopwatch, but no trouble at all for a microcontroller.

*This is how you can measure approximately how far away lightning is by measuring the time between the flash and the boom and multiplying by 1000/340 (which is ~3).*

#### TODO: diagram

These sensors have four pins:
 * Power (5V)
 * Ground
 * Trig
 * Echo

### TODO: waveform

*Note: although the distance sensors require 5V, the bit:bot takes care of this for us. If you were connecting an ultrasonic sensor directly to the micro:bit, you'd need additional circuitry.*

To start a pulse, you send a brief pulse on the trig line, then measure how long until there's a pulse on the echo line. Because we want the timing to be accurate, we used a special built-in MicroPython function to time the pulse for us.

# TODO: we can also use the length of hte pulse rather than the delay to the pulse? Which is better?

```
from microbit import *
import machine
# TODO
machine.time_pulse_us(pinN, 0, 1)
```

Confusingly, on the bit:bot, the `echo` and `trig` lines are connected together into a single micro:bit pin, so you need to first send the trigger, then switch the pin back to input, then time the pulse.

```
from microbit import *
import machine

def distance_cm():
  pinN.write_digital(1)
  pinN.write_digital(0)
  pinN.read_digital()
  tof = machine.time_pulse_us(pinN, 0, 1)
  return tof / 29.4

while True:
  print(distance_cm())
  sleep(500)
```
