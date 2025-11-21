#kata
#https://discord.com/channels/1049951289209012244/1233479204373401721

from collections import deque
from typing import Generator, Tuple
def all_rationals() -> Generator[Tuple[int, int], None, None]:
    queue = deque([(1, 1)])
    while True:
        a, b = queue.popleft()
        yield (a, b)
        queue.append((a, a + b))  
        queue.append((a + b, b))