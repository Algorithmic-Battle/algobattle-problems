"""Simple dummy solver for the DomSet problem, outputting a static solution."""

import json
import pathlib

with pathlib.Path("output/solution.json").open("w") as output:
    json.dump({"domset": [1]}, output)
