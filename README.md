# ELFG-LANGUAGE

					Description
The ELFG Language Generator is a Python-based tool designed to create a unique language (conlang) named ELFG, which blends elements from English, French, Italian, and Georgian. This project leverages the `googletrans` Python library for translating English words into the other three languages. The key feature of this tool is its ability to generate novel words based on the translated words, forming the basis of the ELFG language. 

				Installation Requirements
 
1. To run the ELFG language generator you will need to have Python installed on your system. 
2. Create a new folder
3. Copy past the code (main.py) with the 4 text file provided in the folder
<img width="217" alt="Screenshot 2024-01-28 at 16 57 54" src="https://github.com/Oto0398/ELFG-LANGUAGE/assets/149970372/6aa8f79c-8f5c-4a92-a481-868be1a2f9ce">

5. Create a new python environment for this folder
6. Install the needed modules: 
`os`, `json`, `collections.defaultdict`, `random`, and `pathlib.Path`.
7. AND install specific version of `googletrans` library: 
pip install googletrans==3.1.0.a0


					Usage

To use the ELFG Language Generator, follow these steps:

*make sure to have internet connection before running the code*
1. Run the script main.py using Python:

2. If you want more translation, you have to add sentences or words in the differents text files using the correct languages then rerun the code 

					Output

**The three outputs that you will get after running the code:**

1. A JSON file containing the English words and their translations into French, Italian and Georgian.
<img width="241" alt="Screenshot 2024-01-28 at 17 07 19" src="https://github.com/Oto0398/ELFG-LANGUAGE/assets/149970372/bcde3840-f622-4d82-ba9e-e2eb06676542">

2. A JSON file with the identical content plus the translation of the word in the ELFG language

<img width="298" alt="Screenshot 2024-01-28 at 17 07 47" src="https://github.com/Oto0398/ELFG-LANGUAGE/assets/149970372/d0a6de8a-0e2e-47ed-8890-8818a9d8841a">

3. A .txt file of the sentences translated into ELFG.

<img width="386" alt="Screenshot 2024-01-28 at 17 15 00" src="https://github.com/Oto0398/ELFG-LANGUAGE/assets/149970372/3b92acdc-67d5-431a-bc6f-912955b69146">

				Version 2.0 of the Code

The idea for the second version of the code is the same, except for the fact that it only uses the English text file and simlpy creates a list of words for this one.

The important change is that the code will ask the user if they wish to add a new sentence to the text file with a yes or no question to which one should answer with "1" for a yes and "2" for a no.

The system is a loop, therefore it will keep asking the question untill responded with a no:

<img width="1107" alt="Screenshot 2024-01-28 at 17 09 40" src="https://github.com/Oto0398/ELFG-LANGUAGE/assets/149970372/dc819ea7-c117-4878-844b-f7fc0eff6c41">



Every time you add new sentences/words in the texts files you are going to get the new words translation in ELFG at the end of the json file, if you delete the Json files, then you will get others translation of ELFG. 
Then the code is going to provide also a new text file that contains the translation of our texts files in the new ELFG languages, again if the dictionary is deleted then the new file will give other sentences.   




