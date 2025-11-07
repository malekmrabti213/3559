#!/usr/bin/python3

import sys
sys.path.insert(0, '/root')

canUnlockAll = __import__('2-lockboxes').canUnlockAll

if __name__ == "__main__":
    boxes = []

    keys = []
    for n in range(1, 1000):
        keys = []
        for m in range(1, 1000):
            keys.append(m)
        boxes.append(keys)

    print(canUnlockAll(boxes))
