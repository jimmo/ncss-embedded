# Chapter 8 -- Filtering

Any sensor will inevitably suffer from some noise. Whether it comes from limitations in the sensor, random fluctuations in the electronics and amplifiers, or from imperfectly mounted sensors, it is necessary to design our code in a way that handles the unavoidable noise of our sensors. Unfortunately, when there are random fluctuations in the signal, it can make extracting events out of the signal very difficult. 

Take the below data for example. The true signal is a nice smooth bump, perhaps the intensity of a light source. We want to know when the signal intensity rises above some threshold. From the true signal, we can define a clear threshold above which we can say the event occurred. Unfortunately, once this signal passes through our light sensor, the data is no longer quite so clear. It is impossible in this data to define a simple threshold which will constitute the event occurring. For any line we can draw, the noise causes the measured signal to pass through the threshold multiple times.

Depending on the speed of the event that you would like to detect, one approach to reducing the random fluctuations in our signal is averaging: reading multiple samples of data and taking a weighted sum of those samples. Below we will review the two most common ways that we can perform this averaging.

\begin{figure}
\centering
\includegraphics[width=\linewidth]{images/NoisySignal.png}
\caption{Measuring a signal a) before any noise is added, b) once it has passed through a sensor and c) after it has been filtered.}
\label{fig:noisy_signal} 
\end{figure}

## Windowed Averaging

The simplest approach to averaging a signal is to take $N$ rolling samples and take their average. In the below data, each output point consists of 4 raw data points, with a sliding window of points used to generate the filtered signal.

\begin{figure}
\centering
\includegraphics[width=0.5\linewidth]{images/WindowedAverages.png}
\caption{Windowed averaging with $N=4$}
\label{fig:windowed_averaging} 
\end{figure}

In order to generate the filtered signal, we need to keep a list of $N$ signal points, and keep taking their average to get the next point. For example, if we want to take a windowed average with $N=4$ points using the bit:bot light sensor, we can write code that looks like:

```python
from microbit import *

N = 4
# Generate a list of zeros with N points
input_samples = [0]*N

def get_next_point():
    new_sample = pin2.read_analog()
    # Remove the oldest sample from the sample list
    # the pop(i) method removes the item at index i from the list
    input_samples.pop(0)
    # Add the new sample into the list
    input_samples.append(new_sample)
    # And return the average of the previous N samples
    # We use the builtin sum() function to add all the elements
    # of the list together
    return sum(input_samples)/len(input_samples)

while True:
    print((get_next_point(),))
    sleep(50)
```

The above code will output a filtered signal from the light sensor on the bit:bot in a format that is compatible with the `Mu` plotter. Try play around with the value of $N$ and see how it affects your output signal.

## Exponential Averaging

While windowed averaging gives good results, it can be quite a expensive method of performing filtering in terms of the amount of memory required, as we need to keep a list of the $N$ previous signal points for the algorithm to work. Once $N$ becomes large, this can end up being limiting.

Another method of performing filtering that only requires us to keep track of a single number is exponential averaging (sometimes called exponential smoothing). Here we weight our incoming data by a damping factor ($\alpha$), which takes a value between 0 and 1, such that our smoothed data is made up of a mixture of the previous point($x_p$) and the new sample ($s_n$) according to:

\begin{equation}
x_n = \alpha \times x_p + (1-\alpha) \times s_n
\end{equation}

We can rewrite our `get_next_point` function to use exponential averaging like so:

```python
from microbit import *

ALPHA = 0.75
# Keep track of previous point
prev_point = 0

def get_next_point():
    new_sample = pin2.read_analog()S
    # Calculate the value of the next point, based on the value of the
    # previous point
    new_point = ALPHA*prev_point + (1-ALPHA)*new_sample
    prev_point = new_point
    return new_point

while True:
    print((get_next_point(),))
    sleep(50)
```

Where we use the value of $N$ in windowed averaging to increase the amount of smoothing, in exponential averaging, we use the value of $\alpha$ to control the degree of smoothing. The closer $\alpha$ is to 1, the more smoothed our output data will be (as incoming samples will have less of an effect on the output data).

Given that this method only requires a single variable, you might ask why we don't always use exponential averaging? Unfortunately, since we no longer have a record of old points, it is no longer possible to remove old data from the average, so any spikes will persist for longer in exponential averaging than they would for a windowed average for a similar degree of smoothing.

## The downside of filtering

Although filtering may seem like the solution to all noise problems, if we are not careful, it might end up obscuring the signal that we are trying to measure. Filtering is able to reduce the effect of noise in our signal by reducing the effect of high frequency noise spikes in our signal. In fact, both of the above filters are examples of **low pass filtering**. The effect of a low-frequency signal is made more obvious by removing any high frequency noise that might be hiding the event we want to detect.

This technique only works as long as the signal we are looking for is **slow** relative to the amount of averaging that is applied. If we apply more averaging to our signal, we will only be sensitive to slower events. After a certain point, if we want to detect fast events with high accuracy, we will either need to find a sensor that introduces less noise into the system, or use more advanced techniques for detecting an event. If you are curious to know more, feel free to ask one of us for more information!
