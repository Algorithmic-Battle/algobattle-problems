"""Simple dummy solver for the Pairsum} problem, outputting a static solution."""

import json
import pathlib

with pathlib.Path("/output/solution.json").open("w+") as output:
    json.dump({"indices": [0, 1, 2, 3]}, output)
