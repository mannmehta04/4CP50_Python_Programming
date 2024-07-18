text = "The quick brown fox jumps over the lazy dog."

words = text.split()

sorted_words = sorted(words)

sorted_text = ' '.join(sorted_words)

print(sorted_text)