import re

sentence = """A, very   very; irregular_sentence"""

words = re.split(r'[\s,;_]+', sentence)

print(" ".join(words))