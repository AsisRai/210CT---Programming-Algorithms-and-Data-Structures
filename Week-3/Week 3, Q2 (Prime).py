""" Write a recursive function (pseudocode and code) to check if a number n is prime (hint: check whether
n is divisible by any number below n). """
#pseudocode

"""

GLOBAL A ← (input)//input a number to find out if it is a prime or not
GLOBAL B ← 2 //lowest prime number therefore acting as divisor

PRIMENUMBER(B,A)

    if A<← 1
       return false, print(A)

    else
        if B>← A
           return true, print(B)

        else
            if A = B
                return true, print(B)

            elif (B % A) == 0:
                return false, print(B)

            else 
                return PRIMENUMBER(B+1,A)

      
    return false

"""

#python code

Number = int(input("Please input a number: "))
divisor = 2 #lowest prime number, divisor

def PRIMENUMBER(divisor,Number):
    
    if Number <= 1:
        return False, print(Number,"= Number cannot be negative or below lowest prime 2")
    else:
        if divisor >= Number:
            return True, print(Number, "= This number is a PRIME number")
        else:
            if Number == divisor:
                return True, print(Number, "= This number is a PRIME number")
            elif (Number % divisor) == 0:
                return False, print(Number, "= This number is NOT a prime number")
            else:
                return PRIMENUMBER(divisor+1,Number)


    return False

PRIMENUMBER(divisor,Number)

#http://stackoverflow.com/questions/37095508/how-do-i-find-a-prime-number-using-recursion-in-python
