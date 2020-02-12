def euclid_gcd(number, divisor):
    quotient = 0
    remainder = 0
    while(divisor != 0):
        accumulator = 0
        while(divisor * (accumulator + 1) <= number):
            accumulator += 1
        quotient = accumulator
        remainder = number - divisor * quotient
        print(number, "=", divisor, "*", quotient, "+", remainder)
        number = divisor
        divisor = remainder
    return number

def benzout(a, b):
    table = [[a, 0, 1, 0], [b, int(a / b), 0, 1]]
    i = 2
    while(True):
        row = [table[i - 2][0] % table[i - 1][0], 0, 0, 0]
        if(row[0] == 0):
            break;
        row[1] = int(table[i - 1][0] / row[0])
        row[2] = table[i - 2][2] - (table[i - 1][1] * table[i - 1][2])
        row[3] = table[i - 2][3] - (table[i - 1][1] * table[i - 1][3])
        table.append(row)
        i += 1
    return (table[i-1][2], table[i-1][3])

def launch(num1, num2):
    if(num1, num2):
        temp = num1
        num1 = num2
        num2 = temp
    gcd = euclid_gcd(num1, num2)
    benzout_result = benzout(num1, num2)
    print("gcd(", num1, ",", num2, ") =" , gcd)
    print(num1, "*", benzout_result[0], "+", num2, "*", benzout_result[1], "=", gcd)


num1 = int(input("Enter a number: " ))
num2 = int(input("Enter another number: "))
launch(num1, num2)



