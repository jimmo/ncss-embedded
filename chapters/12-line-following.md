## Line following

We've already seen how we can use the sensors on the bottom of the bit:bot to detect masking tape. In Python, we read the current state of these sensors with `pin11` and `pin5`. We can make a very simple line following program by reading whether the sensors are over the masking tape and applying a correcting rotation when they are:

```python

while True:
  if pin11.read_digital() == 1:
    # left side on masking tape, turn left.
  if pin5.read_digital() == 1:
    # right side on masking tape, turn right.
  else:
    # all clear, drive straight.
```

### Control algorithms

The code above is an example of a "control" algorithm -- it continuously adjusts an output (e.g. the motors) in order to maintain a desired state (following the line), and optionally reads some sensor or sensors (the light sensors) in order to measure the output. You see control algorithms everywhere - here are some examples:

 * An automatic light switch turns off the light after it's been on for 10 minutes.
 * An automatic light that detects motion to keep the light on while people are in the room.
 * An air conditioner monitors the current room temperature and turns on or off the compressor, heater and fans. (Or similarly, a fridge).
 * The cruise control system in a car monitors the speed, and adjusts the accelerator to maintain a constant speed.

There are two main categories of control algorithms, "open-loop" and "closed-loop" control. The difference being whether they use feedback from sensors to change their behaviour.

Since these algorithms are very commonly used to control systems, there are a couple of bits of jargon that you may come across when reading about control algorithms. The three most important terms that you will come across repeatedly are:
* Process value (pv) -- the current measured value (e.g. in degrees C)
* Set point (sp) -- the desired state (i.e. the desired temperature in degrees C)
* Output (op) -- the current control output (i.e. is the compressor on or off)

#### Open-loop control

Like the first automatic light example above, no feedback from sensors is used, so the control loop is said to be "open". Instead some model of how the system operates is used to "guess" what will happen (in this case the simple model is that people leave the room within 10 minutes).

Here are some examples from the bit:bot:
* Drive forward 1 metre by turning on both motors at full speed for 3.7 seconds.
* Turn left 90 degrees by turning the the motors in opposite directions for 0.9 seconds.
* Follow a course by pre-programming motor movements.

You might recognise this form of control from the previous lab. When we preprogrammed the motor powers and rotation times to get our robot to move in certain ways in the previous lab we were doing *open loop control*.

Open-loop control is much simpler to implement, but tends to make it very difficult to get accurate results. For example, if the battery is lower, then the time needed to drive forward 1 metre will be longer. If the torque of the two motors is different (due to imperfections in the gears, fluff on the tyres etc.) then we have to adjust the powers in our program with no guarantee they won't change. *For this reason it's very difficult to do line following with open loop control!*

#### Closed-loop control

The system operates in a loop, where sensor readings provide "feedback" into the control algorithm. The fridge or air conditioner is a great example of this -- when the temperature is too high, it turns on the cooling, and when it's too low it turns it off.

[comment]: # TODO: Closed Loop diagram

Here are some examples from the bit:bot:
* Drive forward 1 metre by using the ultrasonic distance sensor to measure how far has been travelled.
* Turn left 90 degrees using the micro:bit's compass.
* Line following using the line sensors on the bit:bot.

The main challenge with closed-loop control is getting good results from the sensors, and figuring out how to translate the sensor inputs (`pv`) into control outputs (`op`). 

[comment]: # TODO: Move the below definitions somewhere else, as this does not flow
[comment]: #  * accuracy: does the sensor reflect the true value of what it's measuring
[comment]: #  * precision: how noisy is the sensor

### "Bang bang" control

You've probably heard your fridge loudly "click" as the compressor turns on or off. This is an example of "bang bang control", named because it switches abruptly between two states.

A very basic implementation might look something like this:

```python
sp = 3
while True:
  pv = fridge.temperature()
  if pv < sp:
    compressor.off()
  else:
    compressor.on()
```

The problem with this simple approach is that the compressor will *oscillate* very quickly between on and off as the fridge hovers around 3 degrees C. This will be particularly bad if the temperature sensor is noisy.

To improve this, we have two options. The first is to simply slow down our loop, preventing the system from changing state too often. In this case, adding a `sleep(30 * 60 * 1000)` at the end of the loop to only allow the compressor to be adjusted every 30 minutes. This will result in our algorithm being less responsive to temperature changes in the fridge, but will at least prevent this oscillation.

The other option is to use a range of sensor values rather than a specific threshold value. In the example below, we still target 3 degress C, but allow a movement down to 2 and up to 4 before changing the compressor state.

```python
sp = 3
while True:
  pv = fridge.temperature()
  if pv < sp - 1:
    compressor.off()
  elif pv > sp + 1:
    compressor.on()
  # Otherwise compressor stays in the same state.
  sleep(60 * 1000)
```

The simplest possible line following algorithm works in much the same way, however there's a key difference. In a fridge, we can measure the PV (current temperature) extremely well, but only have very crude control over the OP (compressor on/off). On a bit:bot we have very good control over the OP (motor speed), but a very limited way to measure the PV (are we currently over a line).

*Note: Some modern fridges have a VFD (variable frequency drive) compressor that allows much finer control over the compressor power. This lets you use a much more efficient control algorithm, resulting in a quieter and more energy efficient fridge.*

### Proportional control

TODO

*Note: this is the first part of a commonly used control algorithm called a PID Controller. PID stands for proportional-integral-derivative.*

### Line following

For our line following algorithm, the obvious approach is to use the following values:
 * sp - make both sensors read "dark".
 * op - motor speeds.
 * pv - current sensor readings ("light" or "dark").

Try experimenting with the bang bang controller above in order to make your bit:bot follow a track. Notice how the bit:bot will tend to bounce on and off the line, and have some difficulty following corners. Try adjusting the `sleep` in the loop to see how that impacts the bit:bot's ability to follow the line.

One of the main ways to improve this is to look at how to get a better indication of how far onto the line the sensor is. By recording how many times we see the line, we can get a crude approximation of this. The assumption here is that once the bit:bot drives onto the line, driving forward is likely to keep it on the line. This is a reasonable assumption, especially over short time periods.

```python
count_left = 0
count_right = 0
while True:
  if pinA.read_digital() == 1:
    count_left += 1
  else:
    count_left = max(0, count_left - 1)
  if pinB.read_digital() == 1:
    count_right += 1
  else:
    count_left = max(0, count_right - 1)

  if count_left > 4:
    # turn left
  elif count_right > 4:
    # turn right
  else:
    # drive straight

  sleep(500)
```

The example above is using the number of times we've detected the line as an approximation of how far we've driven onto the line. Like the fridge example above where we used a range of values, this means that the bit:bot will be less sensitive and allow for smoother movement and less oscillation.

*Note: this is very similar to the "I" (integral) part of a PID controller.*

## Lab exercises:

1. Experiment with the bang bang controller above and see what sort of lines it can and can't follow.
2. Improve on the counting controller by adjusting the motor speed proportionally to the counts. So the higher the count goes, the faster the bit:bot will turn in that direction.
