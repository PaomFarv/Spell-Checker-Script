from spellchecker import SpellChecker
import os
from colorama import Fore
import re

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

    def error_marked_text(self, text):  
        formatted_text = ""
        for word in text.split():
            if word in self.misspelled_words:
                formatted_text += f"{Fore.RED}{word}{Fore.RESET} "
            else:
                formatted_text += word
            
        print(formatted_text)
        
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
        
        try:
            mod_user_text = "".join(re.findall(r"[A-Za-z ]", user_text))
        except:
            print(Fore.RED + "Please enter only alphabetic characters.")
            continue

        if user_text.lower() == 'q':
            print("Exiting the Spell Checker Script.")
            break

        app.word_checker(mod_user_text)
        print(Fore.GREEN + "\nError Marked Text:" + Fore.RESET)
        app.error_marked_text(mod_user_text)
        print("\nCoded by PaomFarv.\n")
