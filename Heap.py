# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:44:56 2016

@author: Tim
"""
import math

def leftChild(place):
    return 2*place;
    
def rightChild(place):
    return 2*place + 1;
    
def parent(place):
    return math.floor(place/2);

def CheckArraySize(A, newPlace):
    if (len(A)< newPlace):
        n = newPlace - len(A);
        none = [None]*n;
        A2 = A + none;
    else:
        A2 = A;
    return A2;
    
#Given an element of an array, the idea here is to see if this element satsifies
#the max heap property with its children. If so, a truth value is sent, along with
#the value of their children so long as they're not None, so that they can 
#be tested in the same way as well. 
#The hard part of this is when we are given children taht are None, so the
#conditions here work with that. 
def MaxHeapProperty(B, element):
    left = leftChild(element+1)-1;
    right = rightChild(element+1)-1;
    if ((B[left] == None) and (B[right] == None)):
        return True;
    elif (B[left] == None):
        if (B[right] >= B[element]):
            return [True, right];
        else:
            return [False]
    elif (B[right] == None):
        if (B[left] < B[element]):
            return [True, left];
        else: 
            return False;
    elif ((B[right] >= B[element] ) and (B[left] < B[element])):
        return [True, left, right];
    else:
        return False;
    
    
def MaxHeap(B):
    testableEntries = [0];
    while (len(testableEntries) > 0):
        for entry in testableEntries:
            results = MaxHeapProperty(B, entry);
            if (results[0] == False):
                return False;
            else: 
                newentries = results.pop([0]);
                testableEntries = testableEntries + newentries;
    return True;

def heapAdd(B, key):
    newPlace = 1;
    while (B[newPlace-1] != None):
        
        if (B[newPlace-1] < key):
            newPlace = rightChild(newPlace);

        else:
            newPlace = leftChild(newPlace);
        B = CheckArraySize(B, newPlace);#Increase size of array to make sure while loop keeps processing.
    B = CheckArraySize(B, newPlace); #Increase size of array to add key. 
    B[newPlace -1] = key; #Adding key to proper place in array. 
    return B;

#The idea here is to make a heap from an array. 

def heap():
    B = []
    B.append(A[0]);
    for i in range(len(A)-1):
        B = heapAdd(B, A[i+1]);
        
B = [0,-1,2]
print (MaxHeap(B))
