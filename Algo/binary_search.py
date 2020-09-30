#!/usr/bin/python
# -*-coding:utf-8 -*

def binary_search(x, sorted_list):
    if len(sorted_list) == 1:
        return False
    half = len(sorted_list)//2
    if x == sorted_list[half]:
        return half
    if x < sorted_list[half]:
        return binary_search(x, sorted_list[:half])
    if x > sorted_list[half]:
        return half + binary_search(x, sorted_list[half:])

i = 0
sorted_list = []

while i < 20000:
    sorted_list.append(i)
    i += 1
x = 15897

print(binary_search(x, sorted_list))