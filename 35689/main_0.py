#!/usr/bin/python3

import sys
sys.path.insert(0, '/root')

canUnlockAll = __import__('2-lockboxes').canUnlockAll

if __name__ == "__main__":
  boxes = [[1], [2], [3], [4], []]
  print(canUnlockAll(boxes))
