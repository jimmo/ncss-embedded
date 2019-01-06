# Chapter 6 -- Radio, Files, Plotting

## Radio

The micro:bit includes a Bluetooth Low Energy (BLE) radio. From MicroPython, we don't have access to most of the BLE functionality, but we can use the radio to send and receive small *packets* of data.

If you've listened to an AM or FM radio station, you'll hear them referred to by their frequency. For example, Triple J in Sydney transmits on the frequency 105.7 MHz. This is the same for television stations, mobile phones, etc. By broadcasting at different frequencies, they can transmit at the same time without interfering with each other. micro:bits use a band of the frequency spectrum between 2.4GHz and 2.5GHz called the ISM band, which is split into 84 different channels.

Much like a radio station, *packets* are broadcast to all nearby micro:bits that are listening on that channel. As a result we don't need to pair micro:bits as long as they are all set to send and receive messages on the same channel.

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

The way receive works is a bit like a letter box. Once the radio is turned on, all messages on the configured channel will be received and stored in the "letter box", that is called a queue. When we call `receive`, it checks to see if there's any messages waiting for us in the queue. If there isn't it returns `None`, which is why we need the if statement above. 

By default, the radio can only store 3 messages in the queue with a maximum message length of 32-bytes, so make sure that your messages aren't too long, and that you regularly clear the incoming message queue. If you try and send a message longer than 32 characters you might find your messages get cut short. Similarly, if the queue is full, any new incoming messages will be dropped silently.

If you need to, you can increase the maximum message length (up to 254 characters) and the size of the queue, at the expense of reducing the amount of memory available on your micro:bit. We can do this by passing the optional `length` and `queue` arguments to the `config()` function:

```python
import radio

max_length = 64
max_messages = 5

radio.config(channel=22, length=max_length, queue=max_messages)
radio.on()
```

See the micro:bit MicroPython documentation for more information at [https://microbit-micropython.readthedocs.io/en/latest/radio.html](https://microbit-micropython.readthedocs.io/en/latest/radio.html).

### Groups and addresses

Because your micro:bits aren't transmitting all the time, it's possible to have multiple micro:bits sharing the same frequency. Since micro:bits communicate by broadcast, You can use the `address` and `group` optional arguments to `radio.config()` to filter out messages that don't match the same address and group. 

Unfortunately, unlike a real address, there isn't a way of sending messages to a specific address without also changing your own address or group. In the same vein, there is no way of retrieving messages that were sent to a different address/group than your micro:bit.

#### Unique IDs

If you need a unique ID to identify your micro:bit, you can use:

```python
import machine
my_id = machine.unique_id()
```

*Note: This was added since the Grok micro:bit crash course was written.*

## Files

The micro:bit contains a small *filesystem* which allows you to store data that persists even when the micro:bit is switched off. You can use the regular Python functions to access it.

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

You might want to use this to save program data, configuration options, or to record sensor data than will fit into memory.

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
