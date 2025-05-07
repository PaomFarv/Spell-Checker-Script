from spellchecker import SpellChecker
import os
from colorama import Fore
import re

class SpellCheckerApp():
    def __init__(self):
        self.spell_checker = SpellChecker()
        self.spell_checker.distance = 1

    def word_checker(self, words):
        misspelled = self.spell_checker.unknown([w for w in words if w.isalpha()])
        
        if misspelled:
            print(Fore.RED + f"\nMisspelled words: {Fore.GREEN}(With Suggestions){Fore.RED}")
            for word in misspelled:
                print(f" - {word} -> {self.spell_checker.candidates(word)}")
        else:
            print(Fore.GREEN + "No misspelled words found.")
        
        return misspelled

    def error_marked_text(self, words, misspelled):
        formatted_text = ""
        for word in words:
            if word in misspelled:
                formatted_text += f"{Fore.RED}{word}{Fore.RESET} "
            else:
                formatted_text += f"{word} "
        print(formatted_text)

def clear_terminal(): 
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

app = SpellCheckerApp()

if __name__ == "__main__":
    while True:
        print(Fore.WHITE + "\nWelcome to the Spell Checker Script!")

        user_input = input("Please enter the text you want to check (or type 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Exiting the Spell Checker Script.")
            break

        try:
            # Keeps words and punctuation
            words = re.findall(r"\w+|[^\w\s]", user_input)
        except:
            print(Fore.RED + "Please enter valid text.")
            continue

        misspelled = app.word_checker(words)
        print(Fore.GREEN + "\nError Marked Text:" + Fore.RESET)
        app.error_marked_text(words, misspelled)
        print("\nCoded by PaomFarv.\n")
