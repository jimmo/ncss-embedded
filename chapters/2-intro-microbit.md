## Chapter 3 -- micro:bit basics

### Images and sleeping

Let's turn on the display!

```python
from microbit import *

display.show(Image.HAPPY)
```

What's happening here? The first line is to `import` the microbit module, which gives us all the functions we're going to use.

`display.show` is a function that displays an image, `Image.HAPPY`. It looks like a happy face :)

There are a long list of in-built images [on the microbit documentation](https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html).

To show multiple images, we need to `sleep` in between instructions, because the micro:bit runs so fast that the images will flash faster than our eyes can see them if we don't do this.

The parameter of `sleep` is in *milliseconds*, so `sleep(1000)` means *sleep for 1 second*. So someone's life story told in 2 seconds might look like this:

```python
from microbit import *

display.show(Image.HAPPY)
sleep(1000)
display.show(Image.SAD)
sleep(1000)
display.show(Image.SKULL)
```

### Show and scrolling text

We can use the same command to show text:

```python
from microbit import *
display.show('Hi NCSS')
```

But that flashes letters and it's a bit weird. Much better of `scroll` text instead:

```python
from microbit import *
display.scroll('Hello there, this text is scroooooooling')
```

To scroll integers, we need to convert them to a string using the `str` function before scrolling:

```python
from microbit import *
num = 50
display.scroll('The answer is: ' + str(num))
```

We might want to repeatedly scroll text:

```python
from microbit import *
display.scroll('LOLOLOLOLOLOLO', repeat=True)
```

That text will keep repeating, to speed it up we can use the `delay` *key word argument* (called a kwarg).

```python
from microbit import *
display.scroll('LOLOLOLOLOLOLO', delay=50, repeat=True)
```

The `delay` specifies the delay in *milliseconds* between each frame.

Find more info on scrolling text in the [docs](https://microbit-micropython.readthedocs.io/en/latest/display.html?highlight=scroll#microbit.display.scroll). Lots of those options are available in `display.show` too!

### Printing to the console

It's annoying to try and look at a scrolling error message on the LED display.

```python
print('hello')
```

That will print messages to the serial console so you can get an actual output, to do some debugging. In Grok, look at the "Output" tab to view the serial output in the simulator (you can also get a REPL there, too).

### picture here

Printing is the same as `display.scroll` (and in python), where we need to convert to `str` before printing numbers.

```python
answer = 42
print('The answer to live is ' + str(answer))
```

### Using loops

Embedded systems, we generally don't want to stop them to stop. So we really want them to do things *forever*. Let's take a look a program that does this:

```python
from microbit import *

while True:
  display.show(Image.HEART)
  sleep(500)
  display.show(Image.HEART_SMALL)
  sleep(500)
```

The `while` loop is what does this. It comes in the form `while condition:`, why the `condition` evaluates to `True` then the loop repeats. At the beginning of each loop, the `condition` is checked to see if the loop continues.

By typing
```python
while True:
```
this means it will be an *infinite loop*, **don't forget to put in the colon**.

Everything inside the loop should be *indented* (we recommend 2 spaces for each indentation).

### Using the buttons

The `microbit` module gives us `button_a` and `button_b` objects to use the buttons.

To simply see if the button is pressed down right now, use the `is_pressed()` function, as the name would imply.

```python
from microbit import *

while True:
  if button_a.is_pressed():
    display.show(Image.HEART)
  # code keeps executing if
```

Notice the use of the `if` statement. Like the `while` loop, `if` checks if a condition is `True` or `False`.

So if `button_a` is pressed down, the function `button_a.is_pressed()` returns `True`.

We can connect an `if` statement with an `else` statement, and only *one* of them will run.

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
    display.show(Image.GHOST)
  elif button_a.is_pressed():
    display.show(Image.GHOST)
  else:
    display.clear()
```

### was it pressed?

Because the microbit moves so fast, often it's better to use `was_pressed()`.

`was_pressed` means between this time and the last time we checked, was the button pressed? The button needs to be released before `was_pressed` will return `True` again.

So `was_pressed` makes the buttons work a bit more like buttons how we 'expect' them to work.

We can use it in the same way we used `is_pressed`.

```python
if button_a.was_pressed():
  # do the thing
```

### Working with the display

The `display` module does more than just setting pre-built images. We can programmatically do this with the `display.set_pixel` function.

The display works on a grid with (0, 0) at the top left:

![Grid source:microbit docs](https://microbit-micropython.readthedocs.io/en/latest/_images/happy.png)

```python
from microbit import *
display.set_pixel(2, 2, 9)
```

Each pixel has a brightness from `0` to `9`, so the code above sets pixel (2, 2) to full brightness.

### Writing for loops

Some times the images we want don't exist, so we can set the pixel by writing a `for` loop.

```python
from microbit import *

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
display.set_pixel(0, 4, 9)
display.set_pixel(1, 4, 9)
display.set_pixel(2, 4, 9)
display.set_pixel(3, 4, 9)
display.set_pixel(4, 4, 9)
```

that's pretty boring to write. So use a `for` loop instead.
