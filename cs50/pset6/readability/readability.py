text = input("Text: ")

letters, words, sentences = 0, 1, 0

for i in range(len(text)):
    if text[i].isalpha():
        letters += 1

        if text[i - 1] in [' ', '"']:
            words += 1

        if text[i + 1] in ['.', '!', '?']:
            sentences += 1

L = (letters / words) * 100.0
S = (sentences / words) * 100.0

index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
