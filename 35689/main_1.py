#!/usr/bin/python3

import sys
sys.path.insert(0, '/root')

canUnlockAll = __import__('2-lockboxes').canUnlockAll

if __name__ == "__main__":
  boxes = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
  print(canUnlockAll(boxes))
