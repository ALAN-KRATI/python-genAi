def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    return " ".join(reversed_words)

print(reverse_words("Hello Python Developer"))