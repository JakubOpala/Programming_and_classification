import string

# Assignment 16 ---------------------------------------------------------------------------------------

def cesar(message, d):

    """
    Function takes as an input message - string and shift parameter d. Then it shifts the number representing
    position in ASCII table for every character in given string by d. Then it returns a string with every character
    from the original string replaced by a character corresponding to that number (modulo 128 - size of basic ASCII table).

    Parameters:
            message(String): text for encryption/decryption
            d(Int): shift parameter

    Return:
            trans(String): text after encryption/decryption

    Conditions:
            string for encryption should contain only characters from the standard ASCII table
    """

    cipher = {}

    for i in range(128):
        cipher[chr(i)] = chr((i+d) % 128)

    cipher = str.maketrans(cipher)
    trans = message.translate(cipher)

    return trans

# Assignment 17 ---------------------------------------------------------------------------------------

def sort_dict(names, adresses):

    """
    Functions takes as an input two arrays of the same length, and creates a dictionary that to every cell
    names[i] assigns a cell adresses[i]. Then it sorts this dictionary in ascending order by the adresses.

    Parameters:
            names(Array[Any]): array of names (keys) for the adress book
            adresses(Array[Any]): array of adresses (values) for the adress book

    Return:
            sort_dict(dict): dictinary that for every name assigns an adress

    Conditions:
            there can't be any duplicated elements in the names array
    """

    if (len(set(names)) != len(names)):
        raise ValueError

    if (len(names) !=  len(adresses)):
        raise ValueError

    adress_book = {x: y for x, y in zip(names, adresses)}

    sort_dict = dict(sorted(adress_book.items(), key=lambda x:x[1]))
    return sort_dict

#print(sort_dict(adress_book))