import time
import concurrent.futures
import random
from UserInput import DiceValues

values = DiceValues()
quantity = values[0]
diceType = values[1]

start = time.perf_counter()


def GenRand(seconds):
    num = random.randint(1, diceType)
    time.sleep(seconds)
    return num

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(GenRand, 1) for _ in range(quantity)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f'finished in {round(finish - start, 2)} second(s) ')


