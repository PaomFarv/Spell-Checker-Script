from spellchecker import SpellChecker


class SpellCheckerApp():
    def __init__(self):
        self.spell_checker = SpellChecker()
    
    def user_text(self,text):
        user_spelled_words = text.split()
        self.misspelled_words = self.spell_checker.unknown(user_spelled_words)
        
        if self.misspelled_words:
            print("Misspelled words:")
            for word in self.misspelled_words:
                print(f" - {word}")
        else:
            print("No misspelled words found.")

    def correct_text(self, text):
        corrected_text = []
        for word in text.split():
            if word in self.misspelled_words:
                corrected_word = self.spell_checker.correction(word)
                corrected_text.append(corrected_word)
            else:
                corrected_text.append(word)
        print(' '.join(corrected_text))
        

app = SpellCheckerApp()

if __name__ == "__main__":
    app.user_text("This is a smaple text with some erors.")
    app.correct_text("This is a smaple text with some erors.")
    print("\nCoded by PaomFarv.\n")