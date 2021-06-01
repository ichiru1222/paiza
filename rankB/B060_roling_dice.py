import io
import sys

_INPUT = """\
7 3 4
2 1
DRRUULL
"""
sys.stdin = io.StringIO(_INPUT)

import numpy as np

NHW_list = list(map(int, input().split()))
s_list = list(map(int, input().split()))
s = list(input().split())

N = NHW_list[0]
H = NHW_list[1]
W = NHW_list[2]
s_y = s_list[0]
s_x = s_list[1]

frag = np.zeros((H, W), dtype=int)

"""
[]is index
     2[0]
3[2] 1[3] 4[4] 6[5]
     5[1]
"""
initial_pos = [2, 5, 3, 1, 4, 6]

class Dice():
    def __init__(self, initial_pos):
        self.initial_pos = initial_pos
        self.pos = []

    def rolling(self,turn):
        pos = self.initial_pos
        if turn == "D":
            pos[0], pos[1], pos[3], pos[5] = pos[5], pos[3], pos[0], pos[1]
        if turn == "U":
            pos[0], pos[1], pos[3], pos[5] = pos[3], pos[5], pos[1], pos[0]
        if turn == "L":
            pos[2], pos[3], pos[4], pos[5] = pos[3], pos[4], pos[5], pos[2]
        if turn == "R":
            pos[2], pos[3], pos[4], pos[5] = pos[5], pos[2], pos[3], pos[4]
        self.initial_pos = pos
        return pos


dice = Dice(initial_pos)
for n in range(N):
    if n == 0:
        bottom_dice = dice.initial_pos[5]
        frag[s_y -1][s_x -1] = bottom_dice
    pos = dice.rolling(s[0][n])
    if s[0][n] == "U":
        s_y -= 1
    if s[0][n] == "D":
        s_y += 1
    if s[0][n] == "R":
        s_x += 1
    if s[0][n] == "L":
        s_x -= 1
    bottom_dice = pos[5]
    frag[s_y -1][s_x -1] = bottom_dice
    #print(bottom_dice)
    
    #print(dice.initial_pos)
for _ in range(H):
    print(*frag[_])