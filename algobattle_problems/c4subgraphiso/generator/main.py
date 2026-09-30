"""Simple dummy generator for the C4subgraphiso problem, outputting a static instance."""

import json
import pathlib

with pathlib.Path("output/instance.json").open("w+") as output:
    json.dump({"num_vertices": 4, "edges": [[3, 0], [0, 1], [1, 2], [2, 3]]}, output)

with pathlib.Path("output/solution.json").open("w+") as output:
    json.dump({"squares": [[0, 1, 2, 3]]}, output)
