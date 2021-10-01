import time
import random
interval = 0.04
while True:
  num = random.randint(6, 30)
  for i in range(10):
    for i in range(num):
      print(" "*i + "HELLO WORLD!")
      time.sleep(interval)
    for i in range(num):
      print(" "*(num-i) + "HELLO WORLD! ")
      time.sleep(interval)
