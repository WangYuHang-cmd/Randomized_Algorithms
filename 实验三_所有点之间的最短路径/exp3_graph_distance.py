import Seidel
import Strassen
import numpy as np
from time import time
import matplotlib.pyplot as plt

st = time()

def get_graph(n:int):
    A = np.random.randint(low=0,high=2,size=(n,n))
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 0
    # print(A)
    return A


def solve():
    n=int(input("请输入随机生成的图的大小:"))
    seidel = Seidel.Seidel2()
    st = time()
    A = get_graph(n)
    B = seidel.get_distance_matrix(A)
    ed = time()
    print("Seidel算法(手写矩阵乘法)耗时"+str(ed-st))
    st = ed
    seidel1 = Seidel.Seidel1()
    C = seidel1.get_distance_matrix(A)
    ed = time()
    print("优化矩阵乘法后的Seidel算法耗时:"+str(ed-st))
    st=ed
    seidel2 = Seidel.Seidel()
    D = seidel2.get_distance_matrix(A)
    ed = time()
    print("Seidel算法(numpy自带矩阵乘法)耗时"+str(ed-st))

def calc(n:int):
    st = time()
    A = get_graph(n)
    seidel2 = Seidel.Seidel()
    D = seidel2.get_distance_matrix(A)
    ed = time()
    return ed - st

if __name__ == '__main__':
    st = time()
    solve()
    cnt = 16
    xs=[]
    ys=[]
    while cnt < 4096:
        xs.append(cnt)
        ys.append(calc(cnt))
        cnt *= 2
    plt.plot(xs, ys)
    plt.title("Seidel-Efficency")
    plt.show()