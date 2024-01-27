#2023/2024 Project -Generator of ELFG Language- by Kassandra Briola, Samuele Antonelli, Otari Tchigladze

#import the needed libraries
import os
import json
from collections import defaultdict
import random
from googletrans import Translator
from pathlib import Path


# --------------------- PART I Get translation from files and create dictionary stored into Json file----------------------------------

"""
FUNCTION
"""

#function that open, reads text files 
#return a list of unique words and put every letter in lower cases
def read_file(file_name):
    with open(file_name, "r") as f:
        text = f.read()
    return list(set(text.lower().split()))

#function that translate a word from the source language to the target language
#by creating a instance"Translator" class form googletrans library
#and return a list of translated words
def get_translations(word, src_lang, tgt_lang):
    translator = Translator()
    try:
        translations = translator.translate([word], src=src_lang, dest=tgt_lang)
        return [translation.text for translation in translations]
    except:
        return []

"""
SCRIPT
"""

#reads the English, French, Italian, and Georgian text files
english_words = read_file("eng.txt")
french_words = read_file("fre.txt")
italian_words = read_file("ita.txt")
georgian_words = read_file("geo.txt")

# prints the the list of unique words for each language
print("English words:", english_words)
print("French words:", french_words)
print("Italian words:", italian_words)
print("Georgian words:", georgian_words)

#initializes a defaultdict called translations to store the translations.
translations = defaultdict(lambda: defaultdict(list))

# Load existing translations from a JSON file if it exists
if os.path.exists('translations.json'):
    with open('translations.json', 'r') as json_file:
        translations = json.load(json_file)

# Create or update the dictionary with the four translations for each English word list
    #loop that iterates through list of languages
    #checks if current language is not already a key in the dictionary for the current English word if no execute the 'if' block
    # Convert translations to lower case
for english_word in english_words:
    if english_word not in translations: 
        translations[english_word] = {}
    for language in ['english','french', 'italian', 'georgian']:
        if language not in translations[english_word]:
            translations[english_word][language] = get_translations(english_word, 'english', language)
            translations[english_word][language] = [translation.lower() for translation in translations[english_word][language]]


# Convert the dictionary into a JSON string and write it to a file
with open('translations.json', 'w') as json_file:
    json.dump(translations, json_file, ensure_ascii=False, indent=4)


# --------------------- PART II Create New words in ELFG and new dictionary  ----------------------------------
"""
FUNCTION
"""

#function that generates a word in ELFG based on a set of unique characters and an average word length.
def generate_elfg_word(unique_chars: set[str], avg_length: int) -> str:
    alphabet = sorted(list(unique_chars))
    target_length = avg_length if avg_length % 2 == 0 else avg_length - 1  # Ensure even length for ELFG word
    return ''.join(random.choice(alphabet) for _ in range(target_length))


#function that create or updates dictionary with a new ELFG word for the given English word
#initializes an empty set to store the unique characters in the translations of the English word.
#generates a new ELFG word using the generate_elfg_word function and the set of unique characters
#add new entry to the elfg dictionary for the given English word
def update_elfg_translations(elfg_translations: dict, english_word: str, word_translations: dict, avg_length: int) -> dict:
    if english_word in elfg_translations:
        return elfg_translations
   
    unique_chars = set()
    for language, translations_list in word_translations.items():
        unique_chars.update(set("".join(translations_list)))

    elfg_word = generate_elfg_word(unique_chars, avg_length)
    elfg_translations[english_word] = {"translations": word_translations, "elfg": elfg_word}
    return elfg_translations

"""
SCRIPT
"""

#Check if the ELFG translations file exists
#If not initialize an empty dictionary
if os.path.exists('elfg_translations.json'):
    with open('elfg_translations.json', 'r') as json_file:
        elfg_translations = json.load(json_file)
else:
    elfg_translations = {}


# Calculate the average length of the four translations and generate the ELFG word
    #create new dictionary that contains ELFG translations for each English word in the translations dictionary
    #generates a new ELFG word for each English word based on the unique characters and average length of its translations
    #Check if the word ELFG is already in the dictionary or not to avoid replacement
elfg_translations_new = {}
for english_word, word_translations in translations.items():
    lengths = []
    unique_chars = set()

    for language, translations_list in word_translations.items():
        lengths.extend([len(translation) for translation in translations_list])
        unique_chars.update(set(''.join(translations_list)))

    avg_length = round(sum(lengths) / len(lengths))

    if english_word not in elfg_translations:
        elfg_word = generate_elfg_word(unique_chars, avg_length)
        elfg_translations_new[english_word] = {"translations": word_translations, "elfg": elfg_word}
    elif elfg_translations[english_word]["translations"] != word_translations:
        elfg_word = generate_elfg_word(unique_chars, avg_length)
        elfg_translations_new[english_word] = {"translations": word_translations, "elfg": elfg_word}
    else:
        elfg_translations_new[english_word] = elfg_translations[english_word]

# create or save the updated ELFG translations to a JSON file 
if elfg_translations_new != elfg_translations:
    with open('elfg_translations.json', 'w') as json_file:
        json.dump(elfg_translations_new, json_file, ensure_ascii=False, indent=4)


# --------------------- PART III Create New text file in ELFG ----------------------------------
"""
FUNCTION
"""

#opens the file, and loads the JSON content into a Python dictionary.
def load_elfg_translations(file_path: str) -> dict:
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

#Function that checks if the English word exists in the dictionary and returns its ELFG translation
def get_elfg_translation(english_word: str, elfg_translations: dict) -> str:
    if english_word in elfg_translations:
        return elfg_translations[english_word]['elfg']
    else:
        return ''


##Function that splits the English text into lines then into words.
#For each word, retrieves the ELFG translation and joins the translated words back into a line.
#joins the translated lines back into a single string and returns it.
def translate_text_to_elfg(english_text: str, elfg_translations: dict) -> str:
    lines = english_text.split('\n')
    elfg_lines = []
    for line in lines:
        elfg_words = [get_elfg_translation(word, elfg_translations) for word in line.split()]
        elfg_lines.append(' '.join(elfg_words))
    return '\n'.join(elfg_lines)

#Function that opens the file in write mode and writes the ELFG text to it.
def write_elfg_text_to_file(elfg_text: str, file_path: str):
    with open(file_path, 'w') as text_file:
        text_file.write(elfg_text)

"""
SCRIPT
"""

#checks if the script is being run directly or imported as a module. If it is, block will be executed.
if __name__ == '__main__':
    # Load the ELFG translations from the JSON file
    elfg_translations = load_elfg_translations('elfg_translations.json')

    # Read the English text from a file
    english_text = ''
    with open('eng.txt', 'r') as text_file:
        english_text = text_file.read()

    # Translate the English text to ELFG
    elfg_text = translate_text_to_elfg(english_text, elfg_translations)

    # Write the ELFG text to a file
    write_elfg_text_to_file(elfg_text, 'elfg_text.txt')
