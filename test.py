# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:14:34 2017

@author: DAKS
"""


#from sympy import limit, Symbol, oo, sin

#coding = utf-8
#simpson 法計算積分，數值積分，效果非常理想
import matplotlib.pyplot as plt
from sympy import sin

s = 0

for i in range(1, 360):
    s = s + (1/i)
    plt.scatter(i, s)
    plt.scatter(i, 1/i) 
plt.show()    