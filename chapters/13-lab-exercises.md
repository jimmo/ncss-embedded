## Chapter 1 -- Introduction
## Chapter 2 -- micro:bit
## Chapter 3 -- Electronics

### LEDs

1. Wire up some LEDs using the breadboards and the grove jumper wires.
1.1. Experiment with different resistor values.
1.2. Make a program that animates some resistors in a row.
2. Wire up an RGB LED. These contain three individual LEDs (red, green, and blue) and are wired up like this:

#### TODO: RGB LED diagram.

2.1. Make a program that cycles between red, green and blue.
2.2. What if you turn on the colours at the same time, figure out which combinations give you pink, cyan, yellow, and white. You might need to adjust the resistors to balance the brightness of the different colours.

3. Can you think of a way to adjust the brightness of the LED? *Hint: what if you turn the LED on and off really quickly?* (TODO: is this hint too strong?)
3.1. Use this to get other colours from the RGB LED.


## Chapter 4 -- States, Classes, Dictionaries
## Chapter 5 -- Grove, PWM, Servos

### Grove

#### Part 1 - Switches

For these tasks you will need:
- Grove button sensor
- magnet and Grove hall effect (magnet) sensor

1. Test that the button module works -- write a program to display a different image on the screen depending on whether a button module is currently pressed or not.
2. Try our your code from the [Dead Man's Switch](https://groklearning.com/learn/microbit-crash-course/6/2/) problem in Module 6 from the Grok Crash Course.
3. Use a button module, and write a program to count the number of times the button has been pressed (showing the count on the display using `display.show`).
   1. This is a bit tricky because there is no `was_pressed` for pins. You'll need to detect the **pin changing state** rather than just looking at whether it's currently pressed.
4. Make an automatic door opener that detects motion and opens the door. Show this by animating a door opening on the display of the screen.
5. Add a "lock" mode to your automatic door by adding a button module that disables the sensor if it has been pressed, press again to unlock.
6. Add a "card reader" that uses a magnet as a key-card to open the door even when locked.

!!Show your work to a tutor before continuing!!

#### Optional extension tasks
Most of these sensors behave a lot like the micro:bit buttons (especially the button module!). It'd be great if we could use the `is_pressed()` and `was_pressed()` functions like we can on the built-in buttons.

1. Write a class for each of the sensors that works like the `MicroBitButton` class. It should provide both an `is_pressed()` and a `was_pressed()` method (or equivalently, `is/was_motion()` and `is/was_magnet()`).
   1. *Hint*: you'll need to add another method that your program will need to call at the start of every loop that will actually read the state of the pin.
2. Try out one of the heart rate monitors. These work by sending a pulse for every beat detected (much like the motion sensors, but much shorter pulses). Ask your tutors for advice. Make the micro:bit flash the `Image.HEART` image for every beat and press a button to `display.show` the BPM.


#### Part 2 - Sound

For these tasks you will need:
- Grove sound sensor

This gives us the *volume* of the ambient sound in the room.

1. Write a program so that every time you clap your hands, the next image from a list of micro:bit images. It should start at the beginning of the list once the end is reached.
2. Instead of changing images, write a program to scale the brightness of Image.HEART so that the brightness scales with the sound emitted. It's possible to divide an image by a number to adjust the brightness:
```python
display.show(Image.HEART/1.5)
```
3. Write a program so scale the brightness of each pixel of *anything currently displayed* proportional to the volume detected by the sound sensor. *Hint* you should use `display.get_pixel` to get each pixel value and adjust the brightness by creating an *image string*.
   1. **Bonus**: write a function to turn one of your image strings into an `Image` object, so you can use divides like in your solution to the previous problem.

!!Show your work to a tutor before continuing!!

#### Part 3 - Rotary encoder

**Note**: You will need to *set* pull up resistors for this task at the start of your program

```python
# set the pull up resistors on each pin, in this example 2 & 15
pin2.read_digital()
pin2.set_pull(pin2.PULL_UP)
pin15.read_digital()
pin15.set_pull(pin15.PULL_UP)
```

The rotary encoder works by having 2 signals. The relative phase of the two signals can tell us if the encoder is turning clockwise, or anti-clockwise. Every time the encoder is turned, a pulse is sent, and we can look at the signals to figure out if it's clockwise, or anti-clockwise.

**The clockwise signal looks something like this:**

![Clockwise rotary signals](images/clockwise-rotary.png)

**The anti-clockwise signal looks something like this:**

![Anti-clockwise rotary signals](images/anticlockwise-rotary.png)

Write a program to read from the encoder, and print 0 to 9 on the 5x5 LED on the micro:bit. If the number is greater than 9, it should be set to 0, similarly if it becomes less than 0, it should be set to 9.

!!Show your work to a tutor before continuing!!


### PWM

1. Make an LED pulse on and off by smoothly changing the brightness up and down.
1.1. Try different pulsing patterns (e.g. sinusoidal).
2. Use an RGB LED to experiment with colours.
2.1. Generate a rainbow sequence, smoothly changing through the spectrum.


### Servo motors

1. Use a standard servo to make a boom-gate style barrier that open and closes based on a signal from the micro:bit (e.g. when a button is pressed).
2. TODO more


## Chapter 6 -- Radio, Files, Plotting
## Chapter 7 -- bit:bots, NeoPixels

### bit:bot neopixels

1. Make your bit:bot indicate its left and right side like a boat or aeroplane. Turn on the front LED on the left to red, and the front LED on the right to green.
2. TODO: flashing sequence (white, red, red)?
3. TODO: Animation (forwards/backwards)
4. TODO: Rainbow
 * Hint: Ask your tutors about how to convert a "hue" into an RGB colour.
5. TODO: Gamma correction.
6. TODO: Indicate line following state.



### Ultrasonic distance sensor

1. Try out the example above. How accurate and precise are the measurements?
2. Experiment with some ways to improve the reliability of the sensor:
  * Calibrate the sensor with a ruler and update the tof->cm factor.
  * Try creating a moving average of the sensor readings to reduce noise.


### bit:bot line following

0. **Getting Started**:
    * Put some batteries in the compartment and plug in a micro:bit using the right-angle adaptor. As we have SONAR distance sensors installed on the fronts of these robots, you won't be able to plug them in directly.
    * Ensure that the power LED comes on, and that the micro:bit is powered by the batteries. You may have to write a short program that outputs something on the display to ensure this work, as we don't want to rely on the USB cable for this exercise.
    * Make the robot drive forwards.
1. Speed Control
    * Now that the bit:bot works, let's play around with the motors and speed controls a bit. First let's try making the bit:bot drive in a straight line. Does it work when both motors are set to the same power? Why or why not? Can you find some values that do make it move in a straight line? Write a function that makes the bit:bot drive forward with these speed values, it will be useful later on.
    * Write three functions that make the bit:bot turn 90-degrees clockwise, 90-degrees counter-clockwise and 180-degrees around.
    * Write a program that uses the previous functions you wrote and makes the bit:bot drive forwards for one second, spin around, and drive back to where it started. Did it work as you expected? What about if you upload the same code with no modifications to abother bit:bot.
2. Make your bit:bot detect when it's driven into a "garage" and stop automatically. i.e. the ambient light decreases
3. Make a simple radio-controlled car using the micro:bit radio and two micro:bits. When a button is pressed on the controller, toggle between two modes:
    * Driving forward at 100% speed.
    * Reversing in an arc to the left.
    Play a beep sound when changing modes.
    (This is how cheap radio-controlled car toys in the 90's worked as they only had a very simple radio that allowed for a single button!)
4. Improve the radio control to allow for four modes:
    - drive forwards (both buttons pressed)
    - turn left (left button only)
    - turn right (right button only)
    - stop (no buttons pressed)
5. The bouncing DVD logo is one of the more iconic screensavers of the early 2000s, and recently made a bit of a resurgence (for example: https://youtu.be/m8NAlDOCG6g). Let's try to recreate it with our bit:bots using the functions we wrote before and the line following sensors on our bit:bots.
    * To do this exercise you will need a rectangular area marked out with masking tape on the floor.
    * Before you get started, you can study how the screensaver looks here: https://bouncingdvdlogo.com/
    * **HINT**: You will need to use both of the line sensors to figure out which way your robot needs to turn when it hits an edge.
    * **EXTENSION**: Add colors to your bit:bot using the neopixels.
    * **EXTENSION**: Can you detect a rare corner-hit and play a sound if it happens?
6. Let's combine the radio controller and the light sensors! Make a circular-ish fenced off area for your bit:bot using masking tape. Using the line sensors, modify your radio controlled bit:bot such that it can't be driven out of its area.
    * **HINT**: you might want to make is spin around and move backwards whenever it hits the edge of the pen, otherwise it will just get stuck at the edge.

### Line following

Today's lab focuses on closed-loop control. We're going to work on taking some of the tasks that we did in the previous lab with hard coded values and improve them to use feedback from the micro:bit and bit:bot sensors. Not only does that allow our code to be ported between different bit:bots, which might need different times/powers to move and rotate in the same way, but it will also mean our code runs a bit more reliably than before.

0. **Getting Started**:
    * If you didn't get around to it last lab, get your bit:bot working, make sure that the line following sensors work as you expect (use a small strip of masking tape on the floor).
    * Make sure that you are able to drive straight-ish, and make smooth curves to the left and right.

1. Let's start of with a simple line follower. Follow the bang-bang controller skeleton that's given in this chapter to follow a line on the floor.
    * When the *left* line sensor detects the masking tape, turn to the left.
    * When the *right* line sensor detects the masking tape, turn to the right.
    * When *both* or *none* of the line sensors detect masking tape, go straight.

    How well does this program do at following the line?

    * Change your program to arc to the left and the right, rather than turning sharply. Does this do any better?
        * Is there a situation where this approach will fail?

2. The simple bang-bang implementation, although effective, is not the fastest way we could follow the line. We can improve on this by counting the number of times the line sensor detects the masking tape and using this as an approximation for how far over the line we've gone.

    By doing this, we can make the robot make small corrections at first, and make larger and larger corrections if it comes to a sharp corner.

    * You can use the skeleton provided above to implement this.

3. **More Closed Loop Control**: We can also change the implementations for going straight and turning that we used in the previous lab to use closed loop control. This will allow our code to be far more portable than before.
    1. Using the compass sensor on the micro:bit, make a program that travels straight, adjusting the left and right motor powers whenever the heading changes.
        * *HINT*: The example code for the PI controller may be helpful here
    2. Modify your code so that it is able to drive straight for exactly 1, 2 and 4 seconds.
    3. Write some code to turn 90 degrees clockwise/counterclockwise.
        * *HINT*: You may have to slow down when you approach the correct heading to ensure you don't overshoot. Can you use the difference between the current heading and target heading to select a speed? What sort of control algorithm would this be?
    4. Use this code to drive forwards for 1 second, rotate 180 degrees, and drive forwards for 1 second. Did it do better than before? What about if you upload the same code to another bit:bot with no modifications?

#### Bit:Bot Challenge

Once you've completed the above lab exercises, there are a couple of additional challenges that will require you to combine all the concepts you've covered thus far.

We've set up two (hidden) courses somewhere in the building. Your challenges, should you choose to accept them, are given below...

1. **The Obstacle Course**

    Now that you've got your line following robots working it's time to deploy them in the field. Of course, the real world is never as neat as the lab, so you'll have to make sure your robot can handle a bit of noise.... Your robot will have to handle the following things:

    * angular turns
    * steep curves
    * overlapping lines
    * rough surfaces

    Finally at the end of the course, your bit:bot will drive into a box. Your robot should detect that this has occured using the top-mounted light sensors and stop at the end.

2. **The Time Trial**

    One advantage of moving from a bang-bang controller to a PI style controller is that we spend a lot more time driving forwards. The better our control algorithm, the faster we can go! Unfortunately, as you will soon discover, speed does come at the expense of stability, so your challenge here will be to push your robot to complete our obstacle course as fast as you can.

    Although not as sharp as for challenge 1, the course will still have some steep curves that you will need to handle.


## Chapter 8 -- Filtering, Control
## Chapter 9 -- ICs, Datasheets, Signalling, Drivers
## Chapter 10 -- Pyboard, Quokka
