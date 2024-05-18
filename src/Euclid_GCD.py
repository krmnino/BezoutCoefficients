# Euclid's Algorithm to find greatest common divisor of 2 numbers
def euclid_gcd(dividend, divisor, trace=False): 
    quotient = 0 
    remainder = 0
    # While divisor is not zero, keep iterating
    while(divisor != 0): 
        # While the result of the operation below is less or equal
        # than the dividend, then increase the quotient value by 1
        while(divisor * (quotient + 1) <= dividend):
            quotient += 1 
        # Set remainder value with the result of the operation below 
        remainder = dividend - divisor * quotient 
        # Print state of variables of the current iteration
        if(trace == True):
            print(dividend, "=", divisor, "*", quotient, "+", remainder)
        # Update dividend and divisor values, clear quotionet before
        # jumping into the next iteration
        dividend = divisor  
        divisor = remainder 
        quotient = 0
    # When divisor is 0, then the dividend is the greatest common divisor
    return dividend