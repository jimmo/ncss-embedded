## Pulse Width Modulation

We've seen how to control an LED connected to a pin by using `write_digital` to turn the pin on or off. Once we choose a value for the current limiting resistor however, the brightness is fixed.

The most obvious way to make the brightness change would be to change the pin voltage, as you can see in the formula:

![LED current](http://mathurl.com/y8vbxndb.png)

If the pin voltage decreases, then the current will decrease correspondingly, which will lower the brightness of the LED. Unfortunately, most microcontrollers do not have a way to set a pin voltage to anything other than *digital low* (0V) and *digital high* (often 3.3V or 5V), whereas we'd need some way to set an *analog voltage*. Some microcontrollers may have a device called a "Digital to Analog Converter" (DAC), but typically this will only be connected to one or two pins, and the micro:bit does not have one.

Instead, we use a different technique. If we turn the LED on and off very quickly, then our eye will perceive this as reduced brightness. This also works well for controlling the speed of devices like motors.

So if we had an LED connected to pin0, with a current limiting resistor chosen such that the LED is at full brightness when the pin is turned on, then the following code will make the LED show at half brightness.

```python
from microbit import *
while True:
  pin0.write_digital(1)
  pin0.write_digital(0)
```

Because this loop has no sleeps or delays in it, our eyes will not be able to see the LED flickering as it turns on and off. On the micro:bit, changing a pin from Python takes about 1 ms (millisecond), so the LED is flashing at about 500 Hz.

By adjusting the amount of time it spends on vs off, we can set the brightness to anything we like. The following code will turn on the LED for 1/4 of the total time.

```python
from microbit import *
ON = 1
OFF = 3
while True:
  for i in range(ON):
    pin0.write_digital(1)
  for i in range(OFF):
    pin0.write_digital(0)
```

*Note: there are no sleeps in this code, but we're relying on the fact that `write_digital` takes about 1 ms to run.*

TODO: Waveform diagram

This is called "Pulse Width Modulation" or PWM. Our code is generating pulses, and modulating their width. (Modulation is one thing controlling another thing). Some terminology:

* The **pulse length** is how long the pin is on for. In the first example, it's approximately 1 ms.
* The **period** is the length of time from the start of one pulse to the next. In the first example, this is approximately 2 ms, in the second it is `ON + OFF` ms.
* The **frequency** is how many pulses per second. It is calculated as `1 / period`, so in the first example, `1 / 0.002 = 500 Hz`.
* The duty cycle is the ratio of the pulse length to the period, expressed as a percentage. So the first example is 50%, the second example is 25%. The duty cycle will correspond to the brightness (or the motor speed, etc).

### Built-in PWM support

The micro:bit can do this for you using the `write_analog` method. This method takes the duty cycle, but expressed as a number between 0 (i.e. 0%) and 1023 (i.e. 100%). *Can you guess why 1023 is the maximum? Ask your tutor!*

So the two examples from above would simply become:

```python
from microbit import *
pin0.write_analog(512)
```

```python
from microbit import *
pin0.write_analog(256)
```

This has two big advantages over toggling the pins manually:

* It runs automatically in the background, allowing your code to do other things.
* The timing is more precise and can run at a higher speed.

The default period is 20 ms (50 Hz), however this can be adjusted using `set_analog_period` or `set_analog_period_microseconds`.

## Lab exercises

1. Make an LED pulse on and off by smoothly changing the brightness up and down.
1.1. Try different pulsing patterns (e.g. sinusoidal).
2. Use an RGB LED to experiment with colours.
2.1. Generate a rainbow sequence, smoothly changing through the spectrum.
