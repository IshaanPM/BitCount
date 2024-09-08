def count_bits(n):
    ones = 0
    zeros = 0
    totalbits = 0
    while n > 0:
        totalbits += 1
        if n & 1:   
            ones += 1
        else:       
            zeros += 1
        n >>= 1    
    
    print(f"Total number of bits: {totalbits}")
    print(f"Number of 1 bits: {ones}")
    print(f"Number of 0 bits: {zeros}")

# Example usage
number = int(input("Enter a number: "))
count_bits(number)
