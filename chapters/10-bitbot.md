## Robotics with the Micro:Bit

Aside from working with sensors and screens, we can also hook up our micro:bits to various types of robot. For our labs we are going to be working with the bit:bot. The bit:bot is a robot designed specifically for the micro:bit, and interfaces with the micro:bit via the edge connector. It has the following features:

* Line following sensors that detect the lightness of the surface that the bit:bot is driving on
* Light sensors that allow it to detect the ambient light on either side
* Two geared motors, allowing differential steering
* A buzzer (which makes a buzz noise)
* 12 programmable RGB LEDs
* Optional accessories, including a distance sensor and a claw

<span style="color:red">**Warning!!**</span> The gearboxes on the bit:bot are a little fragile, and the teeth on the gears can break if too much torque is applied. Don't try to hold the wheels from spinning while the motors are on.

[comment]: # (The below should be reworded... Don't like how this turned out)

Over the course of the next two labs, we are going to start off by playing with the features of the bit:bot, before getting into some algorithms for controlling the bit:bot a bit more intelligently.

### Getting Started

The bit:bots are controlled using a micro:bit via the edge connector. Unfortunately, when we have the front attachment installed the micro:bit does not fit into the robot, and the screen is partially obscured. For this reason, most of the time we would want to use the "angle:bit" connector that allows the micro:bit to stand vertically.

Each function on the bit:bot is accessible on a pin through the micro:bit. The below table lists the various functions that you can access:

| Function | Pin | Description |
| --- | --- | --- |
| Left Motor Direction | Pin 8 | Access using `write_digital`<br>`0 - Forward`<br>`1 - Backwards` |
| Left Motor Speed | Pin 0 | Speed `0 - 1023` with `write_analog` |
| Right Motor Direction | Pin 12 | Access using `write_digital`<br>`0 - Forward`<br>`1 - Backwards` |
| Right Motor Speed | Pin 0 | Speed `0 - 1023` with `write_analog` |
| Left Line Sensor | Pin 11 | Access using `read_digital`<br>`HIGH` on a reflective surface<br>`LOW` on a dark surface |
| Right Line Sensor | Pin 5 | Access using `read_digital`<br>`HIGH` on a reflective surface<br>`LOW` on a dark surface |
| Neopixels | Pin 13 | RGB LEDs around the edge of the bit:bot.<br>Access using the `neopixel` module |
| Buzzer | Pin 14 | Makes a beeping noise, when accessed using `write_digital` |
| Light Sensor Select | Pin 16 | Select upwards facing light sensor to read.<br>`LOW` - Left Sensor<br>`HIGH` - Right Sensor |
| Light Sensor Input | Pin 2 | Reads the upwards facing light sensors on the left/right of the micro:bit.<br>Returns a value between `0-1023` |

If you ever need it, this information is also helpfully printed on the bottom of the bit:bots.

**NOTE** The light sensors are not useful for line following, for that task you must use the line sensors, which return a digital value.

#### Powering the bit:bot

In order to use any of the functionality on the bit:bot, the bit:bot needs to be switched on using the switch at the back of the robot. The bit:bots are powered via three AA batteries which can also be used to power the micro:bit. Confusingly, if the micro:bit is plugged into the PC via the USB cable, the micro:bit will operate, however none of the bit:bot peripherals will be operational, including the motors, light and line sensors.

### Programming

#### Driving
There are four pins that control driving:

* pin8 -- left direction
* pin12 -- right direction
* pin0 -- left speed
* pin1 -- right speed

The direction pins can be set to `LOW` (forward) or `HIGH` (backward), by using `pin8/12.write_digital(0)` or `pin8/12.write_digital(1)` respectively.

The speed pins can be set using PWM (pulse width modulation) by using `pin0/1.write_analog(speed)` where `speed` is a number between `0` and `1023`. To recap, PWM will turn the pin on for a fraction of the time, which has the effect of reducing the speed of the motor (just like how we used it to change the brightness of an LED).

Confusingly the speeds moving in the **reverse** direction are reversed, so to run at quarter speed in the forward direction, we would write speed `256` and to move at quarter speed in the reverse direction, we would write `1023 - 256 = 767`.

