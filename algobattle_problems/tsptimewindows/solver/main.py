"""Simple dummy solver for the Tsptimewindows problem, outputting a static solution."""

import json
import pathlib

with pathlib.Path("output/solution.json").open("w") as output:
    json.dump({"tour": [0, 3, 4, 1, 2]}, output)
