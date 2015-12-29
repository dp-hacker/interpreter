#-*- coding:UTF-8 -*-
__author__ = 'dhs'
from matplotlib import pyplot as plt
import numpy as np
from numpy import cos as COS, sin as SIN
import grammar_analyer

def draw():
    figure = plt.figure(figsize=(12,12),dpi=80,facecolor='gray')  # 坐标纸属性设置
    ax = plt.gca()
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    pointList = np.arange(eval(grammar_analyer.loop[0]),eval(str(grammar_analyer.loop[1])),eval(str(grammar_analyer.loop[2])))
    # 运用eval函数的性质，将T换为数据集，计算str类型的数学式，如cos(T),边换成cos(pointList)
    x = eval(grammar_analyer.loop[3].replace('T','pointList'))
    y = eval(grammar_analyer.loop[4].replace('T','pointList'))
    # 旋转
    x_new = x * COS(eval(str(grammar_analyer.rot))) + y * SIN(eval(str(grammar_analyer.rot)))
    y_new = y * COS(eval(str(grammar_analyer.rot))) - x * SIN(eval(str(grammar_analyer.rot)))
    x_new*=float(grammar_analyer.scale[0])
    y_new*=float(grammar_analyer.scale[1])  # 比例
    #print x_new,y_new
    #x_new+=float(grammar_analyer.origin[0])
    #y_new+=float(grammar_analyer.origin[1])
    ax.plot(x_new,y_new,)
    plt.grid(True)
    plt.xlim((-20000,20000))  # x,y轴限制
    plt.ylim((-20000,20000))
    plt.show()

if __name__ == '__main__':
    draw()
