## Chapter 8 - Functions

So far we've been using lots of functions in Python like `sleep` or `print`. These functions are *defined* by someone else, and we can just call that function to use it.

But you can also write your own functions just like these ones!

Say we just wanted to show the `HAPPY` image, sleep for 1 second, the clear the display.

```python
from microbit import *
def happy():
  display.show(Image.HAPPY)
  sleep(1000)
  display.clear()

happy() # call the function
```

The `def` keyword *defines* the function `happy`, and calling the function by using the name and parentheses (in this case `happy()`), runs the lines of code inside the function.

It's possible to send information into a function, via a *parameter* or *argument* (sometimes we abbreviate this and call it an **arg**). Let's look at an example:

```python
from microbit import *
def happy(ms):
  display.show(Image.HAPPY)
  sleep(ms)
  display.clear()

happy(300) # call the function, sleep for 300 ms
happy(500) # call it again, sleep for 500 ms this time
```

Here we can change the value that is sent into the function and it will use that value inside it.

We can also get information back from functions by using the `return` statement

```python
from microbit import *

# Conversion functions for C->F and F->C
def celcius_to_fahrenheit(c):
  return c * 9 / 5 + 32

def fahrenheit_to_celcius(f):
  return (f - 32) * 5 / 9

# Shows the current temperature in C and F
def update_display():
  c = temperature()
  f = celcius_to_fahrenheit(c)
  display.scroll(str(c) + 'c ' + str(f) + 'f')

# Update the display once per second
while True:
  update_display()
  sleep(1000)
```

Functions can return multiple values, the `temp` function below returns *two* values:

```python
# using functions from above
def celcius_to_fahrenheit(c):
  return c * 9 / 5 + 32

def temp():
  c = temperature()
  f = celcius_to_fahrenheit(c)
  return c, f

c, f = temp()
display.scroll(str(c) + 'c ' + str(f) + 'f')
```

to get back multiple value, we can *unpack* the values by using the comma (,) in between each one. You can return more than two values, to add more, just add more commas.