For example, to drive the bit:bot forward at 1/4 speed:

```python
pin8.write_digital(0)
pin12.write_digital(0)
pin0.write_analog(256)
pin1.write_analog(256)
```

Or to drive the bit:bot in an arc to the left:

```python
pin8.write_digital(0)
pin12.write_digital(0)
pin0.write_analog(256)
pin1.write_analog(512)
```

To move backwards:
```python
pin8.write_digital(0)
pin12.write_digital(1)
pin0.write_analog(256)
pin1.write_analog(767)
```

To spin on the spot, you can drive the motors in opposite directions:

```python
pin8.write_digital(0)
pin12.write_digital(1)
pin0.write_analog(512)
pin1.write_analog(512)
```

#### Line sensing

The line sensors are connected to `pin11` and `pin5`. They will read `HIGH` or `LOW` depending on whether the surface below them is light or dark respectively. The sensors themselves are the pair of black/blue bumps situated just behind the front coaster on the bottom of the bit:bot. They are made up of an infrared (IR)-LED (the bluish bulb at the front of each sensor) and a photodiode with an IR filter (black bulb at the back of each sensor). Although the IR light is not visible to the naked eye, most mobile phone cameras do not completely block IR light, so if you are curious you can see a purplish-glow from those LEDs.

On a reflective or white surface the light from the LED at the front is reflected back at the photodiode, causing the sensor to read `HIGH`. On a dark or absorbing surface, the sensor will read `LOW`.

For these sensors, the thresholds are fixed and unchangeable, which has led to issues when using the sensors on shiny surfaces, such as tiles. If you would like to use the sensors on tiled surfaces, we recommend either printing a dark line onto white paper, or pulling over a carpet.

For example here is a simple example that stops the bit:bot if it drives from a dark surface onto a light surface.

```python
# Drive forward slowly.
pin8.write_digital(0)
pin12.write_digital(0)
pin0.write_analog(256)
pin1.write_analog(256)

while True:
  left_sensor = pin11.read_digital()
  right_sensor = pin5.read_digital()

  if left_sensor or right_sensor:
    # Detected dark on either sensor, stop the bit:bot.
    pin0.write_analog(0)
    pin1.write_analog(0)
  break
```

During the labs we will usually be following a line made of masking tape against the black carpet. As a result, the sensors will read `HIGH` when the sensors run over the tape.

#### Light sensing

The light sensors on top of the bit:bots, unlike the line sensors, are analog sensors, and so are able to detect a range of different light values. Unfortunately, as there are only 3 free analog pins on the micro:bit, and 2 of those are used to control the motors, we somehow have to multiplex two light sensors onto one analog pins. In order to do this, the bit:bot uses `pin16` to control a switch that selects which sensor should be read, and the sensor value can be read from `pin2`.

For example, to read the left and right sensor values, we can do:

```python
# Select the left sensor
pin16.write_digital(0)
left_sensor = pin2.read_analog()

# Select the right sensor
pin16.write_digital(1)
right_sensor = pin2.read_analog()
```

#### Neopixels

Along the edge of the bit:bots there are 12 RGB LEDs called neopixels. By writing values RGB values to each of these sensors, we can show colors around the edge of the LEDs. The neopixels are chained together on a single pin, such that we don't need to use a pin (or 3) per LED. We will go neopixels in more detail in the next chapter, but as an example of how they work, let's set the 2nd LED to show a dim blue light, and the 8th LED to show a bright green light:

```python
import neopixel

neopixel_pin = pin13 # Control pin for neopixels
neopixel_num = 12 # The number of neopixels in the chain

np = neopixel.NeoPixel(neopixel_pin, neopixel_num)
np[2] = (0, 0, 40) # Format is (r, g, b) with a number between 0-255 for each
np[8] = (80, 0, 0)
np.show()
```

#### Buzzer

The buzzer on the bit:bot have an internal oscillator, and put out a fixed tone when pin 14 is driven `HIGH`. Note that this also means that we are only able to play a single tone with this speaker.

```python
# Play a short beep.
pin14.write_digital(1)
sleep(500)
pin14.write_digital(0)
```
