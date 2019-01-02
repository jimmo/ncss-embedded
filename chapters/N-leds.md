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

## Lab exercises

1. Wire up some LEDs using the breadboards and the grove jumper wires.
1.1. Experiment with different resistor values.
1.2. Make a program that animates some resistors in a row.
2. Wire up an RGB LED. These contain three individual LEDs (red, green, and blue) and are wired up like this:

#### TODO: RGB LED diagram.

2.1. Make a program that cycles between red, green and blue.
2.2. What if you turn on the colours at the same time, figure out which combinations give you pink, cyan, yellow, and white. You might need to adjust the resistors to balance the brightness of the different colours.

3. Can you think of a way to adjust the brightness of the LED? *Hint: what if you turn the LED on and off really quickly?* (TODO: is this hint too strong?)
3.1. Use this to get other colours from the RGB LED.
