#!/usr/bin/env python

import json
from jinja2 import Environment, FileSystemLoader


if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader("./"),
                      trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("feed.template.xml")

    items = ['{0:02d}'.format(i) for i in range(88)]
    with open("feed.xml", "w") as f:
        f.write(template.render(items=items).encode('utf8'))
