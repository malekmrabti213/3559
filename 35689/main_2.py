#!/usr/bin/python3

import sys
sys.path.insert(0, '/root')

canUnlockAll = __import__('2-lockboxes').canUnlockAll

if __name__ == "__main__":
  boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
  print(canUnlockAll(boxes))