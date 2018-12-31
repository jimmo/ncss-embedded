## Servo motors

Last chapter we looked at Pulse Width Modulation (PWM). It's very useful for making an approximation of an analog output from a digital system (such as LED brightness or motor speed control). Another really common usage of PWM is for *servo motors*.

First, some background about motors:

### Regular motors

A motor is a device that uses an electromagnet to rotate when a voltage is applied. They come in two main variants:
 * Direct current (DC). A constant voltage is applied to the terminals, and the motor will spin continuously at a speed determined by the voltage (and PWM).
 * Alternating current (AC). A sinusoidal voltage (or voltages for multi-phase motors) is applied to the terminals and the motor's frequency is related to the frequency of the waveform. This is commonly used for large motors, especially powered by mains power (which is already AC). You can also generate the AC waveform using an *inverter*.

A motors speed is determined by the voltage, and the torque by the amount of current that the motor is able to draw from the power supply. *As a microcontroller can typically only supply a very small amount of current, you cannot drive a regular motor directly from a microcontroller pin.* It's also common to drive a motor with a different voltage from the microcontroller.

To drive a motor from a microcontroller, you need a circuit that can switch on or off the motors power supply based on input from the microcontroller. This can be done with a transistor, which acts as an *amplifier* -- allowing a small current & voltage from the microcontroller to control a large current & voltage in the motor.

In order to make the motor spin in both directions, you need four transistors, in an arrangement called an H-bridge.

#### TODO: h-bridge diagram.

### Continuous rotation servo motors

This is a type of servo motor that packages an H-bridge and a gearbox into a self-contained unit. The PWM input is used to set the motors speed and direction.

### Standard servos (angle)

This is the more common type of servo, where the PWM input is used to set the motor's angle. They work by automatically turning the motor forwards or backwards until the angle reaches the desired angle.

The way they work internally is they contain a *potentiometer*, connected to the output. This is a device that changes resistance depending on how far it has been rotated. The servo contains a small circuit that measures the resistance of the potetiometer, and turns on the motor until it sees the resistance increase or decrease to match the desired angle.

#### TODO: diagram

### Controlling a servo motor

Servo motors three connectors:
* Power
* Ground
* Signal (PWM)

Servo motors are designed to take a PWM signal, and typically they care only about the pulse length.

#### Continuous rotation

* 0.6ms full speed reverse
* 1.05ms half speed reverse
* 1.5ms stopped
* 1.95ms half speed forward
* 2.4ms full speed forward

The following example sets the motor speed and direction based on a value from `-1` to `1`.

```python
def set_speed(pin, speed):
  pin.set_analog_period(20)
  pulse_length_ms = 1.5 + 0.9 * speed
  duty_cycle = pulse_length_ms / 20
  pin.write_analog(round(1023 * duty_cycle))
```

#### Standard

* 0.6ms -90&deg;
* 1.05ms -45&deg;
* 1.5ms 0&deg;
* 1.95ms 45&deg;
* 2.4ms 90&deg;

The following example sets the servo angle base on a value from `-90` to `90`.

```python
def set_angle(pin, angle):
  pin.set_analog_period(20)
  pulse_length_ms = 1.5 + 0.9 * angle / 90
  duty_cycle = pulse_length_ms / 20
  pin.write_analog(round(1023 * duty_cycle))
```

### Extra: Stepper motors

Servo motors have two limitations:

* Their angle is not very precise due to the potetiometer and the difficulty in reading the PWM pulse length. It's typically fine for steering a remote controlled car, but not for controlling the head of a laser cutter or an industrial robot.
* They only operate over a fixed range (typically 180 degrees), because potentiometers have a fixed range of movement.

There exist types of servo motors that avoid both of these problem by using different types of sensors to measure the angle (for example by detecting a magnetic field from a magnet attached to the shaft, or measuring the angle optically using a rotating disc). The ClearPath motors from Teknic are a good example.

Another option is to use a *stepper motor* which is a type of AC motor, where by generating specific waveforms you can make the motor precisely turn in discrete movements over a very small angle. These typically need a *stepper motor driver* circuit to operate.
