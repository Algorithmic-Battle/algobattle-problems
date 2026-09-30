"""Simple dummy solver for the C4SubGraphIso problem, outputting a static solution."""

import json
import pathlib

with pathlib.Path("output/solution.json").open("w") as output:
    json.dump({"path": [2, 1, 0]}, output)
