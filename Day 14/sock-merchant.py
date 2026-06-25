import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    color_count = {}
    
    for sock in ar:
        color_count[sock] = color_count.get(sock, 0) + 1
    
    for count in color_count.values():
        pairs += count // 2

    return pairs    
    
if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))
    result = sockMerchant(n, ar)
    print(result)
