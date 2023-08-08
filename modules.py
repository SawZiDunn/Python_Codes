import math

import random

from pathlib import Path

class Dice:
    def roll(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        return a, b


members = ["a", "b", "c", "d"]
x = math.floor(random.randint(25, 26))
y = random.choice(members)

path = Path()
for file in path.glob("*.py"):
    print(file)

