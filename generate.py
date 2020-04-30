#!/usr/bin/env python3

from pathlib import Path
from hashlib import md5
import json

colours = [
    0x111111, # Black
    0xcc4c4c, # Red
    0x57A64E, # Green
    0x7f664c, # Brown
    0x3366cc, # Blue
    0xb266e5, # Purple
    0x4c99b2, # Cyan
    0x999999, # Light_grey
    0x4c4c4c, # Grey
    0xf2b2cc, # Pink
    0x7fcc19, # Lime
    0xdede6c, # Yellow
    0x99b2f2, # Light_blue
    0xe57fd8, # Magenta
    0xf2b233, # Orange
    0xf0f0f0, # White
]

pool = []
for author_dir in Path("data/computercraft/lua/treasure").iterdir():
    if author_dir.name == "deprecated" or not author_dir.is_dir():
        continue

    for program_dir in author_dir.iterdir():
        author, program = program_dir.parts[-2:]
        colour = colours[int(md5(bytes(author + "/" + program, "utf-8")).hexdigest()[0], 16)]
        pool.append({
            "type": "minecraft:item",
            "name": "computercraft:treasure_disk",
            "functions": [{
                "function": "minecraft:set_nbt",
                "tag": json.dumps({
                    "Title": "{} by {}".format(program, author),
                    "SubPath": "{}/{}".format(author, program),
                    "Colour": colour,
                })
            }],
        })

with open("data/computercraft/loot_tables/treasure_disk.json", "w") as h:
    json.dump({
        "pools": [{
            "name": "main",
            "rolls": 1,
            "entries": pool,
        }]
    }, h, indent = 4)
