#voting machine using dictionaries
votedList={}
def votingEntry(name):
    if votedList.get(name):
        print("access denied")
    else:
        votedList[name]=True
        print("you can vote")
votingEntry("mike")
votingEntry("mike")
votingEntry("dave")
