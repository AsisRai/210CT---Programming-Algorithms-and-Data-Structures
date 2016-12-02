
"""  Write the pseudocode for a function which returns the highest perfect square which is less or equal to
its parameter (a positive integer). Implement this in the programming language of your choice """

#PSEUDOCODE

"""

GLOBAL A ← (input a number)
GLOBAL B ← A

SQUAREROOT(A)
    C ← A ** 0.5
    D ← C
    return D

HIGHESTSQUARE(D)
    E ← D * D
    Print(E)
    
"""
#Python Code

input1 = input("Please input a number: ")
conin = int(input1) #converted input from string to intergers

def SQUAREROOT(conin): #to find the square root first
    Squirt1 = conin ** 0.5
    ConSquire = int(Squirt1)
    return ConSquire #returned so that it can be used in next function

def HIGHESTSQUARE(Squirt1): #now the values can be used from function above 
    Squirt2 = int(Squirt1) * int(Squirt1)
    print('Highest Perfect Square is', Squirt2)
    
(HIGHESTSQUARE(SQUAREROOT(conin)))





    


