import nltk 
from nltk.book import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.corpus import inaugural
from nltk.stem import PorterStemmer
from collections import Counter
import string

# Assignment 16 ---------------------------------------------------------------------------------------

def cesar(message, d):

    """
    Function takes as an input message - string and shift parameter d. Then it shift every characters
    in given string
    """

    cipher = {}
    for i in range(128):
        cipher[chr(i)] = chr((i+d) % 128)
    cipher = str.maketrans(cipher)
    trans = message.translate(cipher)
    return trans

print(cesar('hn0', 12))        

'''

def cesar1(message, d):
    tab = [ord(x) for x in message]
    crypto = ''
    crypto = crypto.join([chr(x+d) for x in tab])
    return crypto

print(cesar1('hn0',2))

'''

# Assignment 17 ---------------------------------------------------------------------------------------

adress_book = {
    "Jane": "Chicago",
    "Adam": "Warsaw",
    "Dave": "Boston"
}


'''
def add_position(name, adress):
    if name in adress_book.keys():
        raise ValueError("This person has already been asigned to an adress")
    adress_book[name] = adress

def delete_position(name):
    if name in adress_book.keys():
        adress_book.pop(name)
    else:
        raise ValueError("There is no such person in the adress book")
    
def change_adress(name, adress):
    if name in adress_book.keys():
        adress_book[name] = adress
    else:
        raise ValueError("There is no such person in the adress book")
'''

def sort_dict(adress_book):
    sort_dict = sorted(adress_book.items(), key=lambda x:x[1])
    return sort_dict

print(sort_dict(adress_book))
    
# Assignment 19 -----------------------------------------------------------------------------

with open('hound.txt', 'r') as f:
    text = f.read()

def remove(text):

    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tokens = tokenizer.tokenize(text)

    # Join the tokens back into a string without punctuation
    #nopunct_text = ' '.join([token for token in tokens if token.isalnum()])
    nopunct_text = [token for token in tokens if token.isalnum()]

    stop_words = set(stopwords.words('english'))

    no_stopwords = [token for token in nopunct_text if token.lower() not in stop_words]

    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in no_stopwords]

    return stemmed_tokens
    #return ' '.join([token for token in stemmed_tokens])


word_counts = Counter(remove(text))

freq_words = [word for word, count in word_counts.items() if count >= 100]
print("Words occuring at least 100 times in book", freq_words)

'''
with open('hound_nopunct.txt', 'w') as f:
    f.write(nopunct_text)
'''

# Assignment 20 -----------------------------------------------------------------------------

texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
texts = [remove(txt) for txt in texts]

#text7 = brown.words(categories='news')
count7 = texts[6].count('Sunday')

#text9 = inaugural.words()
count9 = texts[8].count('Sunday')

print("Occurences of word 'Sunday' in text 7: ", count7)
print("Occurences of word 'Sunday' in text 9: ", count9)

# Assignment 21 -----------------------------------------------------------------------------

words_text7 = set(texts[6])
words_text9 = set(texts[8])
only9 = words_text9 - words_text7
print("Words in text9 but not in text7: ", only9)

# Assignment 22 -----------------------------------------------------------------------------

words_sets = [set(text) for text in texts]
common_words = set.intersection(*words_sets)
print("Words present in every text (1 to 9): ", common_words)

# Assignment 23 -----------------------------------------------------------------------------

sentences = nltk.sent_tokenize(' '.join(texts[1]))
longest_sentence = max(sentences, key = len)

#sentences_words = [nltk.sent_tokenize(sent) for sent in sentences]
#longest_sentence = max(sentences_words, key=len)
#longest_sentence = " ".join(longest_sentence)

# Find the longest sentence based on the number of words
#longest_sentence = max(sentences, key=lambda sentence: len(nltk.word_tokenize(sentence)))


print("Longest sentence: ", longest_sentence)