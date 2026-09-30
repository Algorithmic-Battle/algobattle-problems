"""Simple dummy solver for the PathPacking problem, outputting a static solution."""

import json
import pathlib

with pathlib.Path("output/solution.json").open("w") as output:
    json.dump({"paths": [[2, 1, 0]]}, output)
