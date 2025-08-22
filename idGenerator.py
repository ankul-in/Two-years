import random
import time

users = []

def main():
    while True:
        time.sleep(0.5)
        random_number = random.randint(1, 999999999)
        url = (f'https://www.roblox.com/users/{random_number}/profile')
        print(url)
main()