import numpy as np

def matrix_multiply():
    N = int(input("Enter size N: "))
    print(f"Enter first {N}x{N} matrix:")
    A = []
    for _ in range(N):
        row = list(map(int, input().split()))
        A.append(row)

    print(f"Enter second {N}x{N} matrix:")
    B = []
    for _ in range(N):
        row = list(map(int, input().split()))
        B.append(row)

    A = np.array(A)
    B = np.array(B)

    result = np.dot(A, B)

    print("Matrix product is:")
    print(result)

# Run the function
matrix_multiply()
