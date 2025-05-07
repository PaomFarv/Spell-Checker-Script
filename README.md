# 📝 SpellCheckerApp

Welcome to **SpellCheckerApp**, a simple and colorful Python script that checks spelling mistakes, highlights them, and shows smart suggestions — all in your terminal!

---

## 🚀 Features

- 🔍 Detects misspelled words from user input
- 💡 Displays suggestions using intelligent correction
- 🎨 Highlights errors in red using `colorama`
- ✨ Preserves punctuation while checking only real words
- 📏 Restricts correction distance to make suggestions more accurate
- 🧼 Clears the terminal each time for a fresh look

---

## 🛠️ How to Use

1. Make sure you have Python installed.
2. Install dependencies (just once):
   ```bash
   pip install pyspellchecker colorama
   ```
3. Run the script:
   ```bash
   python spell_checker_app.py
   ```
4. Type a sentence to check, or `q` to quit.

---

## 📦 Example

```
Welcome to the Spell Checker Script!
Please enter the text you want to check (or type 'q' to quit): This iz a sampple text!

Misspelled words: (With Suggestions)
 - iz -> {'is'}
 - sampple -> {'sample'}

Error Marked Text:
This iz sampple text!
```

(Misspelled words will appear in red ✨)

---

## 👤 Coded by

**PaomFarv**

---

## 🧠 Built With

- [pyspellchecker](https://pypi.org/project/pyspellchecker/)
- [colorama](https://pypi.org/project/colorama/)
- `re` for smart text tokenization
