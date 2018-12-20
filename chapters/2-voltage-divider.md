## Chapter 2 -- Voltage Dividers

A voltage divider is one of the most common circuits that exist! It looks like this:

![Voltage divider source:Wikipedia](https://upload.wikimedia.org/wikipedia/commons/2/21/Resistive_divider2.svg)

Given a voltage input, it produces a fraction of the input as the output.

The equation for the output is:

![Voltage divider equation](https://latex.codecogs.com/svg.latex?V_%7Bout%7D%20%3D%20V_%7Bin%7D%5Cfrac%7BR_2%7D%7BR_1%20+%20R_2%7D)

The voltage divider produces a smaller voltage using the ratio of resistors, which we can calculate from the equation above. 

You might have used one in a volume control like this:

### volume control image here

You can also use a voltage divider to produce a reference voltage from a known higher voltage source (assuming no load).

At NCSS, the main way we'll be using voltage dividers is to read in analog sensors, like a joystick, flex sensor, or any sensor that *changes its own resistance*. 

It's hard for us to read resistance directly, but the micro:bit is *really* good at measuring voltages. So by adding *another* resistor that is known and applying an input voltage that is known, by measuring the output voltage, we can calculate the resistance of the sensor with our voltage divider!

### picture here

### How do we know what the resistance means in the real world?

That depends on the sensor. Usually, looking up the datasheet will tell us what it means. But if it's something like a light sensor, we can *calibrate* the sensor ourselves by measuring the voltage at lots of light, and measuring it again at no light, and getting a *threshold* of what we want to call enough light to trigger an action (like turn on a light).

Let's see how you might do that in practice! First, the code to calibrate the sensor (which is R2 in our voltage divider circuit). `pin0` is Vout in the circuit diagram, and Vin is the micro:bit power at 3.3V. 

```python
from microbit import *
while True:
  sensor = pin0.read_analog()
  print(sensor)
  sleep(50)
```

then once we have a threshold value, we write a simple `if` statement to trigger the action!

```python
from microbit import *

threshold = 600   # measured during calibration

while True:
  sensor = pin0.read_analog()
  if sensor > threshold:
    pin1.write_digital(1)  # turn on a light
  else:
    pin1.write_digital(0)  # turn it off
```
