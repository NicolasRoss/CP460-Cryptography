#--------------------------
# Nicolas Ross 151703880
# CP460 (Fall 2019)
# Assignment 2
#--------------------------

import math
import string
import utilities_A2

#---------------------------------
#Q1: Vigenere Cipher (Version 2) #
#---------------------------------
#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): string of any length
# Return:       ciphertext (string)
# Description:  Genereic Encryption scheme using Vigenere Cipher
#               calls proper function depending on key length
#               if len(key) == 1 --> call e_vigenere1
#               else --> call e_vigenere2
#               If invalid key (not string or empty string or non-alpha string) -->
#                   print error and return '',''
#---------------------------------------------------------------------------------------
def e_vigenere(plaintext,key):
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (e_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return e_vigenere1(plaintext, key)
    else:
        return e_vigenere2(plaintext, key)

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): string of anylength
# Return:       ciphertext (string)
# Description:  Genereic Encryption scheme using Vigenere Cipher
#               calls proper function depending on key length
#               if len(key) == 1 --> call d_vigenere1
#               else --> call d_vigenere2
#               If invalid key (not string or empty string or contains no alpha char) -->
#                   print error and return '',''
#---------------------------------------------------------------------------------------
def d_vigenere(ciphertext,key):
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (d_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return d_vigenere1(ciphertext,key)
    else:
        return d_vigenere2(ciphertext,key)

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def e_vigenere1(plaintext, key):
    square = utilities_A2.get_vigenereSquare()
    ciphertext = ''

    for char in plaintext:
        if char.lower() in square[0]:
            plainIndx = square[0].index(char.lower())
            keyIndx = square[0].index(key)
            cipherChar = square[keyIndx][plainIndx]
            ciphertext += cipherChar.upper() if char.isupper() else cipherChar
            key = char.lower()

        else:
            ciphertext += char

    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def e_vigenere2(plaintext, key):
    square = utilities_A2.get_vigenereSquare()
    ciphertext = ''
    keyChar = 0

    for char in plaintext:
        if char.lower() in square[0]:
            plainIndx = square[0].index(char.lower())
            keyIndx = square[0].index(key[keyChar % len(key)])
            cipherChar = square[keyIndx][plainIndx]
            ciphertext += cipherChar.upper() if char.isupper() else cipherChar
            keyChar += 1
        
        else:
            ciphertext += char

    return ciphertext
    
#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def d_vigenere1(ciphertext, key):
    square = utilities_A2.get_vigenereSquare()
    plaintext = ''
   
    for char in ciphertext:
        if char.lower() in square[0]:
            keyIndx = square[0].index(key)
            plainIndx = 0
            for i in range(26):
                if square[i][keyIndx] == char.lower():
                    plainIndx = i
                    break
            
            plainChar = square[0][plainIndx]
            key = plainChar
            plaintext += plainChar.upper() if char.isupper() else plainChar

        else:
            plaintext += char

    return plaintext

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def d_vigenere2(ciphertext, key):
    square = utilities_A2.get_vigenereSquare()
    plaintext = ''
    keyChar = 0

    for char in ciphertext:
        if char.lower() in square[0]:
            keyIndx = square[0].index(key[keyChar % len(key)])
            plainIndx = 0

            for i in range(26):
                if square[i][keyIndx] == char.lower():
                    plainIndx = i
                    break
            
            plainChar = square[0][plainIndx]
            plaintext += plainChar.upper() if char.isupper() else plainChar
            keyChar += 1

        else:
            plaintext += char

    return plaintext


#-------------------------------------
#Q2: Vigenere Crytanalysis Utilities #
#-------------------------------------

#-----------------------------------------------------------------------------
# Parameters:   text (string)
#               size (int)
# Return:       list of strings
# Description:  Break a given string into strings of given size
#               Result is provided in a list
#------------------------------------------------------------------------------
def text_to_blocks(text,size):
    blocks = []
    
    for i in range(0, len(text), size):
        blocks.append(text[i:(i + size)])

    return blocks

#-----------------------------------
# Parameters:   text (string)
# Return:       modifiedText (string)
# Description:  Removes all non-alpha characters from the given string
#               Returns a string of only alpha characters upper case
#-----------------------------------
def remove_nonalpha(text):
    return  "".join([char.upper() for char in text if char.isalpha()])

#-------------------------------------------------------------------------------------
# Parameters:   blocks: list of strings
# Return:       baskets: list of strings
# Description:  Assume all blocks have same size = n (other than last block)
#               Create n baskets
#               In basket[i] put character #i from each block
#---------------------------------------------------------------------------------------
def blocks_to_baskets(blocks):
    baskets = [""] * len(blocks[0])

    for block in blocks:
        for i in range(len(block)):
            baskets[i] += block[i]

    return baskets

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       I (float): Index of Coincidence
# Description:  Computes and returns the index of coincidence 
#               for a given text
#----------------------------------------------------------------
def get_indexOfCoin(ciphertext):
    charCount = utilities_A2.get_charCount(ciphertext)
    N = len(ciphertext)
    I = 0

    for count in charCount:
        I = I + ((count * (count - 1)) / (N * (N - 1)))

    return I

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses Friedman's test to compute key length
#               returns key length rounded to nearest integer
#---------------------------------------------------------------
def getKeyL_friedman(ciphertext):
    n = len(ciphertext)
    I = get_indexOfCoin(ciphertext)
    k = math.ceil((0.027 * n) / (((n - 1) * I) + 0.065 - (0.038 * n)))

    return k

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses the Ciphertext Shift method to compute key length
#               Attempts key lengths 1 to 20
#---------------------------------------------------------------
def getKeyL_shift(ciphertext):
    counts = [0] * 21
    for i in range(1, 21):
        s = utilities_A2.shift_string(ciphertext, i, 'r')
        matches = 0
        for j in range(len(s)):
            if ciphertext[j] == s[j]:
                matches += 1
        counts[i] = matches

    maxN = counts[0]
    for num in counts:
        if num > maxN:
            maxN = num 
    print(counts)
    k = counts.index(maxN)
    return k


#---------------------------------
#   Q3:  Block Rotate Cipher     #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   key (b,r)
# Return:       updatedKey (b,r)
# Description:  Assumes given key is in the format of (b(int),r(int))
#               Updates the key in three scenarios:
#               1- The key is too big (use modulo)
#               2- The key is negative
#               if an invalid key is given print error message and return (0,0)
#-----------------------------------------------------------
def adjustKey_blockRotate(key):
    updatedKey = (0, 0)
    if not type(key) == tuple:
        return "Error (adjustedKey_blockRotate): Invalid key{}".format(updatedKey)

    if not type(key[0]) == int or not type(key[1]) == int:
        return "Error (adjustedKey_blockRotate): Invalid key{}".format(updatedKey)

    if key[1] % key[0] < 0:
        return "Error (adjustedKey_blockRotate): Invalid key{}".format(updatedKey)
    
    updatedKey = (key[0], (key[1] % key[0]))

    return updatedKey

#-----------------------------------
# Parameters:   text (string)
# Return:       nonalphaList (2D List)
# Description:  Analyzes a given string
#               Returns a list of non-alpha characters along with their positions
#               Format: [[char1, pos1],[char2,post2],...]
#               Example: get_nonalpha('I have 3 cents.') -->
#                   [[' ', 1], [' ', 6], ['3', 7], [' ', 8], ['.', 14]]
#-----------------------------------
def get_nonalpha(text):
    nonalphaList = []
    for i in range(len(text)):
        if not text[i].isalpha():
            nonalphaList.append([text[i], i])

    return nonalphaList

#-----------------------------------
# Parameters:   text (str)
#               2D list: [[char1,pos1], [char2,pos2],...]
# Return:       modifiedText (string)
# Description:  inserts a list of nonalpha characters in the positions
#-----------------------------------
def insert_nonalpha(text, nonAlpha):
    modifiedText = text

    if len(nonAlpha) > 0:
        for i in range(len(nonAlpha)):
            modifiedText = modifiedText[:nonAlpha[i][1]] + nonAlpha[i][0] + modifiedText[nonAlpha[i][1]:]

    return modifiedText

#-----------------------------------------------------------
# Parameters:   plaintext (string)
#               key (b,r): (int,int)
# Return:       ciphertext (string)
# Description:  break plaintext into blocks of size b
#               rotate each block r times to the left
#-----------------------------------------------------------
def e_blockRotate(plaintext,key):
    nonAlpha = get_nonalpha(plaintext)
    plaintext = "".join([char for char in plaintext if char.isalpha()])
    blocks = text_to_blocks(plaintext, key[0])
    ciphertext = ''

    for _ in range(len(blocks[len(blocks) - 1]), len(blocks[0]), 1):
        blocks[len(blocks) - 1] += 'q'
    
    for block in blocks:
        ciphertext += utilities_A2.shift_string(block, key[1], 'l')
        
    ciphertext = insert_nonalpha(ciphertext, nonAlpha)
    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (string)
#               key (b,r): (int,int)
# Return:       plaintext (string)
# Description:  Decryption using Block Rotate Cipher
#-----------------------------------------------------------
def d_blockRotate(ciphertext,key):
    nonAlpha = get_nonalpha(ciphertext)
    ciphertext = "".join([char for char in ciphertext if char.isalpha()])
    blocks = text_to_blocks(ciphertext, key[0])
    plaintext = ''

    for block in blocks:
        plaintext += utilities_A2.shift_string(block, key[1], 'r')
    
    plaintext = insert_nonalpha(plaintext, nonAlpha)
    index = 0
    for i in range(len(plaintext) - 1, -1, -1):
        if plaintext[i] != 'q':
            index = i
            break
    
    plaintext = plaintext[0:index + 1]
    
    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext (string)
#               b1 (int): starting block size
#               b2 (int): end block size
# Return:       plaintext,key
# Description:  Cryptanalysis of Block Rotate Cipher
#               Returns plaintext and key (r,b)
#               Attempts block sizes from b1 to b2 (inclusive)
#               Prints number of attempts
#-----------------------------------------------------------
def cryptanalysis_blockRotate(ciphertext,b1,b2):
    # your code here
    plaintext = ''
    key = (0, 0)
    attempts = 0
    for blockSize in range(b1, b2):
        for possibleKey in range(1, blockSize):
            text = d_blockRotate(ciphertext, (blockSize, possibleKey))
            if (utilities_A2.is_plaintext(text, 'engmix.txt', 0.9)):
                plaintext = text
                key = (blockSize, possibleKey)
                print("Key found after", attempts + 1, "attempts")
                print("Key = ", key)
                print("Plaintext:", plaintext)

                return plaintext, key
            
            attempts += 1
    print("Block Rotate Cryptanalysis Failed. No key was found")
    return plaintext,key

#---------------------------------
#       Q4: Cipher Detector     #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   ciphertext (string)
# Return:       cipherType (string)
# Description:  Detects the type of a given ciphertext
#               Categories: "Atbash Cipher, Spartan Scytale Cipher,
#                   Polybius Square Cipher, Shfit Cipher, Vigenere Cipher
#                   All other ciphers are classified as Unknown. 
#               If the given ciphertext is empty return 'Empty Ciphertext'
#-----------------------------------------------------------
def get_cipherType(ciphertext):
    # your code here
    return cipherType

#-------------------------------------
#  Q5: Wheastone Playfair Cipher     #
#-------------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (string)
# Return:       modifiedPlain (string)
# Description:  Modify a plaintext through the following criteria
#               1- All non-alpha characters are removed
#               2- Every 'W' is translsated into 'VV' double V
#               3- Convert every double character ## to #X
#               4- if the length of text is odd, add X
#               5- Output is formatted as pairs, separated by space
#                   all upper case
#-----------------------------------------------------------
def formatInput_playfair(plaintext):
    modifiedPlain = ''
    plaintext = remove_nonalpha(plaintext)
    n = len(plaintext)
    i = 0

    while i < n:
        if (plaintext[i] == "W"):
            plaintext = plaintext[:i] + "VV" + plaintext[i + 1:]
            n += 1
        i += 1

    if len(plaintext) % 2 > 0:
        plaintext += 'X'
    
    for i in range(len(plaintext)):
        if i % 2 == 0 and i != 0:
            modifiedPlain += ' '
            modifiedPlain += plaintext[i]
        
        else:
            modifiedPlain += plaintext[i]
    
    for i in range(len(modifiedPlain)):
        if i != 0:
            if modifiedPlain[i - 1] == modifiedPlain[i]:
                modifiedPlain = modifiedPlain[:i] + 'X' + modifiedPlain[i + 1:]
        
    return modifiedPlain

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Encryption using Wheatstone Playfair Cipher
#---------------------------------------------------------------------------------------
def e_playfair(plaintext, key):
    ciphertext = ''
    text = formatInput_playfair(plaintext)
    nonAlpha = get_nonalpha(text)
    textList = text.split()
    xA, yA = 0, 0
    xB, yB = 0, 0

    for e in textList:
        for i in range(len(key)):
            for j in range(len(key[0])):
                if key[i][j] == e[0]:
                    xA = j
                    yA = i
                
                if key[i][j] == e[1]:
                    xB = j
                    yB = i
        
        if yA == yB:
            if xA == (len(key) - 1):
                xA = -1

            if xB == (len(key) - 1):
                xB = -1
            
            ciphertext = ciphertext + key[yA][xA + 1] + key[yB][xB + 1]
        
        elif xA == xB:
            if yA == (len(key[0]) - 1):
                yA = -1
            
            if yB == (len(key[0]) - 1):
                yB = -1

            ciphertext = ciphertext + key[yA + 1][xA] +key[yB + 1][xB]
        
        else:
            ciphertext = ciphertext + key[yA][xB] + key[yB][xA]

    ciphertext = insert_nonalpha(ciphertext, nonAlpha)
    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Decryption using Wheatstone Playfair Cipher
#-------------------------------------------------------------------------------
def d_playfair(ciphertext, key):
    plaintext = ''
    text = formatInput_playfair(ciphertext)
    nonAlpha = get_nonalpha(text)
    textList = text.split()
    xA, yA = 0, 0
    xB, yB = 0, 0
    
    for e in textList:
        for i in range(len(key)):
            for j in range(len(key[0])):
                if key[i][j] == e[0]:
                    xA = j
                    yA = i
                
                if key[i][j] == e[1]:
                    xB = j
                    yB = i
        
        if yA == yB:
            if xA == 0:
                xA = len(key)

            if xB == 0:
                xB = len(key)
            
            plaintext = plaintext + key[yA][xA - 1] + key[yB][xB - 1]
        
        elif xA == xB:
            if yA == 0:
                yA = len(key[0])
            
            if yB == 0:
                yB = len(key[0])

            plaintext = plaintext + key[yA - 1][xA] + key[yB - 1][xB]
        
        else:
            plaintext = plaintext + key[yA][xB] + key[yB][xA]

    plaintext = insert_nonalpha(plaintext, nonAlpha)
    return plaintext

