def get_vowels_numbers(wordenter):
    nb_vowels = 0
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            nb_vowels += 1
    return nb_vowels
wordenter = input("Enter A Number")
vowels_count = get_vowels_numbers(word)
print("There Are ", vowels_count, "Number Of Vowels In The Word ", wordenter)
