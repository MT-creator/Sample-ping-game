import random
import time

Password_list = ['abc', 'def', '1234', 'zzz', 'password00', 'creator', '23456aa']

ans = input("Enter account name : ")
time.sleep(1)

print("Finding the password for it ...")
time.sleep(1)
print(random.choice(Password_list) + " is the password.")

