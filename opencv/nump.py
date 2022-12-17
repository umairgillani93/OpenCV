import os
import cv2
import sys
import json
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

arr = np.arange(15).reshape(3, 5)
print(arr)

print(f'\nshape: {arr.shape}')
print(f'\ndimension: {arr.ndim}')
print(f'\ndata type: {arr.dtype.name}')
print(f'\nitemsize: {arr.itemsize}')
print(f'\nsize: {arr.size}')
print(f'\narray type: {type(arr)}')

print(f'\ndtype: {arr.dtype}')

b = np.array([
    [1,2,3,4],
    [4,5,6,7],
    ])

print(b.shape)
print(f'\nb dimension: {b.ndim}')

zeros = np.zeros(shape = (3,4))

print(f'\nzeros: {zeros}')
print(f'\nzeros shape: {zeros.shape}')

ones = np.ones(shape = (3, 7), dtype = np.int16)

arranged_arr = np.arange(10, 100, 10)

print(f'\narranged: {arranged_arr}')

line = np.linspace(0, 10, 10)

print(f'\nnumbers line: {line}')

x = np.linspace(0, 2 * np.pi, 100)

print(f'\n: x is: {x}')

sin_x = np.sin(x)

print(f'\nsine x: {sin_x}')

d3_arr = np.arange(24).reshape(2, 3, 4)

print(f'\nthree dimentional array: {d3_arr}')

print('3d dimension: {}'.format(d3_arr.ndim))
print('3d shape: {}'.format(d3_arr.shape))

A = np.array([[1,1],
    [1,2]])

B = np.array([[1,0],
    [2,1]])

print('element wise: {}'.format(A * B))
print('matrix wise: {}'.format(A @ B))

rnd = np.random.rand(10)

print(d3_arr)
