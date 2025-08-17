#semicode of kata
import collections
def top_3_words(text):
    words = text.split()
    counter = collections.Counter(words)
    x=counter.most_common(3)
top_3_words()