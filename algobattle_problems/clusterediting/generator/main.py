"""Simple dummy generator for the ClusterEditing problem, outputting a static instance."""

import json
import pathlib

with pathlib.Path("output/instance.json").open("w+") as output:
    json.dump({"num_vertices": 4, "edges": [[0, 1], [1, 2], [0, 3]]}, output)

with pathlib.Path("output/solution.json").open("w+") as output:
    json.dump({"add": [[0, 2]], "delete": [[0, 3]]}, output)
