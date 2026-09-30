"""Simple dummy solver for the ClusterEditing problem, outputting a static solution."""

import json
import pathlib

with pathlib.Path("output/solution.json").open("w") as output:
    json.dump({"add": [[1, 3]], "delete": [[1, 2]]}, output)
