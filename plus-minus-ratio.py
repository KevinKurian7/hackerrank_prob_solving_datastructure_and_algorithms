#!/bin/python3
#https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    z=0
    p=0
    m=0
    for i in range(len(arr)):
        if arr[i]>0:
            p=p+1
        elif arr[i]==0:
            z=z+1
        elif arr[i]<0:
            m=m+1        
    print(p/n)
    print(m/n)
    print(z/n)
            
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
