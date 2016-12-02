
""" Given a sequence of n integer numbers, extract the sub-sequence of maximum length which is in
ascending order. Example input: L = [1,2,3,4,1,5,1,6,7] Output: [1,2,3,4]
"""

import sys

sequence = [1,2,3,4,1,5,1,6,7]
newsequence = [1] #initial temporary output

def SUBEXTRACTOR(sequence, newsequence): #This will count each ascending pair and will add it to the new sequence 
	counter = 1
	
	for i in range(0, len(sequence)):
		if i == len(sequence) - 1:
			break
		else:
			if sequence[i] < sequence[i+1]:
				counter += 1
				newsequence.append(counter)
			elif sequence[i] > sequence[i+1]:
				counter = 1
				newsequence.append(counter)
				

				
SUBEXTRACTOR(sequence, newsequence)

def HIGHESTVALUE(sequence, newsequence):
                
        Highestval = newsequence.index(max(newsequence)) #This will take the highest value in the newsequence
        output = [] #New temporary output

        for i in range(1, max(newsequence)+1): #This will take values existing already, notes their position and and over-rides+1
                output.append(Highestval)
                Highestval -= 1

        output.reverse()
        newtemporary = [] #Final temporary output

        for j in output: #Takes the values out of the intial sequence which is then printed
                newtemporary.append(sequence[j])

        print('Given Sequence was: ',sequence)
        print('New sub-extracted sequence: ',newtemporary)

HIGHESTVALUE(sequence, newsequence)

sys.exit()

