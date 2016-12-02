"""Function to return the factorial of a number using recursion"""

userin = input('Please input a number: ') #takes the imput from the user
inconv = int(userin) #converts the string input to integer

def trailing0s(n): #Hint: Count the prime factors of 5 #http://code.activestate.com/recipes/577844-calculate-trailing-zeroes-in-a-factorial/
    factorial5 = 0 #output value of 0's? #1
    for number in range(2, n+1):  #generates 2 numbers and performs action input+1 #n        
        while number > 0: #n
            if number % 5 == 0: #exactly divisible by 5 with remainder 0 #n
                factorial5 += 1 #add one to output #n
                number = number/5 #n
            else: 
                break #n
    return factorial5 #1    

print("The number of trailing 0s are", trailing0s(inconv))


# 7n+1 = 0(n)
