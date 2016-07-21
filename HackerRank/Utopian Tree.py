# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
for _ in range(n):
    cycle = int(raw_input())
    k = cycle / 2
    height = 1 if cycle % 2 == 0 else 2
    print 2**(k+height) - height
