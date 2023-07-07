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

def build_huffman_tree(frequency):
    pq = []
    for char, freq in frequency.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(pq, node)

    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = HuffmanNode(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(pq, merged)

    return pq[0]

def build_huffman_codes(root):
    codes = {}
    build_huffman_codes_helper(root, "", codes)
    return codes
