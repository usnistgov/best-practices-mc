import random
import numpy as np
from statistics import block
random.seed(43279857)
Vz = random.uniform(0.1, 2)
print("Ideal gas number:", Vz)
number = int(Vz)
numbers = np.zeros(int(1e6))
for trial, _ in enumerate(numbers):
    if random.choice(["ins", "del"]) == "ins":
        if random.random() < Vz/(number + 1):
            number += 1
    else:
        if number > 0 and random.random() < number/Vz:
            number -= 1
    numbers[trial] = number
print("Number:", block(numbers))
