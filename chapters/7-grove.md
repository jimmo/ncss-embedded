## Chapter 6 -- Grove

Grove is just a plug and socket to plug in stuff (called modules) like sensors or buttons!

They have 4 pins:
1. Signal
2. Signal
3. Power
4. Ground

The important thing to remember is **P3** is *always* power and **P4** is *always* ground. Many modules might only use pin 1, the pins that are used should be marked on the module. Here is the markings on the Grove Button:

![Grove button](images/grove-button.jpg)

Pin 1 is the `SIG`, so that is the pin that sends the button signal on. Pin 2 in `NC` which stands for *not connected*. `VCC` means *power*, and `GND` is *ground*.

We have made micro:bit adapters for NCSS, which have 4 grove connectors and a speaker.

![Grove adapter](images/grove-adapter.png)

The pin connections are:

- 0 and 13
- 1 and 14
- 2 and 15
- 19 and 20

`pin0` is also the speaker, some adapters do not have a speaker attached (you can't use both).

## Summary Table 
| Sensor | Description |
| --- | --- |
| Infrared Reflective Sensor | Senses proximity and colour |
| PIR Motion Sensor | Detects movement |
| Multi Colour Flash LED | Flashes between colours |
| LED Buttons | Buttons available in red, yellow and blue |
| Button | Push button |
| Circular LED | 24 programmable LEDS |

## Grove components 

### Infrared reflective sensor
This is a proximity and colour sensor. In other words, it can detect the presence of close by objects and distinguish the difference between light and dark colored objects. Meaning you could get the robot to avoid crashes by detecting the walls first!

![Grove Infrared](images/grove-infrared.jpg)

### PIR motion sensor (passive infrared sensor)
Movement from humans, animals and other moving objects can be detected using the PIR motion sensor. 

![Grove PIR](images/grove-PIR.jpg)

### Multi colour flash LED (party LED)
Just like a disco! Like a "party LED", it quickly flashes between bright colours. 

![Grove multi LED](images/grove-multi-LED.jpg)

### LED buttons (red, yellow, blue)

![Grove LED button](images/grove-LED-button.jpg)

### Button

![Grove button](images/grove-button.jpg)

### Circular LED

![Grove circular LED](images/grove-circular-LED.jpg)

### Hall sensor (magnet sensor)
Used to measure the magnitude of a magnetic field. 

![Grove hall](images/grove-hall.jpg)

### Magnetic switch
Good for measuring proximity, the magnetic switch turns on or off when a magnetic field is detected nearby. 

![Grove magnet](images/grove-magnet.jpg)

### Loudness and sound sensor
The loudness and sound sensors are very similar, in that they both contain microphones, have an analogue output and recognize the presence of sound. Compared to the sound sensor, the loudness sensor is slightly more sensitive. 

![Grove loudness](images/grove-loudness.jpg)

![Grove sound](images/grove-sound.jpg)

### Encoder
Whenever you need a rotating knob, for example as a volume changer, then the encoder is for you! It encodes the rotational movement and outputs it as an electronic pulse.

![Grove encoder](images/grove-encoder.jpg)

### Tilt switch 
Tilting the switch different directions causes the sensor to give output as either True or False.

![Grove tilt](images/grove-tilt.jpg)

### Thumb joystick

![Grove joystick](images/grove-joystick.jpg)

### Servos
Connecting other components to servos allows them to be moved and rotated,

![servo](images/servo.jpg)

## Lab work

### Part 1 - Switches

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

## !!Show your work to a tutor before continuing!!

### Optional extension tasks
Most of these sensors behave a lot like the micro:bit buttons (especially the button module!). It'd be great if we could use the `is_pressed()` and `was_pressed()` functions like we can on the built-in buttons.

1. Write a class for each of the sensors that works like the `MicroBitButton` class. It should provide both an `is_pressed()` and a `was_pressed()` method (or equivalently, `is/was_motion()` and `is/was_magnet()`).
   1. *Hint*: you'll need to add another method that your program will need to call at the start of every loop that will actually read the state of the pin.
2. Try out one of the heart rate monitors. These work by sending a pulse for every beat detected (much like the motion sensors, but much shorter pulses). Ask your tutors for advice. Make the micro:bit flash the `Image.HEART` image for every beat and press a button to `display.show` the BPM.


### Part 2 - Sound

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

## !!Show your work to a tutor before continuing!!

### Part 3 - Rotary encoder

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

## !!Show your work to a tutor before continuing!!
