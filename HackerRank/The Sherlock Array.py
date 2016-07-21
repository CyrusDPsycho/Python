
test_cases = int(raw_input())
for _ in xrange(test_cases):
    n = raw_input()
    array_elements = map(int, raw_input().split())
    s = sum(array_elements)
    f = "NO"
    current_element = 0
    for i in xrange(len(array_elements)):
        if i > 0:
            current_element += array_elements[i-1]
        if current_element *2 == s-array_elements[i]:
            f= "YES"
            break
    print f
