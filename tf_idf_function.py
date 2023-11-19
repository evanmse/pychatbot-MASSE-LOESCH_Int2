import math
import os

directory = "./speeches"

def score_TF(strings_chain):  # Function that associates to each word how many times it appeared in a strings_chaine

    dictionnary = {}
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" #A string that contains all the punctuations
    mylist_words = []

    for caracter in strings_chain:
        if caracter not in punctuations:
            mylist_words.append(caracter)       #Append to mylist_words all the caracters that are not punctuations
        else:
            mylist_words.append(' ')            #Replace all the punctuations by space

    str_chain_no_punctuations = ''.join(mylist_words)
    list_chain_no_punctuations = str_chain_no_punctuations.split(" ")

    for i in range(list_chain_no_punctuations.count("")):   #Remove all the "" in the list
        list_chain_no_punctuations.remove("")

    for k in range(list_chain_no_punctuations.count("\n")):     #Remove all the "\n" in the list
        list_chain_no_punctuations.remove("\n")

    for j in range(len(list_chain_no_punctuations)):    #Remove "\n" in the each word of the list
        if "\n" in list_chain_no_punctuations[j]:
            list_chain_no_punctuations[j] = list_chain_no_punctuations[j].replace("\n", "")

    list_unique_word = list(set(list_chain_no_punctuations))

    for word in list_unique_word:
        dictionnary[word] = list_chain_no_punctuations.count(word)   #Create the dictionnary

    return dictionnary

def score_IDF(directory):

    files_name = os.listdir(directory)
    dictionnary_IDF = {}

    for file in files_name[1:]:

        full_path = os.path.join('./speeches', file)

        with open(full_path, 'r', encoding='utf-8') as f:

            content = f.read()
            print(score_TF(content))

print(score_TF("\noui j'aime les am\nis"))

