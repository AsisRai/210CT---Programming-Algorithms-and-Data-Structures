
"""Adapt the binary search algorithm so that instead of outputting whether a specific value was found, it
outputs whether a value within an interval (specified by you) was found. Write the pseudocode and
code and give the time complexity of the algorithm using the Big O notation"""
#Search Algorithm:
# 1 Find middle value of sequence.
# 2 If search value == middle value then success.
# 3 If search value is < middle value then forget about the top half of the
#sequence.
# 4 If search value is > middle value then forget about the bottom half of
#the sequence.
# 5 Repeat from step 1 until len(sequence)==0.


#pseudocode

"""
Global A ← [array]
Global B ← (input)
Global C ← (input)
Global D ← length(A)
Global E ← 0

BINARYSEARCH(A,B,C,E,D)
    if D - E <←1
       print('False')

    else
       F ← (D+E) mod2
       if A[F] > B and A[F] <C
          print('True')
       elif C<←[F]
          return BINARYSEARCH(A,B,C,E,F-1)
       elif B>← A[F]
          return BINARYSEARCH(A,B,C,F+,D)

BINARYSEARCH(A,B,C,E,D)

while false
    BINARYSEARCH(A,B,C,E,D)
 
"""
#Python Code

import sys

array = [2,3,5,7,9,13]
lowinterval = int(input("Please input the lower interval: "))
highinterval = int(input("Please input the higher interval: "))
highkey = len(array)
lowkey = 0 
  
def BINARYSEARCH(array, lowinterval, highinterval, lowkey, highkey):  
    if highkey - lowkey <=1: #1
        print("False") #1

    else: 
        midvalue = (highkey+lowkey) //2 #Floor Division #1
        if array[midvalue] > lowinterval and array[midvalue] < highinterval: #1
            print("True")#1
        elif highinterval<=array[midvalue]:#1
            return BINARYSEARCH(array, lowinterval, highinterval, lowkey, midvalue-1)#1
        elif lowinterval>=array[midvalue]:#1
            return BINARYSEARCH(array, lowinterval, highinterval, midvalue+1, highkey)#1
       
    
BINARYSEARCH(array, lowinterval, highinterval, lowkey, highkey)
        
while False: #n
            BINARYSEARCH(array, lowinterval, highinterval, lowkey, highkey)#1n
            

#Big O Runtime = O(n)

sys.exit()



