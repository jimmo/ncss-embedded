## Neopixels & programmable LEDs

As well as the line following and light sensors, the bit:bots also have 12 programmable RGB LEDs. These are commonly known as "Neopixels", however their real part name is `WS2812B`.

On the bit:bot, the 12 LEDs are arranged in two strips of 6. You can also buy them in pre-made flexible strips.

### Programmable LEDs
We've seen how to control an LED and change its brightness using PWM on the micro:bit. To recap, we connect the LED to the pin, use a current limiting resistor to set the maximum brightness, then use PWM to control how much time the LED spends turned on (which is effectively the brightness).

A regular RGB LED is just a red, green, and blue LED inside the same bulb, so we use the same method to control the brightness of each of the three primary colours, which lets us create any colour combination we like.

The problem is that this takes a lot of pins on our micro:bit, and needs a lot of resistors. Imagine trying to do this for more than 10, let alone hundreds or thousands of LEDs.

Programmable LEDs, on the other hand, have tiny integrated circuits inside of them, and we can send digital messages to them to set the colour and brightness. They also chain together, so by having our micro:bit connected to just the first one, they will send the messages along the chain to control all of them.

### TODO: Neopixel wiring diagram here

### Programming

```python
import neopixel
leds = neopixel.Neopixel(12, pin14)  # TODO, arg order, pin number.

for i in range(12):
  leds[i] = (128, 0, 0,)
leds.show()
```

This uses the built-in `neopixel` module that is included with micro:bit MicroPython. The code constructs an instance of the Neopixel class, telling it how many LEDs we have in the chain (`12`), and which pin the first one is connected to (`pin14`). You can check the pin number by looking at the notes on the bottom of the bit:bot.

This gives us an object, `leds`, which behaves like a list of tuples of `(red, green, blue)`. We can set the colour and brightness of any LED by assigning to that element of the list. So `leds[3] = (0, 255, 0,)` would set the fourth LED to green at full brightness. In the example above, we set all 12 LEDs to red at half brightness.

Whenever you change any LEDs, you need to call the `show` method to send the new information to the LEDs. You can also use the `clear` method which will set all the LEDs to `(0, 0, 0,)` and call `show` for you.

### Colour mixing

Here are some example colours:

```
COLOUR_BLACK = (0, 0, 0,)
COLOUR_WHITE = (255, 255, 255,)
COLOUR_RED = (255, 0, 0,)
COLOUR_GREEN = (0, 255, 0,)
COLOUR_BLUE = (0, 0, 255,)
COLOUR_PINK = (255, 0, 255,)
COLOUR_YELLOW = (0, 0, 0,)  # TODO
COLOUR_ORANGE = (0, 0, 0,)  # TODO
```

### Other types of programmable LED

The main alternative to the WS2812B is the APA102C (commonly known as "Dotstars"). These have two distinct advantages over the WS2812B:
 * They are much easier to program, as they use SPI communications.
 * They have a much higher refresh rate, allowing for video and persistence-of-vision effects.

At NCSS we use WS2812B because of the built-in `neopixel` module, but it's also fairly straightforward to use APA102Cs via SPI. Like the WS2812B, they also run at 5 volts, so will require a level shifter to use from the micro:bit and pyboard/Quokka.

```python
from microbit import *

# TODO
data = bytearray(4 + NUM_LEDS * 4 + 4)
spi.init(mosi=pin0, sclk=pin13, baudrate=1000000)
spi.send(data)
```

There are also variations of the WS2812B and APA102C that add things like a fourth "colour" which is an extra white LED.
