import heapq
import os

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency
    
def count_frequency(message):
    frequency = {}
    for char in message:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1
    return frequency
