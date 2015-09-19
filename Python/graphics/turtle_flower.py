# -*- coding: utf-8 -*-
'''
使用turtle模块绘制图像-flower

date:2015-09-19
'''

import turtle

windows = turtle.Screen()
babbage = turtle.Turtle()

babbage.color("green", "black")
babbage.left(90)
babbage.forward(100)
babbage.right(90)
babbage.circle(10)

for i in xrange(36):
    babbage.color("red", "green")
    babbage.left(10)
    babbage.forward(50)
    babbage.left(157)
    babbage.forward(50)
windows.exitonclick()
