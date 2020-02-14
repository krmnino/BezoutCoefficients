def euclid_gcd(number, divisor):
    quotient = 0 #set quotient and remainder to 0
    remainder = 0
    while(divisor != 0): #while divisor is not 0...
        while(divisor * (quotient + 1) <= number): #while divisor * (quotient + 1) is less or equal than number
            quotient += 1 #increment quotient by 1
        remainder = number - divisor * quotient #set remainder equal to number - divisor * quotient 
        print(number, "=", divisor, "*", quotient, "+", remainder) #print the current state of the variables
        number = divisor  #for the next iteration, set number to divisor
        divisor = remainder #...set divisor equal to remainder
        quotient = 0 #...and set quotient equal to zero
    return number #when the outer while-loop ends, return current state of variable number

def bezout(a, b): #function that takes 2 numbers and use tabular method to compute Bezout coefficients
    table = [[a, 0, 1, 0], [b, int(a / b), 0, 1]] 
    '''
    initialize table
    | remainder | quotient | s | t |
    |     a     |     0    | 1 | 0 |
    |     b     |    a/b   | 0 | 1 |
    this table grow dynamically
    '''
    i = 2 #set iterator to 2 ('poining' to a new row in table)
    while(True): #while true
        row = [table[i - 2][0] % table[i - 1][0], 0, 0, 0] #initialize new row, set all values to 0 with exception of the first entry
        #the i-th remainder is equal to remainder at row i-2 mod quotient at row i-1
        if(row[0] == 0): #if the quotient at the i-th row equal 0, then exit while loop
            break;
        row[1] = int(table[i - 1][0] / row[0]) #set the i-th quotient equal to remainder at i-1 over i-th remainder
        row[2] = table[i - 2][2] - (table[i - 1][1] * table[i - 1][2]) 
        #set i-th s Bezout coefficient equal to quotient at i-1 times s Bezout coefficient at i - 1, then subtract s Bezout cofficient at row i - 2 from the product 
        row[3] = table[i - 2][3] - (table[i - 1][1] * table[i - 1][3])
        #set i-th t Bezout coefficient equal to quotient at i-1 times t Bezout coefficient at i - 1, then subtract t Bezout cofficient at row i - 2 from the product
        table.append(row) #add computed row to table
        i += 1 #increment iterator by 1
    return (table[i-1][2], table[i-1][3]) #return tupple with final s and t Bezout coefficients

def launch(num1, num2): #function that takes two unordered numbers and calls 
    if(num1 < num2): #if second number is greater than the first one, swap them
        temp = num1
        num1 = num2
        num2 = temp
    gcd = euclid_gcd(num1, num2) #call euclid_gcd() and bezout() and store returned values respectively
    bezout_result = bezout(num1, num2)
    print("gcd(", num1, ",", num2, ") =" , gcd) #print gcd variable
    print(num1, "*", bezout_result[0], "+", num2, "*", bezout_result[1], "=", gcd) #print Bezout coefficients


num1 = int(input("Enter a number: " )) #ask for user input, converts it into integers
num2 = int(input("Enter another number: "))
launch(num1, num2) #call wrapper function



