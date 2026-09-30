"""Simple dummy generator for the DomSet problem, outputting a static instance."""

import json
import pathlib

with pathlib.Path("output/instance.json").open("w+") as output:
    json.dump({"num_vertices": 2, "edges": [[0, 1]]}, output)

with pathlib.Path("output/solution.json").open("w+") as output:
    json.dump({"domset": [0]}, output)
