#!/usr/bin/env python3

def print_fibonacci(length = 0):
    nums = []
    for index in range(length):
        if(index < 2):
            nums.append(index)
        else:
            nums.append(nums[-2] + nums[-1])    
    print(nums)

print_fibonacci(3)