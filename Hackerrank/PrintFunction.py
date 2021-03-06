if __name__ == '__main__':
    n = int(input())
     # Establish value to return
    val = 0
    # Establish exponent for adding each digit
    exp = 0

    # Loop through digits from a to 0; add along the way
    for i in range(n, 0, -1):
        # Get digits in i, store in vals in reverse order
        b = i
        vals = []
        while b > 0:
            vals.append(b % 10)
            b //= 10
        # Add vals to val
        for j in vals:
            val += 10**exp * j
            exp += 1
    
    print(val)