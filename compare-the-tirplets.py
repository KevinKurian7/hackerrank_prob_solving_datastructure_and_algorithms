#!/bin/python3
#https://www.hackerrank.com/challenges/compare-the-triplets/problem
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    j=list()
    pa=0
    pb=0
    for i in range(3):
        
        if a[i]>b[i]:
            pa=pa+1
            pb=pb+0
        elif a[i]==b[i]:
            pa=pa+0
            pb=pb+0
        elif a[i]<b[i]:
            pa=pa+0
            pb=pb+1        
    j=[pa,pb]
    return j        
        
               
   
  

                        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
