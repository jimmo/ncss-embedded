## 4tronix bit:bot

The bit:bot is a robot designed for the micro:bit, primarily designed for line following. It has the following features:
 * Line following sensors that detect the lightness of the surface that the bit:bot is driving on.
 * Light sensors that allow it to detect the ambient light on either side.
 * Two geared motors, allowing differential steering.
 * A buzzer.
 * 12 programmable RGB LEDs.
 * Optional accessories, including a distance sensor and a claw.

**Warning!!** The gearboxes in the bit:bot are a little fragile, and the teeth on the gears can break if too much torque is applied. Don't try to hold the wheels from spinning while the motors are on.

### Connecting the micro:bit

Most of the time you'll probably wnat to use the "angle:bit" connector that allows the micro:bit to stand vertically. This will allow you to leave the USB cable connected to the micro:bit.

On the bottom of the bit:bot, there's a helpful description of which pins control which functionality.

### Powering the bit:bot

In order to use any of the functionality on the bit:bot, the bit:bot needs to be switched on. This will also power the micro:bit.

However, if a USB cable is connected to the micro:bit, then just the micro:bit will continue to function as normal. We recommend turning off the bit:bot whenever you're not currently driving it.

### Programming

#### Driving
There are four pins that control driving:

* pinA -- left direction.
* pinB -- right direction.
* pinC -- left speed.
* pinD -- right speed.

The direction pins can be set to `HIGH` (forward) or `LOW` (backward), by using `pinN.write_digital(0)` or `pinN.write_digital(1)`.

The speed pins can be set using PWM (pulse width modulation) by using `pinN.write_analog(speed)` where `speed` is a number between `0` and `1023`. To recap, PWM will turn the pin on for a fraction of the time, which has the effect of reducing the speed of the motor (just like how we used it to change the brightness of an LED).

For example, to drive the bit:bot forward at 1/4 speed:

```python
pinA.write_digital(0)
pinB.write_digital(0)
pinC.write_analog(256)
pinD.write_analog(256)
```

Or to drive the bit:bot in an arc to the left:

```python
pinA.write_digital(0)
pinB.write_digital(0)
pinC.write_analog(256)
pinD.write_analog(512)
```

To spin on the spot, you can drive the motors in opposite directions:

```python
pinA.write_digital(0)
pinB.write_digital(1)
pinC.write_analog(512)
pinD.write_analog(512)
```

#### Line sensing

The line sensors are connected to `pinA` and `pinB`. They will read `HIGH` or `LOW` depending on whether the surface below them is light or dark.

Here's a simple example that stops the bit:bot if it drives from a dark surface onto a light surface.

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
	break

Typically we want the bit:bot to follow a masking tape line on dark carpet, so the sensors should stay in the dark area, and turn the bit:bot if they detect a light surface.

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
