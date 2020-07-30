"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
 when the input is not a number.
2. When will a ZeroDivisionError occur?
 when the input value is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator(non-zero number): "))
    denominator = int(input("Enter the denominator(non-zero number): "))
    while True:
        if denominator==0 or numerator==0:
            print('Cannot divide by zero!')
            numerator = int(input("Enter the numerator(non-zero number): "))
            denominator = int(input("Enter the denominator(non-zero number): "))
        else:            
            fraction = numerator / denominator
            print(fraction)
            break
except ValueError:
    print("Numerator and denominator must be valid numbers!")
""" except ZeroDivisionError:
    print("Cannot divide by zero!") """
print("Finished.")