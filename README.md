# ELFG-LANGUAGE

					Description
The ELFG Language Generator is a Python-based tool designed to create a unique language (conlang) named ELFG, which blends elements from English, French, Italian, and Georgian. This project leverages the `googletrans` Python library for translating English words into the other three languages. The key feature of this tool is its ability to generate novel words based on the translated words, forming the basis of the ELFG language. 

				Installation Requirements
 
1. To run the ELFG language generator you will need to have Python installed on your system. 
2. Create a new folder
3. copy past the code (main.py) with the 4 text file provided in the folder
4. Create a new python environment for this folder
5. Install the needed modules: 
`os`, `json`, `collections.defaultdict`, `random`, and `pathlib.Path`.
6. AND install specific version of `googletrans` library: 
pip install googletrans==3.1.0.a0


					Usage

To use the ELFG Language Generator, follow these steps:

*make sure to have internet connection before running the code*
1. Run the script main.py using Python:

2. if you want more translation, you have to add sentences or words in the differents text files using the correct languages then rerun the code 

					Output
The code is going to create 2 differents Json files, one that contains for every English word the 4 matching words for English, French, Italian and Georgian and another one that contains the same things plus the new words translation in ELFG.
Every time you add new sentences/words in the texts files you are going to get the new words translation in ELFG at the end of the json file, if you delete the Json files, then you will get others translation of ELFG. 
Then the code is going to provide also a new text file that contains the translation of our texts files in the new ELFG languages, again if the dictionary is deleted then the new file will give other sentences.   




