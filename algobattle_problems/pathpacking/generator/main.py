"""Simple dummy generator for the PathPacking problem, outputting a static instance."""

import json
import pathlib

with pathlib.Path("output/instance.json").open("w+") as output:
    json.dump({"num_vertices": 3, "edges": [[0, 1], [1, 2]]}, output)

with pathlib.Path("output/solution.json").open("w+") as output:
    json.dump({"paths": [[0, 1, 2]]}, output)
