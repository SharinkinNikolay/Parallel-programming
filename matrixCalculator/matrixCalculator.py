import threading
import time
import numpy as np

class Matrix:

    def __init__(self, m, n):
        self.n = n
        self.m = m

    def read_matrix(self, path, size):
        matrix = np.zeros((size, size))
        with open(path) as file:
            for i, line in enumerate(file):
                row = list(map(int, line.split()))
                matrix[i] = row
        return matrix

def cycle(A, B, C, i):
    for j in range(B.shape[1]):
        C[i][j] = 0
        for k in range(A.shape[1]):
            C[i][j] += A[i][k] * B[k][j]

def multiply_without_thread(A, B):
    start = time.time()
    C = np.dot(A, B)
    end = time.time()
    print("Time without threads:", end - start)
    return C

def multiply_thread(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    threads = []
    start = time.time()
    for i in range(A.shape[0]):
        th = threading.Thread(target=cycle, args=(A, B, C, i))
        th.start()
        threads.append(th)
    for th in threads:
        th.join()
    end = time.time()
    print("Time with threads:", end - start)
    return C


pathA = "D:\\Проекты\\secondcourse\\vscode\\matrixCalculator\\matrixA.txt"
pathB = "D:\\Проекты\\secondcourse\\vscode\\matrixCalculator\\matrixB.txt"
size = 200

A = Matrix(size, size).read_matrix(pathA, size)
B = Matrix(size, size).read_matrix(pathB, size)

R1 = multiply_without_thread(A, B)
R2 = multiply_thread(A, B)

for i in range(R1.n):
        for j in range(R1.m):
            print(R1.matrix[i][j], end = " ")
        print()
