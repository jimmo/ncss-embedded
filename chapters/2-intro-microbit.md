## Chapter 2 -- micro:bit basics

The micro:bit is a small, handheld, embedded microcontroller, which we will be using for the duration of the camp. Apart from being very friendly, it has a huge number of peripherals that we can use: a compass, an accelerometer, a thermometer, a radio for chatting between 2 micro:bits, two buttons and a 5x5 display. More importantly, it can run Python! The aim of the next few days will be to get up to speed on the various features of the micro:bit. 

To get started we're going to be working through the micro:bit crash course on the grok platform. For those of you who have done the challenge, this will be a very familiar interface, with the key difference that our code will now be running on an emulated micro:bit in the browser.

The crash course will go through everything you need to play around with the micro:bit. In addition to the course, we give a brief description of the peripherals of the micro:bit below, which you can use as a reference if you ever get stuck.

### Getting Started

If you're using the microbit emulator on Grok, you don't need anything more to get started.

If you're playing around with a real micro:bit, you'll need a couple of other things to get going. When you plug the micro:bit in to your computer, it will show up as a drive connected to your computer. The micro:bit expects you to copy a `.hex` file which contains the compiled program that you want to run.

There's a couple of ways to get this file. If you are using the Grok interface to write your programs, you can hit the "Download" button in the top right corner of the editor to download the hex file that corresponds to your written program. Then, copy and paste that file onto the micro:bit drive that appears.
![GrokInterface](images/GrokDownload.png)

Alternatively, you can use the `Mu` editor -  a simple editor for python that interfaces directly with the micro:bit, and is able to upload code directly to the micro:bit. During the micro:bit labs, this will be the main editor we use. The editor can be downloaded from https://codewith.mu/en/. By pressing the `Flash` button in the editor, we can upload the code to the micro:bit. Once the upload is completed, the micro:bit will automatically reset and start running your new program.
![MuInterface](images/mu_buttons.png)

**Note**: If this set of buttons doesn't appear in your copy of `Mu`, you may not be running in the "micro:bit" mode. You can change the target in `Mu` by pressing the `Mode` button in the top left corner of the editor.

### Using the micro:bit

Plug your micro:bit into the computer with a USB cable, open up `Mu` and let's start coding!

#### Our first program (the micro:bit display and sleep)

Let's turn on the display!

```python
from microbit import *

#show an image on the 5 x 5 display
display.show(Image.HAPPY)
```

What's happening here? The first line is to `import` the microbit module, which gives us all the functions we're going to use.

`display.show` is a function that displays an image, `Image.HAPPY`. It looks like a happy face :)

There are a long list of in-built images [on the microbit documentation](https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html).

To show multiple images, we need to `sleep` in between instructions, because the micro:bit runs so fast that the images will flash faster than our eyes can see them if we don't do this.

The parameter of `sleep` is in *milliseconds*, so `sleep(1000)` means *sleep for 1 second*. So someone's life story told in 2 seconds might look like this:

```python
from microbit import *

#show an image on the 5 x 5 display
display.show(Image.HAPPY)
#wait for a number of milliseconds
sleep(1000)
display.show(Image.SAD)
sleep(1000)
display.show(Image.SKULL)
```

#### Show and scrolling text

We can use the same command to show text:

```python
from microbit import *

#show text on the 5 x 5 display one letter at a time
display.show('Hi NCSS')
```

But that flashes letters and it's a bit weird. Much better of `scroll` text instead:

```python
from microbit import *

#scroll text on the 5 x 5 display 
display.scroll('Hello there, this text is scroooooooling')
```

To scroll integers, we need to convert them to a string using the `str` function before scrolling:

```python
from microbit import *

num = 50
#scrolling text with joining
display.scroll('The answer is: ' + str(num))
```

We might want to repeatedly scroll text:

```python
from microbit import *

#scrolling text with repetition
display.scroll('LOLOLOLOLOLOLO', loop=True)
```

That text will keep repeating, to speed it up we can use the `delay` *key word argument* (called a kwarg).

```python
from microbit import *

#scrolling text with repetition and change of speed
display.scroll('LOLOLOLOLOLOLO', delay=50, loop=True)
```

The `delay` specifies the delay in *milliseconds* between each frame.

