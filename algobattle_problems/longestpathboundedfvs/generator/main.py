"""Simple dummy generator for the C4SubGraphIso problem, outputting a static instance."""

import json
import pathlib

with pathlib.Path("output/instance.json").open("w+") as output:
    json.dump({"num_vertices": 3, "edges": [[0, 1], [1, 2], [2, 0]], "fvs": [1]}, output)

with pathlib.Path("output/solution.json").open("w+") as output:
    json.dump({"path": [0, 1, 2]}, output)
