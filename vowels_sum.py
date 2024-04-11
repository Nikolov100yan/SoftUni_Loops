text = input()
vowels_sum = 0
for i in range(0, len(text)):
    if text[i] == "a":
        vowels_sum += 1
    elif text[i] == "e":
        vowels_sum += 2
    elif text[i] == "i":
        vowels_sum += 3
    elif text[i] == "o":
        vowels_sum += 4
    elif text[i] == "u":
        vowels_sum += 5
print(vowels_sum)
