#!/usr/bin/python3
"""
This method determines if all boxes can be opened
returns True on success
"""

def canUnlockAll(boxes):
    """Check if the boxes can be unlocked"""
    for key in range(1, len(boxes) - 1):
        control = False
        for index in range(len(boxes)):
            control = (key in boxes[index] and key != index)
            if control:
                break
        if control is False:
            return control
    return True
