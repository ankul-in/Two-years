#kata
#https://www.codewars.com/kata/5efae11e2d12df00331f91a6/train/python

import hashlib
def crack(md5_hash: str) -> str:
    target = md5_hash.strip().lower()
    for n in range(100000):
        pin = f"{n:05d}"
        digest = hashlib.md5(pin.encode("utf-8")).hexdigest()
        if digest == target:
            return pin
    raise ValueError("No matching 5-digit PIN found for the provided MD5 hash.")