#!/bin/python3
#https://www.hackerrank.com/challenges/camelcase/problem
import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    c=0
    for i in range(len(s)):
        if s[i].isupper():
            c=c+1
    return (c+1)        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
