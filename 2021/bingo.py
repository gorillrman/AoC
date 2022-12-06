#! /usr/bin/env python3
# Sean McKenna test scripting (2021)

import pandas as pd

bingos = pd.read_csv(
    "E:\OneDrive\Programmy\Python\AoC\\2021\\bingo_input.txt", header=None, dtype=str
)

print(bingos)
