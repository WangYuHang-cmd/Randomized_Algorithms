# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:55:48 2022

@author: Henry
"""

import math
import numpy as np
import matplotlib.pyplot as plt

xs = []
ys = []

def check(dt,n):
    return len(dt) == n

def work(n:int):
    dt = set()
    time = 0
    while check(dt, n) != 1:
        time += 1
        number = np.random.randint(0,n)
        dt.add(number)
    return time


n = int(input())
for i in range(1,n+1):
    tmp = []
    for j in range(100):
        new_time=work(i)
        tmp.append(new_time)
    tmp.sort()
    xs.append(i)
    ys.append(tmp[len(tmp)//2])

plt.plot(xs, ys)
plt.title("n-time")
plt.legend()
plt.show()