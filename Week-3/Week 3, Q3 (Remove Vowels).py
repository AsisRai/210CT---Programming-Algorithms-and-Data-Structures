""" recursive function (pseudocode and code)
that removes all vowels from a given string"""

#pseudocode
"""
GLOBAL A ←(input) //input word to remove vowels

REMOVEVOWELS(B)
    if length(B)=0
        return B
    else
        C ← B[1:length(B)+1]
        D ← B[0]
        if D in "a,e,i,o,u,A,E,I,O,U"
            return REMOVEVOWELS(C)
        else
            return D + REMOVEVOWELS(C)

print(REMOVEVOWELS(A))

"""
#Python Code

a = input("Type in a word: ")
def REMOVEVOWELS(userpinput):
    if len(userpinput) == 0:
        return userpinput 
    else:
        vowelsremove = userpinput[1:len(userpinput) + 1]
        firstelement = userpinput[0] #looks up first letter from userinput
        if firstelement in "a,e,i,o,u,A,E,I,O,U":
            return REMOVEVOWELS(vowelsremove)
        else:
            return firstelement + REMOVEVOWELS(vowelsremove)# add first letter back at start after removing rest
            

print(REMOVEVOWELS(a))
