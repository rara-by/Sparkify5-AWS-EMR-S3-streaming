#! /usr/bin/python3
import json
import sys

for dicto in sys.stdin:
    obj = json.loads(dicto)
    if obj['artist']:
        print('{}\t{}'.format(obj['artist'], 1))
