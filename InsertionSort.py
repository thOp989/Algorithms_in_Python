# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:32:22 2016

@author: Tim
"""

#We are given an array of numbers. 
#Our goal is to sort the array in increasing order via InsertionSort.
#To do this, we have a new array, to place each element of the original array into,
# one at a time. 
#
0
# This function will sort an array B, while B[0: len(B)-1] is a sorted array, 
#but the whole array B may not be. So this definition finds the right location 
#for B[len(B)-1] in the array of B. 
def FixArray(B):
    m = len(B);
    for j in range(m-1):
        newvalue = B[m-1-j];
        if (B[m-1-j-1] <= B[m-1-j]):
            break;
        else:
            b = B[m-1-j-1]
            B[m-1-j-1] = newvalue;
            B[m-1-j] = b;
    return (B);

# This function creates another array B, adds one element of A to B at a time, 
#then sorts B after each insertion. 
def InsertionSort(A):
    B = [];
    n = len(A);
    for i in range(n):
        B.append(A[i]);
        B = FixArray(B);
    return B;

def main():
    A = [2,4,6,2,3,1,1];
    print (InsertionSort(A))
    
main()





