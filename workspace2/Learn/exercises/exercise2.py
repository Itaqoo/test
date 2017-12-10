#!/bin/bash
def square(x):
    return x*x
def string(x):
    print(x)
def required(x,y,z,opt1=1,opt=2):
    return x+y+z

def fun1(x):
    return x/2
def fun2(x):
    return x*4
test=fun1(5)
print(fun2(test))
def fl(x):
    try:
        return float(x)
    except FloatingPointError:
        pass
