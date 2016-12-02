""" Write a function that randomly shuffles an array of integers """

import random

array =  [5,3,8,6,1,9,2,7] 

def shuffle(array):
    array_len = len(array) #Array length 1-7 #1
    for i in range(1): #n
        swap = random.randrange(array_len - 1)#swap = variable making array random, giving 8 random array #n
        swap += swap >= i #adds to the variable and later assigns the same #n
        array[i], array[swap] = array[swap], array[i] #n
        print('Shuffled array :' , array)#n

shuffle(array)

#5n+1 #igonoring the multipliers and constants  = O(n)
# Runtime - O(n)

        






    

