import string

def count_words(text):
    cleaned_text = ''.join(char if char.isalpha() or char.isspace() else ' ' for char in text)

    words = cleaned_text.lower().split()

    return {word: len(word) for word in words}

def main():
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    result = count_words(text)
    print(result)

main()