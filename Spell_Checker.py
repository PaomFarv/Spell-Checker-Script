from spellchecker import SpellChecker
import os
from colorama import Fore

class SpellCheckerApp():
    def __init__(self):
        self.spell_checker = SpellChecker()
    
    def word_checker(self,text):
        user_spelled_words = text.split()
        
        self.misspelled_words = self.spell_checker.unknown(user_spelled_words)
        
        if self.misspelled_words:
            print(Fore.RED + "\nMisspelled words:")
            for word in self.misspelled_words:
                print(f" - {word}")
        else:
            print(Fore.GREEN + "No misspelled words found.")

    def correct_text(self, text):  
        error_text = []
        for word in text.split():
            if word in self.misspelled_words:
                error_text.append(Fore.RED + word)
            else:
                error_text.append(word)
        print(Fore.WHITE + ' '.join(error_text))
        
def clear_terminal(): 
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

clear_terminal()

app = SpellCheckerApp()

if __name__ == "__main__":
    while True:
        print(Fore.WHITE + "\nWelcome to the Spell Checker Script!")

        user_text = input("Please enter the text you want to check (or type 'q' to quit): ")
        mod_user_text = user_text.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace('"', "")
        if not mod_user_text.isalpha():
            print(Fore.RED + "Please enter only alphabetic characters.")
            continue

        if user_text.lower() == 'q':
            print("Exiting the Spell Checker Script.")
            break

        app.word_checker(user_text)
        print(Fore.GREEN + "\nCorrected text:")
        app.correct_text(user_text)
        print("\nCoded by PaomFarv.\n")
