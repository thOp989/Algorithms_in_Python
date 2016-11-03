# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:19:46 2016

@author: Tim
"""

#Get array
#Check array stats, sorting increasing or decreasing? 
#Get key to search for.
#Check n/2 and cut array in half to new one. Keep repeating this
#Return key location if it exists or say it doesn't exist. 

#Method to cut array in half. 
import math
import numpy as np
import math

#We are given an array sorted in increasing order, with a given key. 
#We want to find what element in a given array has a value equal to a given key. 
# To do this, we will keep track of the upper and lower limits of the span of
#elements that could possibly have elements that have a value equal to the given key. 
# First, the lower limit is 0, and the upper limit is len(A)-1. Using BinarySearch, 
# we compare the floor(upper-lower/2) element to the key, and determine the new
#upper and lower limits. Once we apply this numerous times, there will be a time 
#when the upper and lower limits are equal to each other. At this point, if the 
#key is equal to the value of the element, we return the element location. If not, 
#the key doesn't exist and a string is returned with this. 

#The next function is 
def half(A, key, lower, upper):
    c = math.floor((upper-lower)/2);
    halfPlace = lower + c;
    if ((key < A[lower]) or (key > A[upper])):
        return ['Element does not exist'];
    elif (upper == lower):
        if (A[upper] == key):
            return [upper];
        else: 
            return ['Element does not exist'];
    elif (key == A[halfPlace]):
        return [halfPlace];
    elif (key < A[halfPlace]):
        upper = halfPlace;
        return [lower, upper];
    else:
        lower = halfPlace;
        return [lower, upper];

def BinarySearch(A, key):
    answer = [0,1];
    lower = 0;
    upper = len(A)-1;
    while (len(answer) > 1):
        answer = half(A,key,lower, upper);
        if (len(answer) == 2):
            lower = answer[0];
            upper = answer[1];
    return answer;
    

def main():
    A = [0,1,2,3,4,5,6,1000,1002,2000];
    key = 3;
    print (BinarySearch(A,key));


main();



