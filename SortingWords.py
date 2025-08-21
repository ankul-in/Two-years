#this sorts words in string


def sort_str(words):
    new_words = words.split()
    return " ".join(sorted(new_words, reverse=True))

# prints 'Charlie Bob Alice'
print(sort_str("Charlie Alice Bob"))