import io
import sys

_INPUT = """\
5 3 2
RRLLF
RRL
RL
"""
sys.stdin = io.StringIO(_INPUT)

nab_list = list(input().split())
s_N = input()
s_A = input()
s_B = input()

N = int(nab_list[0])
A = int(nab_list[1])
B = int(nab_list[2])

for n in range(N):
    if s_A[0] == s_N[n]:
        s_A = s_A[1:A]
        A -= 1

    if s_B[0] == s_N[n]:
        s_B = s_B[1:B]
        B -= 1
print(A,B)

