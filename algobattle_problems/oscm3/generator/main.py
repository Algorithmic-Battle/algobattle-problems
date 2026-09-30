"""Simple dummy generator for the BiClique problem, outputting trivial instances."""

import json
from pathlib import Path

size = int(Path("input/max_size.txt").read_text())

with Path("output/instance.json").open("w+") as output:
    json.dump({"neighbors": {i: set() for i in range(size)}}, output)

with Path("output/solution.json").open("w+") as output:
    json.dump({"vertex_order": list(range(size))}, output)
