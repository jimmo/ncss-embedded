# Chapter 6 -- Radio, Files, Plotting

## Radio

The micro:bit includes a Bluetooth Low Energy (BLE) radio. From MicroPython, we don't have access to most of the BLE functionality, but we can use the radio to send and receive small *packets* of data.

If you've listened to an AM or FM radio station, you'll hear them referred to by their frequency. For example, Triple J in Sydney is 105.7 MHz. Similar for television stations, mobile phones, etc. By broadcasting at different frequencies, they can transmit at the same time without interference. micro:bits use an area of the spectrum at 2.4GHz called the ISM band, and they can use 84 different channels all at slightly different frequencies.

To use the radio from Python, we import the `radio` module, select a channel, and turn it on.

```python
import radio

radio.config(channel=22)
radio.on()
```

To send a message, we use the `send` function:

```python
while True:
  if button_a.was_pressed():
    radio.send('Is there anybody out there?')
```

On a different micro:bit we can receive a message using the `receive` function.

```python
while True:
  message = radio.receive()
  if message:
    display.show(message)
```

The way receive works is a bit like a letter box. Once the radio is turned on, all messages on the configured channel will be received and stored in the "letter box". When we call `receive`, it checks to see if there's any messages waiting for us. If there isn't it returns `None`, which is why we need the if statement above.

See the micro:bit MicroPython documentation for more information at [https://microbit-micropython.readthedocs.io/en/latest/radio.html](https://microbit-micropython.readthedocs.io/en/latest/radio.html).

### Groups and addresses

Because your micro:bits aren't transmitting all the time, it's possible to have multiple micro:bits sharing the same frequency. You can use the `address` and `group` optional arguments to `radio.config()` to filter out messages that don't match the same address and group.

### Unique IDs

If you need a unique ID to identify your micro:bit, you can use:

```python
import machine
my_id = machine.unique_id()
```

*Note: This was added since the Grok micro:bit crash course was written.*

## Files

The micro:bit contains a small *filesystem* which allows you to store data even when the micro:bit is switched off. You can use the regular Python functions to access it.

For example to write the string `"hello"` to a file named `data.txt`, you can write:

```python
# Open the file for writing.
f = open('data.txt', 'w')
f.write('hello')
f.close()
```

Then to read it back later:

```python
# Open the file for reading.
f = open('data.txt', 'r')
data = f.read()
f.close()
```

You might want to use this to save program data, or to record more sensor data than will fit into memory.

## Plotting with Mu

Mu has a super handy new *plotter* feature that helps you plan for world domination. No...the other type of plotting... making a graph of something.

When working with sensors, especially analog ones, sometimes it can be extremely useful to visualise what the sensor data looks like. This helps us find patterns and understand how the sensor behaves.

To use this feature, your program should print *tuples* of data out to the console, using the `print` function.

```python
while True:
  # Read data from sensor.
  x = accelerometer.get_x()
  y = accelerometer.get_y()
  z = accelerometer.get_z()
  # Make a tuple.
  record = (x, y, z,)
  # Print to the console.
  print(record)
  # Need a short sleep to avoid sending too much data.
  sleep(50)
```

You can read more about this feature here: [https://codewith.mu/en/tutorials/1.0/plotter](https://codewith.mu/en/tutorials/1.0/plotter).
