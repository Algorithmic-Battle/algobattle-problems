"""Simple dummy solver for the C4subgraphiso problem, outputting a static solution."""

import json
import pathlib

with pathlib.Path("output/solution.json").open("w") as output:
    json.dump({"squares": [[0, 1, 2, 3]]}, output)
