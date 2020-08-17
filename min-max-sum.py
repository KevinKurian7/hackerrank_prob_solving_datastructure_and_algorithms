#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/mini-max-sum/problem
#Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sarr=list()
    k=0
    for i in range(5):
        sum=0
      
        for j in range(5):
            if k==j:
                continue
            else:
                sum=sum+arr[j]
        sarr.append(sum)
        k=k+1        
         
    print(min(sarr),max(sarr))        


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
