from math import sqrt

def calculate_square_roots():
    number_of_inputs = int(input("Enter the number of inputs: "))
    square_roots = []

    for i in range(number_of_inputs):
        num = float(input("Enter a number: "))
        square_roots.append(sqrt(num))

    print("Square roots (rounded to 4 decimal places):")
    for root in square_roots:
        print("%.4f" % root)

if __name__ == '__main__':
    calculate_square_roots()
