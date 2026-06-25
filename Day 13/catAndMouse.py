import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(catA, catB, mouse):
    distA = abs(catA - mouse)
    distB = abs(catB - mouse)
    if distA < distB:
        return "Cat A"
    elif distB < distA:
        return "Cat B"
    else:
        return "Mouse C"
        
if __name__ == '__main__':
    q = int(input()) 
    for _ in range(q):
        catA, catB, mouse = map(int, input().split()) 
        print(catAndMouse(catA, catB, mouse))
