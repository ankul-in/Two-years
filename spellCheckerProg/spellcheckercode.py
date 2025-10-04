#https://youtu.be/2SSr-RVAwIg


from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell=SpellChecker()

    def correct_text(self,text):
        words=text.split()
        corrected_words=[]
        for word in words:
            corrected=self.spell.correction(word)
            if corrected!=word.lower():
                print(f'"correcting"{word}" to "{corrected}')
                corrected_words.append(corrected)
        return "".join(corrected_words)
    
    def run(self):
        print("--spellChecker--\nEnter:exit to close program")
        while True:
            text=input("enter text----->")
            if text.lower()=="exit":
                print("closing program")
                break
            corrected_text=self.correct_text(text)
            print(f"corrected Text:{corrected_text}")

if __name__=="__main__":
    SpellCheckerApp().run()

