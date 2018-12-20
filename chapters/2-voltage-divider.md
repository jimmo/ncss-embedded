## Chapter 2 -- Voltage Dividers

A voltage divider is one of the most common circuits that exist! 

Given a voltage input, it produces a fraction of the input as the output.

![Voltage divider](https://upload.wikimedia.org/wikipedia/commons/2/21/Resistive_divider2.svg)

The equation for the output is:

<img src="https://latex.codecogs.com/gif.latex?V_{out}&space;=&space;V_{in}\frac{R_1}{R_1&space;&plus;&space;R_2}" title="Voltage divider equation" />

The voltage divider produces a smaller voltage using the ratio in the equation. You might have used one in a volume control like this:

### volume control image here

You can also use a voltage divider to produce a reference voltage from a known higher voltage source (assuming no load).

At NCSS, the main way we'll be using voltage dividers is to read in analog sensors, like a joystick, flex sensor, or any sensor that *changes its own resistance*. 

It's hard for us to read resistance directly, but the micro:bit is *really* good at measuring voltages. So by adding *another* resistor that is known, applying an input voltage that is known, but measuring the output voltage, we can calculate the resistance of the sensor with our voltage divider!

### picture here

### How do we know what the resistance means in the real world?

That depends on the sensor. Usually, looking up the datasheet will tell us what it means. But if it's something like a light-sensor, we can *calibrate* the sensor ourselves by measuring the voltage at lots of light, and measuring it again at no light, and getting a *threshold* of what we want to call enough light to trigger whatever action we want to take.


