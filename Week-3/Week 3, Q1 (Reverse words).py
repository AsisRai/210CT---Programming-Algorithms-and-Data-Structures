""" Write the pseudocode and code for a function that reverses the words in a sentence. Input: "This is
awesome" Output: "awesome is This". Give the Big O notation """

#pseudocode

"""
A ← (input)// user input as string
B ← []
C ←  A.split("")

for i in range(C,0,-1)
    B.append(C[i-1])

B ← ''.join(B)

print(B)

"""

#python code

sentence = ('This is awesome')
output = []
step1 = sentence.split(" ")

for i in range (len(step1), 0, -1): #n
    output.append(step1[i-1]) #1

output = ' '.join(output) #1

print(output) #1

#Runtime = n+3
#BigO = O(n)


