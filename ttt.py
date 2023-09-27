import sys
from collections import deque

a = [1,2,3]
q_a = deque(a)
print(q_a[0])
q_a.append(q_a.popleft())
print(q_a[0])