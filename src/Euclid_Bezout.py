import sys

from Euclid_GCD import euclid_gcd

def print_table(table):
    print('{:>10}'.format('p'), '{:>9}'.format('q'), '{:>9}'.format('s'), '{:>9}'.format('t')) #set header format for table
    out = '' #initialize empty string variable
    for row in table: #for each row in table
        for i in range(0, len(row)): #for each element in row at index i
            out += '{:>10}'.format(row[i]) #print element of row at index i with format
        print(out) #when inner loop ends, print out string
        out = '' #clear out string

def bezout(a, b):
    # Check for base cases and return appropriately
    if (a == 0 and b == 0):
        return (0, 0)
    elif(a == 0): 
        return (0, 1)
    elif(b == 0): 
        return (1, 0)
    # Initialize table and append the first 2 rows
    # The Bezout coefficient will be placed at the end of the s and t columns
    # | remainder | quotient | s | t |
    # |     a     |     0    | 1 | 0 |
    # |     b     |   a//b   | 0 | 1 |
    table = [] 
    table.append([a, 0, 1, 0]) 
    table.append([b, a // b, 0, 1])
    # Index to table pointing the next row
    i = 2 
    while(True):
        # Create new row with and set remainder value. The i-th remainder
        # is equal to remainder at row i-2 % remainder at row i-1
        row = [table[i - 2][0] % table[i - 1][0], 0, 0, 0]
        # If remainder is 0, then end the loop
        if(row[0] == 0):
            table.append(row)
            print_table(table)
            break
        # Set quotient value in new row
        row[1] = table[i - 1][0] // row[0]
        # Set the i-th s Bezout coefficient equal to the s Bezout cofficient at row i-2
        # minus the product of quotient at i-1 times s Bezout coefficient at i-1
        row[2] = table[i - 2][2] - (table[i - 1][1] * table[i - 1][2]) 
        # Set the i-th t Bezout coefficient equal to the t Bezout cofficient at row i-2
        # minus the product of quotient at i-1 times t Bezout coefficient at i-1
        row[3] = table[i - 2][3] - (table[i - 1][1] * table[i - 1][3])
        # Now that the row has been populated, add it to the table
        table.append(row)
        # Increase index by one
        i += 1
    return table[i-1][2], table[i-1][3]

def main():
    if(len(sys.argv) != 3):
        print('usage: python3 Bezout_Coefficients.py <num1> <num2>')
        return
    try:
        nums = [abs(int(sys.argv[1])), abs(int(sys.argv[2]))]
    except:
        print('<num1> and <num2> must be numeric integer values')
        return
    nums.sort(reverse=True)
    gcd = euclid_gcd(nums[0], nums[1])
    bezout_result = bezout(nums[0], nums[1])
    print("gcd(" + str(nums[0]) + "," + str(nums[1]) + ") = " + str(gcd))
    print(str(nums[0]), "*", str(bezout_result[0]), "+", str(nums[1]), "*", str(bezout_result[1]), "=", str(gcd))

if(__name__ == '__main__'):
    main()