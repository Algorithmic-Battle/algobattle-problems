"""Simple dummy generator for the Pairsum problem, outputting a trivial instance."""

import json
import pathlib

with pathlib.Path("/input/max_size.txt").open("r") as input:
    n = int(input.readline())

with pathlib.Path("/output/instance.json").open("w+") as output:
    json.dump({"numbers": [1] * n}, output)

with pathlib.Path("/output/solution.json").open("w+") as output:
    json.dump({"indices": [0, 1, 2, 3]}, output)
