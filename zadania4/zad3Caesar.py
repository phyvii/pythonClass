def caesar(text, key, alphabet='abcdefghijklmnopqrstuvwxyz'):

    chars = text.lower()

    encrypted = ""

    for char in chars:
        if char not in alphabet:
            encrypted += char
        else:

            index = (alphabet.index(char) + key) % len(alphabet)

            encrypted += alphabet[index]

    return encrypted


message = caesar("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 3,["a","B"])
print(message)