#!/bin/python3
#https://www.hackerrank.com/challenges/apple-and-orange/problem
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap,o=0,0
    for i in range(m):
        if (apples[i]+a) in range(s,t+1):
            ap+=1
    for i in range(n):        
        if (oranges[i]+b) in range(s,t+1):
            o+=1    
    print(ap)
    print(o)
    return 0

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)