Find more info on scrolling text in the [docs](https://microbit-micropython.readthedocs.io/en/latest/display.html?highlight=scroll#microbit.display.scroll). Lots of those options are available in `display.show` too!

#### The REPL

In addition to uploading scripts to the micro:bit and running them, we can also interactively run single lines of python code on the micro:bit. The easiest way to access the REPL on the micro:bit is using the `Mu` editor, where we can press the `REPL` button in the menu bar. This will stop the currently running program and bring up a prompt, into which you can type Python expressions.

For example, try bringing up the `REPL` and type the following lines:

```pycon
>>> display.show(Image.HAPPY)
```

Opening the `REPL` causes whatever code is uploading to stop, however we can also restart our running code, either by pressing the "reset" button on the micro:bit, or pressing `<Ctrl-D>` in the `REPL` window.

Note, you won't be able to upload code to the micro:bit while the `REPL` window is open. If you want to upload a new program, you will have to close the `REPL` window first.

#### Printing to the console

It's annoying to try and look at a scrolling error message on the LED display. Instead of printing to the display, we can output straight to the `REPL` window. Upload the following code to your micro:bit.

```python
#displaying to the console 
print('Hello, World!')
```

That will print messages to the serial console so you can get an actual output, to do some debugging. In Grok, look at the "Output" tab to view the serial output in the simulator. In `Mu` to see what the output looks like, you can open the `REPL` window, and either hit the "reset" button on your micro:bit or press `<Ctrl-D>` in the `REPL` window to start your program going again. Your message will show up in the window:

![REPL_Print](images/REPL_print.PNG)

Printing is the same as `display.scroll` (and in python), where we need to convert to `str` before printing numbers.

```python
#displaying joined text to the console  
answer = 42
print('The answer to life the universe and everything is ' + str(answer))
```

#### Using loops

Embedded systems, we generally don't want them to stop. So we really want them to do things *forever*. Let's take a look a program that does this:

```python
from microbit import *

#first while loop
while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
```

The `while` loop is what does this. It comes in the form `while <condition>:`, when the `condition` evaluates to `True` then the loop repeats. At the beginning of each loop, the `condition` is checked to see if the loop continues. The code that we want to run is indented to indicate that it is all part of the `while` loop. Unindented code will not be run as part of the loop. For example, in the following code:

```python
while True:
    print("Hello, World!")
    sleep(500)
print("Goodnight, Moon.")
```

The phrase "Hello, World!" will be printed indefinitely, while "Goodnight, Moon." will never be reached.

In addition, in both the above loops, since `True` is always `True`, the above code will repeat forever. It is an *infinite loop*.

We can also write a loop that will terminate once a certain action has taken place. For example, in the following code:

```python
i = 0
while i < 5:
    print("The number was: " + str(i))
    i += 1
print("Done")
```

the condition `i < 5` is true until i = 5, so this code will print:

```
The number was: 0
The number was: 1
The number was: 2
The number was: 3
The number was: 4
Done
```

#### Buttons and if statements

The `microbit` module gives us `button_a` and `button_b` objects to use the buttons.

To simply see if the button is pressed down right now, use the `is_pressed()` function, as the name would imply.

```python
from microbit import *

# Show a heart while the button is pressed
while True:
    display.clear()
    if button_a.is_pressed():
        display.show(Image.HEART)
    sleep(1000)
```

Notice the use of the `if` statement. Like the `while` loop, the `if` statement will check whether the condition is true, and run the indented code if it is. In the above code, `display.show(Image.HEART)` is run if `button_a.is_pressed()` is true. Since `sleep(1000)` isn't indented relative to the `if` statement, it will always be run.

We can connect an `if` statement with an `else` statement, which will run if the condition evaluates to 

```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HEART)
    else:
        display.show(Image.GHOST)
```

The `elif` statement lets us add more options!

```python
from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.HEART)
    elif button_a.is_pressed():
        display.show('A')
    elif button_b.is_pressed():
        display.show('B')
    else:
        display.clear()
```

#### Was it pressed?

While the `is_pressed()` function will tell us whether a button is currently being pressed, often what we want to do is check whether a button was pressed at some point in the past. For this purpose we have the `was_pressed()` function

The `was_pressed()` checks: between this time and the last time we checked, was the button pressed? One thing to remember: the `was_pressed()` function will return `True` ONCE for a button press. If we run it again without releasing the button, it will subsequently return `False`.

For example, we can write a simple counter like so:

```python
count = 0
while True:
    # Show the current count, and increment it
    display.show(count)
    count += 1
    # If button a was pressed at some point, reset the count
    if button_a.was_pressed():
        count = 0
    # Wait 1 second before continuing
    sleep(1000)
```

If we were to replace `was_pressed` with `is_pressed`, we wouldn't be able to detect any button presses that occured during the sleep. In other words, we would have a pretty rubbish reset button....

#### Working with the display

The `display` module does more than just setting pre-built images. We can programmatically do this with the `display.set_pixel` function.

The display works on a grid with (0, 0) at the top left:

![Grid source:microbit docs](https://microbit-micropython.readthedocs.io/en/latest/_images/happy.png)

```python
from microbit import *

#set_pixel(x,y,amount)  3rd light across and 4th down because we count from 0
display.set_pixel(2, 3, 9)
```

Each pixel has a brightness from `0` to `9`, so the code above sets pixel (2, 3) to full brightness.

#### Writing for loops

Some times the images we want don't exist, so we can set the pixel by writing a `for` loop.

```python
from microbit import *

#faster than writing out each set_pixel
while True:
  if button_a.was_pressed():
    for x in range(5):
      display.set_pixel(x, 4, 9)
  elif button_b.was_pressed():
    display.clear()
```
The for loop `for x in range(5):` will loop 5 times, where `x` is a variable that goes from 0 through to 4.

The equivalent code is:

```python
from microbit import *

display.set_pixel(0, 4, 9)
display.set_pixel(1, 4, 9)
display.set_pixel(2, 4, 9)
display.set_pixel(3, 4, 9)
display.set_pixel(4, 4, 9)
```

that's pretty boring to write. So use a `for` loop instead.

#### Debugging Your Code

Apart from being a great way to quickly test out the functionality of the micro:bit, the `REPL` also allows you to find errors in your code. For example, let's upload this buggy code to our micro:bit.

```python
from microbit import *

for i in range(10):
    display.show(i)
    sleep(1000)
display.show(done)
```

This above code has an error in it, we've forgotten to put quotes around the string `done`. As a result it will crash once it finishes counting to `10`. The micro:bit will scroll the error message across the display, however this is usually slow and difficult to read. 

We can get the same information by opening the `REPL` and restarting our program, either by pressing the "reset" button on the micro:bit, or by pressing `<Ctrl-D>` in the `REPL` window. Once we run into the error, the full error message will be output to the console.

![REPL_Error](images/REPL_Error.PNG)
