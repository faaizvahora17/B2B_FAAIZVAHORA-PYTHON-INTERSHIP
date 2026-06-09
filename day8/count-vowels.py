word = input("Enter a word: ")
vowel = "aeiouAEIOU"
vowel_count = 0
Non_vowel_count = 0
count=0

for char in word:
    if char.isalpha():
        if char in vowel:
           vowel_count += 1
else:
    Non_vowel_count += 1
print(f"Vowels = {vowel_count}")
print(f"non-vowels:", Non_vowel_count)