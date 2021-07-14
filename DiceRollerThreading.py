import time
import threading
import random
from UserInput import DiceValues

values = DiceValues()
quantity = values[0]
diceType = values[1]
start = time.perf_counter()
numArray = []


def GenRand(seconds):
    num = random.randint(1, diceType)
    time.sleep(seconds)
    numArray.append(num)


threads = []

for _ in range(quantity):
    t = threading.Thread(target=GenRand, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

for i in range(0, len(numArray)):
    print(numArray[i], end=" ")

print(f'\nthe total is {sum(numArray)}\n')
finish = time.perf_counter()

print(f'finished rolling in {round(finish - start, 2)} second(s) ')
