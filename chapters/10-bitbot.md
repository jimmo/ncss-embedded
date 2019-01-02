## Robotics with the Micro:Bit

Aside from working with sensors and screens, we can also hook up our micro:bits to various types of robot. For our labs we are going to be working with the bit:bot. The bit:bot is a robot designed specifically for the micro:bit, and interfaces with the micro:bit via the edge connector. It has the following features:

* Line following sensors that detect the lightness of the surface that the bit:bot is driving on
* Light sensors that allow it to detect the ambient light on either side
* Two geared motors, allowing differential steering
* A buzzer
* 12 programmable RGB LEDs
* Optional accessories, including a distance sensor and a claw

**Warning!!** The gearboxes on the bit:bot are a little fragile, and the teeth on the gears can break if too much torque is applied. Don't try to hold the wheels from spinning while the motors are on.

[comment]: # (The below should be reworded... Don't like how this turned out)

Over the course of the next two labs, we are going to start off by playing with the features of the bit:bot, before getting into some algorithms for controlling the bit:bot with a bit more intelligently. At the end of this section, there will be a short challenge that will aim to get you using some of those algorithms for line following.

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
| Neopixels | Pin 13 | RGB LEDs around the edge of the bit:bot. Access using the `neopixel` module |
| Buzzer | Pin 14 | Makes a beeping noise, when accessed using `write_digital` |
| Light Sensor Select | Pin 16 | Select upwards facing light sensor to read.<br>`LOW` - Left Sensor<br>`HIGH` - Right Sensor |
| Light Sensor Input | Pin 2 | Reads the upwards facing light sensors on the left/right of the micro:bit. Returns a value between `0-1023` |

**NOTE** The light sensors are not useful for line following, for that task you must use the line sensors, which return either a digital value.

If you ever need it, this information is also helpfully printed on the bottom of the bit:bots.

#### Powering the bit:bot

In order to use any of the functionality on the bit:bot, the bit:bot needs to be switched on using the switch at the back of the robot. The bit:bots are powered via three AA batteries which can also be used to power the micro:bit. Confusingly, if the micro:bit is plugged into the PC via the USB cable, the micro:bit will operate, however none of the bit:bot peripherals will be operational, including the motors, light and line sensors.

### Programming

#### Driving
There are four pins that control driving:

* pin8 -- left direction.
* pin12 -- right direction.
* pin0 -- left speed.
* pin1 -- right speed.

The direction pins can be set to `LOW` (forward) or `HIGH` (backward), by using `pin8/12.write_digital(0)` or `pin8/12.write_digital(1)`.

The speed pins can be set using PWM (pulse width modulation) by using `pin0/1.write_analog(speed)` where `speed` is a number between `0` and `1023`. To recap, PWM will turn the pin on for a fraction of the time, which has the effect of reducing the speed of the motor (just like how we used it to change the brightness of an LED).

Confusingly the speeds moving in the **reverse** direction are reversed, so to run at quarter speed in the forward direction, we would write speed `256` and to move at quarter speed in the reverse direction, we would write `1024 - 256 = 768`.

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
pin1.write_analog(768)
```

To spin on the spot, you can drive the motors in opposite directions:

```python
pin8.write_digital(0)
pin12.write_digital(1)
pin0.write_analog(512)
pin1.write_analog(512)
```

#### Line sensing

The line sensors are connected to `pin11` and `pin5`. They will read `HIGH` or `LOW` depending on whether the surface below them is light or dark respectively. The sensors themselves are the pair of black/blue bumps situated just behind the front coaster on the bottom of the bit:bot. They are made up of an IR-LED (the bluish bulb at the front of each sensor) and a photodiode with an IR filter (black bulb at the back of each sensor). On a reflective or white surface the light from the LED at the front is reflected back at the photodiode, causing the sensor to read `HIGH`. On a dark or absorbing surface, the sensor will read `LOW`.

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

TODO

#### Neopixels

See the next chapter

#### Buzzer

The buzzer on the bit:bot is a bit different to the speakers we've seen in earlier chapters. It has a set frequency/note, and can only be turned on or off.


```python
# Drive forward slowly.
pinA.write_digital(0)
pinB.write_digital(0)
pinC.write_analog(256)
pinD.write_analog(256)

while True:
  if pinA.read_digital() == 1 or pinB.read_digital() == 1:
    # Detected dark on either sensor, stop the bit:bot.
    pinC.write_analog(0)
    pinD.write_analog(0)

	# Play a short beep.
	pinF.write_digital(1)
	sleep(500)
	pinF.write_digital(0)
	break
```

## Lab exercises

1. Experiment with setting different speeds and directions.
 * Does your bit:bot drive in a perfectly straight line? Can you come up with speeds for each motor that does make it drive straight.
2. Make a simple radio-controlled car using the micro:bit radio. When a button is pressed on the controller, toggle between two modes:
 * Driving forward at 100% speed.
 * Reversing in an arc to the left.
 Play a beep sound when changing modes.
 (This is how cheap radio-controlled car toys in the 90's worked as they only had a very simple radio that allowed for a single button!)
3. Make your radio controlled car automatically change mode when it drives over a masking tape line on the ground.
4. Improve the radio control to allow for four modes:
 - drive forwards (both buttons pressed)
 - turn left (left button only)
 - turn right (right button only)
 - stop (no buttons pressed)
5. Make the bit:bot follow a masking tape line by:
 - driving forwards when both sensors detect dark
 - turning slowly left when the left sensor detects light
 - turning slowly right when the right sensor detects light
 - stopping when both detect light
 How well does this work? Can your bit:bot follow sharp turns in the line? How does the turning speed affect things? What about different ways of turning (i.e. arc left vs spin left).
6. Make your bit:bot detect when it's driven into a "garage" and stop automatically. i.e. the ambient light decreases.
