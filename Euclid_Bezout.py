def euclid_gcd(number, divisor): #function that takes 2 numbers and calculates their gcd using Euclid's algorithm
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

def print_table(table):
    print('{:>10}'.format('p'), '{:>9}'.format('q'), '{:>9}'.format('s'), '{:>9}'.format('t')) #set header format for table
    out = '' #initialize empty string variable
    for row in table: #for each row in table
        for i in range(0, len(row)): #for each element in row at index i
            out += '{:>10}'.format(row[i]) #print element of row at index i with format
        print(out) #when inner loop ends, print out string
        out = '' #clear out string

def bezout(a, b): #function that takes 2 numbers and use tabular method to compute Bezout coefficients
    if (a == 0 and b == 0): #if both numbers are 0, then return (s, t) as (0, 0)
        return (0, 0)
    if(a == 0): #if a is 0, then return (s, t) as (0, 1)
        return (0, 1)
    if(b == 0): #if b is 0, then return (s, t) as (1, 0)
        return (1, 0)
    table = [[a, 0, 1, 0], [b, int(a / b), 0, 1]] 
#    initialize table
#    | remainder | quotient | s | t |
#    |     a     |     0    | 1 | 0 |
#    |     b     |    a/b   | 0 | 1 |
#    this table grows dynamically
    i = 2 #set iterator to 2 ('poining' to a new row in table)
    while(True): #while true
        row = [table[i - 2][0] % table[i - 1][0], 0, 0, 0] #initialize new row, set all values to 0 with exception of the first entry
        #the i-th remainder is equal to remainder at row i-2 mod quotient at row i-1
        if(row[0] == 0): #if the quotient at the i-th row equal 0, then exit while loop
            table.append(row) #append last row to table
            print_table(table) #call print_table()
            break;
        row[1] = int(table[i - 1][0] / row[0]) 
        #set the i-th quotient equal to remainder at i-1 over i-th remainder
        row[2] = table[i - 2][2] - (table[i - 1][1] * table[i - 1][2]) 
        #set the i-th s Bezout coefficient equal to the s Bezout cofficient at row i - 2, minus the product of quotient at i-1 times s Bezout coefficient at i - 1
        row[3] = table[i - 2][3] - (table[i - 1][1] * table[i - 1][3])
        #set the i-th t Bezout coefficient equal to the s Bezout cofficient at row i - 2, minus the product of quotient at i-1 times t Bezout coefficient at i - 1
        table.append(row) #add computed row to table
        i += 1 #increment iterator by 1
    return (table[i-1][2], table[i-1][3]) #return tuple with final s and t Bezout coefficients

def launch(num1, num2): #function that takes two unordered numbers and calls 
    num1 = abs(num1) #if any of the numbers is negative, get their absolute value and replace
    num2 = abs(num2)
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


