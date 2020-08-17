#!/bin/python3
#https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum1=0
    sum2=0
    for i in range(n):
        for j  in range(n):
            if i+j==n-1:
                sum2=sum2+arr[i][j] 
            
    for i in range(n):
        for j  in range(n):
            if i==j:
                sum1=sum1+arr[i][j] 
                    

    # Write your code here
  
    diff=sum1-sum2
    if diff<0:
        return -diff
    else:
        return diff              
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
