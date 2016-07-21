import sys


n = int(raw_input().strip())
j = 0
for i in range(n,0,-1):
    print (i-1)*' ' + (j+1)*'#'
    j+=1
