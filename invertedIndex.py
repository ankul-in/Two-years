#implementing inverted index
#search engine
document1="the quick brown fox jumped over the lazy dog"
document2="the lazy dog slept in the sun"
tokens1=document1.lower().split()
tokens2=document2.lower().split()
terms=list(set(tokens1+tokens2))
inverted_index={}
for i in terms:
    documents=[]
    if i in tokens1:
        documents.append("Document 1")
    if i in tokens2:
        documents.append("Document 2")
    inverted_index[i]=documents
for i,documents in inverted_index.items():
    print(i,"-->",", ".join(documents))