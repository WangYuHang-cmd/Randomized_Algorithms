import numpy as np
import Strassen

class Seidel:
    def get_mask(self, n):
        return np.ones(n, dtype=int) - np.eye(n, dtype=int)

    def get_distance_matrix(self, A):
        Z = np.matmul(A, A)
        B = np.zeros(A.shape, dtype=int)
        for i in range(B.shape[0]):
            for j in range(B.shape[1]):
                B[i][j] = 1 if ((i != j) and (A[i][j] == 1 or Z[i][j] > 0)) else 0

        if (np.array_equal(B - self.get_mask(B.shape[0]), np.zeros(B.shape))): 
            D = 2*B - A
            return D

        T = self.get_distance_matrix(B)
        X = np.matmul(T, A)
        D = np.zeros(A.shape, dtype=int)
        for i in range(D.shape[0]):
            for j in range(D.shape[1]):
                D[i][j] = 2*T[i][j] if (X[i][j] >= T[i][j] * A[j].sum()) else 2*T[i][j] - 1
                # A[j].sum() - is degree of j verticle
        return D

class Seidel1(Seidel):
    def get_distance_matrix(self, A):
        Z = Strassen.strassen(A, A)
        B = np.zeros(A.shape, dtype=int)
        for i in range(B.shape[0]):
            for j in range(B.shape[1]):
                B[i][j] = 1 if ((i != j) and (A[i][j] == 1 or Z[i][j] > 0)) else 0

        if (np.array_equal(B - self.get_mask(B.shape[0]), np.zeros(B.shape))):
            D = 2 * B - A
            return D

        T = self.get_distance_matrix(B)
        X = Strassen.strassen(T, A)
        D = np.zeros(A.shape, dtype=int)
        for i in range(D.shape[0]):
            for j in range(D.shape[1]):
                D[i][j] = 2 * T[i][j] if (X[i][j] >= T[i][j] * A[j].sum()) else 2 * T[i][j] - 1
                # A[j].sum() - is degree of j verticle
        return D


def justmul(A:np.ndarray,B:np.ndarray):
    ans = np.zeros(A.shape, dtype=int)
    sz = A.shape[0]
    for i in range(sz):
        for j in range(sz):
            for k in range(sz):
                ans[i][j] += A[i][k] * B[k][j]
    return ans


class Seidel2(Seidel):
    # def justmul(A,B):
    #     ans = np.zeros(A.shape, dtype=int)
    #     sz = A.shape[0]
    #     for i in range(sz):
    #         for j in range(sz):
    #             for k in range(sz):
    #                 ans[i][j] += A[i][k] * B[k][j]
    #     return ans

    def get_distance_matrix(self, A):
        Z = justmul(A, A)
        B = np.zeros(A.shape, dtype=int)
        for i in range(B.shape[0]):
            for j in range(B.shape[1]):
                B[i][j] = 1 if ((i != j) and (A[i][j] == 1 or Z[i][j] > 0)) else 0

        if (np.array_equal(B - self.get_mask(B.shape[0]), np.zeros(B.shape))):
            D = 2 * B - A
            return D

        T = self.get_distance_matrix(B)
        X = justmul(T, A)
        D = np.zeros(A.shape, dtype=int)
        for i in range(D.shape[0]):
            for j in range(D.shape[1]):
                D[i][j] = 2 * T[i][j] if (X[i][j] >= T[i][j] * A[j].sum()) else 2 * T[i][j] - 1
                # A[j].sum() - is degree of j verticle
        return D

