import numpy as np

def AND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7 #AND条件を満たす重みづけ(w)とバイアス(b)を人間か決める
    y = np.sum(x*w) + b
    if y <= 0:
        return 0
    else:
        return 1

print("---AND---")
print(AND(0, 0)) # 0 を出力
print(AND(1, 0)) # 0 を出力
print(AND(0, 1)) # 0 を出力
print(AND(1, 1)) # 1 を出力

def OR(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2 #OR条件を満たす重みづけ(w)とバイアス(b)を人間か決める
    y = np.sum(x*w) + b
    if y <= 0:
        return 0
    else:
        return 1

print("---OR---")
print(OR(0, 0)) # 0 を出力
print(OR(1, 0)) # 1 を出力
print(OR(0, 1)) # 1 を出力
print(OR(1, 1)) # 1 を出力

def NAND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7 #NAND条件を満たす重みづけ(w)とバイアス(b)を人間か決める
    y = np.sum(x*w) + b
    if y <= 0:
        return 0
    else:
        return 1

print("---NAND---")
print(NAND(0, 0)) # 1 を出力
print(NAND(1, 0)) # 1 を出力
print(NAND(0, 1)) # 1 を出力
print(NAND(1, 1)) # 0 を出力

def XOR(x1, x2):
    s1 = OR(x1,x2)
    s2 = NAND(x1,x2)
    y = AND(s1,s2)
    if y <= 0:
        return 0
    else:
        return 1    

print("---XOR---")
print(XOR(0, 0)) # 0 を出力
print(XOR(1, 0)) # 1 を出力
print(XOR(0, 1)) # 1 を出力
print(XOR(1, 1)) # 0 を出力
