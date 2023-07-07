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

def build_huffman_codes_helper(node, code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = code
    build_huffman_codes_helper(node.left, code + "0", codes)
    build_huffman_codes_helper(node.right, code + "1", codes)

def save_huffman_codes(huffman_codes, output_file):
    with open(output_file, "w") as file:
        for char, code in huffman_codes.items():
            file.write(f"{char}:{code}\n")

def compress(message, output_file, codes_file):
    frequency = count_frequency(message)
    huffman_tree = build_huffman_tree(frequency)
    huffman_codes = build_huffman_codes(huffman_tree)

