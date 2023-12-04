#!/usr/bin/python3
"""
Module determine if locked boxes in a sequence of size n
can all be opened if each box has a key to another box.
"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened.
    boxes[0] is unlocked

    Args:
      n (list[lists]): depth 1 - list of boxes
                       depth 2 - keys in the box

    Returns:
      whether all boxes can be unlocked
    """
    def openBoxes(keys):
        openedBoxContent = None     # Get the keys (if any) from opened boxes

        # Go through the keys and open their respective box
        for key in keys:
            if key < len(boxes):
                if (openedBoxContent is None):
                    openedBoxContent = []
                openedBoxContent += boxes[key]

        if (openedBoxContent is None):
            return None
        return list(set(openedBoxContent))

    keys = [0]
    usedKeys = []

    while True:
        foundKeys = openBoxes(keys)
        if (foundKeys is None):
            # No boxes could be opened with the keys we have
            break

        # Track already used keys, don't reuse them in next iteration
        usedKeys = list(set(usedKeys + keys))
        keys = [key for key in foundKeys if key not in usedKeys]

    # Check if all the boxes in the sequence/positions have been unlocked
    return sum(usedKeys) == sum(range(0, len(boxes)))
