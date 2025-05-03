from spellchecker import SpellChecker
import os

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
        
def clear_terminal(): 
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

clear_terminal()

app = SpellCheckerApp()

if __name__ == "__main__":
    while True:
        print("\nWelcome to the Spell Checker Script!")

        user_text = input("Please enter the text you want to check (or type 'q' to quit): ")
        if user_text.lower() == 'q':
            print("Exiting the Spell Checker Script.")
            break

        app.user_text(user_text)
        print("\nCorrected text:")
        app.correct_text(user_text)
        print("\nCoded by PaomFarv.\n")
