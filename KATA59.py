class Robot:
    def __init__(self):
        self.storage=[]
        #self.storage=['i', 'already', 'know', 'the', 'word', 'thank', 'you', 'for', 'teaching', 'me', 'do', 'not', 'understand', 'input']
        string="I already know the word Thank you for teaching me I do not understand the input"
        for i in string.split(" "):
            if i.lower() not in self.storage:
        
                self.storage.append(i.lower())
            else:
                pass
    
    def learn_word(self,word):
        if word.isalpha():
            if word.lower() in self.storage:
                return f'I already know the word {word}'
            else:
                self.storage.append(word.lower())
                return f'Thank you for teaching me {word}'
        else:
            return f'I do not understand the input'
        


