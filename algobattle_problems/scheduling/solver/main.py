"""Simple dummy solver for the Scheduling problem, outputting static solutions."""

import json
import pathlib

with pathlib.Path("output/solution.json").open("w") as output:
    json.dump({"assignments": [4, 1, 5, 3, 2]}, output)
