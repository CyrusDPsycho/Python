length = int(raw_input().strip())
arr = list(raw_input().split())
a = {}
global freq
for i in arr: 
    a[i] = arr.count(i)
      
print a
maxx = []

for j in a.values():
    maxx.append(j)
M = max(maxx)

for k in a: 
    if a[k] == M: 
        freq = k 
        
print freq

arr = [x for x in arr if x!=freq]
print len(arr)
