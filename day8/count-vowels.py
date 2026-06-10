word = input("Enter a word: ")
vowel = "aeiouAEIOU"
Non_vowel = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWYZ"
vowel_count = 0
Non_vowel_count = 0
count=0

for char in word:
    if char.isalpha():
        if char in vowel:
           vowel_count += 1

for let in word:
     if let.isalpha():
        if let in Non_vowel:
            Non_vowel_count += 1

    
print(f"Vowels = {vowel_count}")
print(f"Non-vowels = {Non_vowel_count}")