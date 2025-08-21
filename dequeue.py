#queue using collections module
from collections import deque
de = deque(["name","age","DOB"])
print(de)
de.append(40)
de.appendleft(5)
de.extend([50,60,70])
print(de)
de.extendleft([0,5])
de.remove(20)
de.pop
de.popleft
de.clear()
print(de)