rom microbit import *

INTERVAL = 100

a_time = 0
b_time = 0

a = 0
b = 0
ab = 0

def show():

while True:
  if button_a.was_pressed():
    if a_time > 0:
      a += 1
      print((a, b, ab,))
    a_time = running_time()
  if button_b.was_pressed():
    if b_time > 0:
      b += 1
      print((a, b, ab,))
    b_time = running_time()
  if a_time > 0 and b_time > 0 and a_time + INTERVAL >= running_time() and b_time + INTERVAL >= running_time() and button_a.is_pressed() and button_b.is_pressed():
        ab += 1
        a_time = 0
        b_time = 0
        print((a, b, ab,))
  if a_time > 0 and a_time + INTERVAL < running_time():
    a += 1
    a_time = 0
    print((a, b, ab,))
  if b_time > 0 and b_time + INTERVAL < running_time():
    b += 1
    b_time = 0
    print((a, b, ab,))
