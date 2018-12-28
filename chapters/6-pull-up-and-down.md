## Chapter 6 - Pull-up and down resistors

A pull-up or pull-down resistor is a resistor that "pulls" a point that is *floating* to a positive voltage (pull **up**), or to ground (pull **down**). This is used in *digital circuits* because everything has to be either on or off.

### What is a floating point?

Say we wanted to connect a button to a controller (we do want to do that, a lot), how do we wire it up?

For starters, it's possible to wire it directly to the positive rail like this:

### positive switch image here

But how do we want know what the voltage is at the `pin` when the switch is open (not pressed)?

We don't! The point is *floating*, which means we can't tell what the voltage at the point will be. When something is supposed to be either "on" or "off", floating is the opposite of what we want, because we have no idea what it is.

So what we do is use a resistor to *pull* the voltage to a known state when it would be floating. This is a pull **up** resistor circuit:

### pull up resistor image here

When the switch is open, the resistor pulls the voltage at the pin to be 3.3V, and when it is closed, this connects the pin directly to ground (0V). So the button works now!

A pull down resistor looks like this:

### pull down resistor here.

In this case the opposite is true, when the switch is open the voltage at the pin is 0V, and when the switch is closed, the voltage is 3.3V.

### Does it matter if I use pull-up or down?

No, it's just a matter of preference. It's much more important to know what each of them means (and write your code accordingly), and that you need to use one of them when you're connecting a button (or basically anything) to a digital input.
