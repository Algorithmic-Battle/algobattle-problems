"""Simple dummy generator for the Hikers problem, outputting a static instance."""

import json
import pathlib

with pathlib.Path("output/instance.json").open("w+") as output:
    json.dump({"hikers": [[1, 3], [10, 12], [1, 1], [2, 5], [3, 3]]}, output)

with pathlib.Path("output/solution.json").open("w+") as output:
    json.dump({"assignments": {0: 1, 3: 1, 4: 1, 2: 2}}, output)
