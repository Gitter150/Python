import time
import numpy as np

print("This is a 3 x 3 Matrix Multiplier!")
time.sleep(1)

print("Enter the elements in the form of a typical matrix.")

print("Matrix 1")
r1 = input("Enter the elements of the first row: ")
r2 = input("Enter the elements of the second row: ")
r3 = input("Enter the elements of the third row: ")

print("Matrix 2")
R1 = input("Enter the elements of the first row: ")
R2 = input("Enter the elements of the second row: ")
R3 = input("Enter the elements of the third row: ")

# Split input strings into lists of strings
Mr1 = r1.split()
Mr2 = r2.split()
Mr3 = r3.split()
MR1 = R1.split()
MR2 = R2.split()
MR3 = R3.split()

# Convert lists of strings to lists of floats, then to NumPy arrays
try:
    M1 = np.array([list(map(float, Mr1)),
                   list(map(float, Mr2)),
                   list(map(float, Mr3))])

    M2 = np.array([list(map(float, MR1)),
                   list(map(float, MR2)),
                   list(map(float, MR3))])
    M = np.dot(M1, M2)
except ValueError:
    M1 = np.array([list(map(int, Mr1)),
                   list(map(int, Mr2)),
                   list(map(int, Mr3))])

    M2 = np.array([list(map(int, MR1)),
                   list(map(int, MR2)),
                   list(map(int, MR3))])
    M = np.dot(M1, M2)
    M = M.astype(int)

M=M.astype(int)
M = M.astype(str)

# Print the resulting matrix
print("\nResulting Matrix:")
for row in M:
    print(' '.join((row)))








