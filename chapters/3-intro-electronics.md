## Chapter 3 -- Electronics

Since we're learning all about embedded development, we need to spend some time learning about electronics. How do microcontrollers send information between sensors, displays and other microcontrollers? Electronics is a huge field, and encompasses a large number of topics, so it's impossible for us to cover every topic exhaustively. So, rather than trying to exhaustively cover the field of electronics, what we'll try and do is introduce enough topics that you can put together simple circuits, hook components together and start to understand what is going on with the embedded devices you see around you.

Since there is such a large number of topics to cover, don't worry if this doesn't all make sense on your first readthrough. Most of this is stuff that you will have a chance to learn along the way. But since we can't cover everything in the limited time we have, this section is meant to be a reference to come back to as the program progresses.

### Voltages and Currents



To build any electronic device, we need to have a way of sending signals between controllers, sensors and outputs. The
The way we send those signals is by sending electrons from one place to another, the movement of electrons through is circuit is called *current*.

The way create a current is to apply a *voltage*, a difference in voltage between two points in a circuit will cause current to flow.

So there are two things we want to keep track of in electronic circuits: **voltage** and **current**.

Two things to remember:
* **Voltage is _across_ things**
* **Current flows _through_ things**

The voltage at any point in the circuit generally means **the potential difference between that point and ground**.

### Relating voltage and current: resistors

The current *through* a device is proportional to the voltage *across* it.

This gives us the relationship called Ohm's Law, which is the most important equation in electronics.

