#kata

def sort_the_inner_content(words):
    word=words.split()
    newlist=[]
    for i in word:
        
        x=(sorted(i,reverse=True))
        newlist.append("".join(x))
    return print(" ".join(newlist))

sort_the_inner_content("sort the inner content in descending order")
# def sort_str(words):
#     new_words = words.split()
#     return " ".join(sorted(new_words, reverse=True))

# # prints 'Charlie Bob Alice'
# print(sort_str("Charlie Alice Bob"))