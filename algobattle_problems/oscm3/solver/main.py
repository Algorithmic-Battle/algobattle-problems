"""Simple dummy solver for the OSCM3 problem, outputting trivial solutions."""

import json
import pathlib

with pathlib.Path("input/info.json").open("r") as infofile:
    info = json.load(infofile)
    size = int(info["max_size"])

with pathlib.Path("output/solution.json").open("w") as output:
    json.dump({"vertex_order": list(range(size))}, output)