![Ohm's Law](https://latex.codecogs.com/svg.latex?V%20%3D%20IR)

The *voltage* is the *resistance* times the *current*.
**Remember this equation!** Seriously. It's the foundation of everything.

### What is resistance?

Like it's name would suggest, it resists current flow. Current can flow much easier through a circuit with lower resistance, but very little current will flow in a circuit with a large resistance. More resistance, less electrons flowing. The unit of resistance is an ohm (Ω).

### Series and parallel

Resistors in series look like this:

![Resistors](https://upload.wikimedia.org/wikipedia/commons/1/11/Resistors_in_series.svg)

To total resistance is just the sum of their resistances together.

![Resistors in series](https://latex.codecogs.com/svg.latex?R_%7Btot%7D%20%3D%20R_1%20&plus;%20R_2%20&plus;%20...%20&plus;%20R_n)

So when something is *in series*, it means that the only way for current to flow is through the device.

When something is in *parallel*, it means there are *multiple paths for current to flow*.

So parallel resistors look like this:

![Parallel resistors](https://upload.wikimedia.org/wikipedia/commons/0/09/Resistors_in_parallel.svg)

The equation, if you care about that sort of thing....

![Parallel equation](https://latex.codecogs.com/svg.latex?R_%7Btot%7D%20%3D%20%5Cfrac%7B1%7D%7B%5Cfrac%7B1%7D%7BR_1%7D%20&plus;%20%5Cfrac%7B1%7D%7BR_2%7D%20&plus;%20...%20&plus;%20%5Cfrac%7B1%7D%7BR_n%7D%7D)


## Analog and Digital

**Analog** (should be analogue but we're lazy) deals with *continuous* values, or *ranges of values*. So when we want to measure ranges of things, it will generally be an analog circuit.

**Digital** circuits are either *on* or *off*. We don't do ranges anymore, it's a binary world. On or off. 0s or 1s. That's it.

The world is in analog, and digital is us making constraints on it. So if it's a thing like "pressing a button" or "turning on a light", it's digital. If we're *measuring a range*, it's analog.

## Chapter 5 -- Voltage Dividers

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

That depends on the sensor. Usually, looking up the datasheet will tell us what it means. But if it's something like a light sensor, we can *calibrate* the sensor ourselves by measuring the voltage at lots of light, and measuring it again at no light, and getting a *threshold* of what we want to call enough light to trigger an action (like turn on a light, because it's dark).

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

### Hang on, how do I know what resistor to use?

This comes from knowing the *range of values* for your sensor (it will be in the datasheet). So if your sensor ranges from 1 kΩ to 10 kΩ, pick a static resistor around the middle, like 5.6 kΩ. This will mean the range of output values is large.

## Chapter 6 - Pull-up and down resistors

A pull-up or pull-down resistor is a resistor that "pulls" a point that is *floating* to a positive voltage (pull **up**), or to ground (pull **down**). This is used in *digital circuits* because everything has to be either on or off.

### What is a floating point?

Say we wanted to connect a button to a controller (we do want to do that, a lot), how do we wire it up?

For starters, it's possible to wire it directly to the positive rail like this:

### positive switch image here

But how do we want know what the voltage is at the `pin` when the switch is open (not pressed)?

We don't! The point is *floating*, which means we can't tell what the voltage at the point will be. When something is supposed to be either "on" or "off", floating is the opposite of what we want, because we have no idea what it is.

So what we do is use a resistor to *pull* the voltage to a known state when it isn't connected to anything. This is a pull **up** resistor circuit:

### pull up resistor image here

When the switch is open, the resistor pulls the voltage at the pin to be 3.3V, and when it is closed, this connects the pin directly to ground (0V). So the button works now!

A pull down resistor looks like this:

### pull down resistor here.

In this case the opposite is true, when the switch is open the voltage at the pin is 0V, and when the switch is closed, the voltage is 3.3V.

### Does it matter if I use pull-up or down?

No, it's just a matter of preference. It's much more important to know what each of them means (and write your code accordingly), and that you need to use one of them when you're connecting a button (or basically anything) to a digital input.

## Level shifting

Digital circuits involving microcontrollers have a signal level that they use as their "on" voltage level.

On the micro:bit, a `pin1.write_digital(1)` will set the voltage on `pin1` to `3.3V`, that's what "on" means.

But some other circuits might used a signal of `5V` to decide if something is "on". For example, the neopixel LEDs want 5V power and 5V digital signal, which the micro:bit simply can't provide either.

So what we do in this case, is use a level-shifter. In order to do this to the waveform:

![Level shifting](images/level-shifter.png)

The chip that does this in the labs is the 74AHCT125, which converts a `3.3V` input signal to a `5V` output signal (as shown in the diagram above). Level shifting is converting a

Level shifting can be a bit more general in that it is shifting from *any* voltage level to *any other* voltage level, but this is a good example. It is quite common the shift the other way (`5V`→`3.3V` where you might use `74LVC245` chip to do this).

### Why do we even need this?

Some devices are only designed to work at a certain voltage. A `1` might be defined as a voltage above a threshold, and if the logic level coming in is below that value, our device may not detect a `1` that we send.

If a logic level is too high, it might be a value greater than a device will accept, so you could damage the components. It's important to send a value to a device that it expects, so it's important to know the voltage of your microcontroller (on the micro:bit it is `3.3V`), and the voltage the device you are talking to expects.

For example, neopixels (WS2812B is the name of the chip), are designed to run at 5V, the reason is because extra voltage is required to produce the full range of colours from the LED (if you supply less, some colours will not be as bright, so the white looks like an off-brown).

## Light Emitting Diodes (LEDs)

Almost every electronic device has an LED in it. Whether it's just the power light, or some sort of status indicator, or perhaps the device needs to produce a lot of light, they are everywhere.

Although there are many types of lights that can be used in circuits, we almost exclusively use LEDs because of their excellent power efficiency, small size, and ease of use.

#### Theory
LEDs are a type of diode, which is a semiconductor device that contains a special junction that only allows current to pass in one direction. The semiconductor junction in an LED is specially built such that when current is flowing, the *band gap* of the semiconductor results in electron transitions that emit photons of specific wavelenghts. This is how LEDs have different colours, red LEDs produce photons that have a wavelength of approximately 650nm, green are 520nm, etc. By combining different colours (usually the primary colours, red, green, and blue) we can produce a whole rainbow of different colours.

There also exist LEDs that produce light outside the visible range, for example, ultraviolet (~300nm) and infrared (~900nm). Infrared LEDs are used in television remote controls or night vision, and ultraviolet has a wide range of uses from skin therapy to sterilisation and even in the production of white light using phosphors. This is how LED light bulbs you use in your house work, they are often UV LEDs which cause a phosphor to glow.

### Powering an LED
Diodes are *"non-linear"* or *"non-ohmic"* devices, which means that Ohm's law doesn't apply to them. When they are conducting, they have very little resistance, and in the other direction they have a very high resistance.

Something with a very low resistance effectively looks like a short circuit, which means that a lot of current will flow and potentially damage the LED or the thing that is powering it (e.g. the micro:bit pin). So what we need is a way to ensure that only a specific current flows, which is why every time we use an LED, we also need a *current-limiting resistor*.

#### TODO: circuit diagram

Typically we choose a desired brightness for our LED, and look up the LED's *data sheet* to find out what current it needs. Then we choose a resistor using Ohm's Law *(V=IR)* to make that work. Remember that devices in series will all have the same current flowing through them, so the current flowing through the LED will be the same as what flows through the resistor.

Here's the formula to figure out what resistor to use for a desired current:

![LED current](http://mathurl.com/y8vbxndb.png)

The *V<sub>led<sub>* is the *forward voltage drop* across the LED. This is a property of the LED and it will be in the data sheet. Typically it's around 2 volts for a red LED.

So if we have an LED that is rated for 20mA at full brightness and has a forward drop of 2 volts, then we get:

![LED current calculation](http://mathurl.com/y7adcb93.png)

If we wanted it to be less bright, then for 10mA, the same calculations would yield 130 ohms.

Resistors only come in specific values, so just round *up* to the nearest one (e.g. 68 ohms or 150 ohms). But unless you're adjusting for a very specific brightness, what matters more is that you have the resistor at all. So most of the time people just use whatever resistor they have spare above about 300 ohms (330 ohms and 470 ohms are extremely commonly used resistors).

**Summary: If you want to use an LED, you must use a current limiting resistor. In almost all cases, a 330 ohm resistor will do the trick.**

#### More notes on current limiting resistors

* Each LED requires its own resistor. *Can you see why?*
* The resistor can be on either side of the LED, it doesn't matter.
* Sometimes you might choose to "invert" the LED by connecting it to VCC instead, then when you turn *off* the pin, the LED will turn on.
* The micro:bit also has current limiting resistors for its built-in LED grid. *They're really tiny! Can you find them and measure their resistance?*
* Blue LEDs typically have a higher forward voltage drop, so will usually require a lower-value resistor for the same brightness.
