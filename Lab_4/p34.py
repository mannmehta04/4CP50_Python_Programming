def count_vowels(string):
    vowels = 'aeiou'
    return {v: string.lower().count(v) for v in vowels}

print("Vowel counts in the string:")
for vowel, count in count_vowels("testing message").items():
    print(f"{vowel}: {count}")