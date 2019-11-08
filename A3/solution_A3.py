#--------------------------
# Nicolas Ross 151703880 Your Name and ID   <--------------------- Change this -----
# CP460 (Fall 2019)
# Assignment 3
#--------------------------

import math
import string
import utilities_A3

#---------------------------------
#  Q1: Columnar Transposition    #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   key (string)           
# Return:       keyOrder (list)
# Description:  checks if given key is a valid columnar transposition key 
#               Returns key order, e.g. [face] --> [1,2,3,0]
#               Removes repititions and non-alpha characters from key
#               If empty string or not a string -->
#                   print an error msg and return [0] (which is a)
#               Upper 'A' and lower 'a' are the same order
#-----------------------------------------------------------
def get_keyOrder_columnarTrans(key):
    keyOrder = []
    visited = []
    if type(key) != str:
        keyOrder.append(0)
        return "Error: Columar Transposition Key " + str(keyOrder)
    
    elif len(key) == 0:
        keyOrder.append(0)
        return "Error: Columar Transposition Key " + str(keyOrder)

    elif all(x.isalpha() or x.isspace() for x in key):
        key = key.lower()
        for char in key:
            if char.lower() not in visited and char.isalpha():
                visited.append(char)

        key = "".join(visited)
        visited = sorted(visited)
        for char in visited:
            keyOrder.append(key.index(char))
    
    else:
        keyOrder.append(0)
        return "Error: Columar Transposition Key " + str(keyOrder)

    return keyOrder

#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               kye (str)
# Return:       ciphertext (list)
# Description:  Encryption using Columnar Transposition Cipher
#-----------------------------------------------------------
def e_columnarTrans(plaintext,key):
    keyOrder = get_keyOrder_columnarTrans(key)
    c = len(keyOrder)
    r = math.ceil(len(plaintext) / c)
    cipherMatrix = utilities_A3.new_matrix(r, c, "")
    counter = 0

    for i in range(r):
        for j in range(c):
            cipherMatrix[i][j] = plaintext[counter] if counter < len(plaintext) else 'q'
            counter += 1

    ciphertext = ''
    for index in keyOrder:
        for i in range(r):
            ciphertext += cipherMatrix[i][index]

    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               kye (str)
# Return:       plaintext (list)
# Description:  Decryption using Columnar Transposition Cipher
#-----------------------------------------------------------
def d_columnarTrans(ciphertext,key):
    keyOrder = get_keyOrder_columnarTrans(key)
    c = len(keyOrder)
    r = math.ceil(len(ciphertext) / c)
    cipherMatrix = utilities_A3.new_matrix(r, c, "")
    counter = 0

    for index in keyOrder:
        for i in range(r):
            cipherMatrix[i][index] = ciphertext[counter]
            counter += 1
    
    plaintext = ''
    for i in range(r):
        for j in range(c):
            plaintext += cipherMatrix[i][j]

    while plaintext[len(plaintext) - 1] == 'q':
        plaintext = plaintext[:-1]

    return plaintext


#---------------------------------
#   Q2: Permutation Cipher       #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key(key,mode)
# Return:       ciphertext (str)
# Description:  Encryption using permutation cipher
#               mode 0: stream cipher --> columnar transposition
#               mode 1: block cipher --> block permutation
#               a padding of 'q' is to be used whenever necessary
#-----------------------------------------------------------
def e_permutation(plaintext,key):
    ciphertext = ''
    tmpKey = key[0]
    newKey = ''

    if key[1] == 0:
        for i in range(len(tmpKey)):
            newKey += chr(ord(tmpKey[i]) + 65)
        
        ciphertext = e_columnarTrans(plaintext, newKey)

    elif key[1] == 1:
        newKey = str(tmpKey)
        blocks = utilities_A3.text_to_blocks(plaintext, len(newKey))

        while len(blocks[-1]) != len(newKey):
            blocks[-1] += 'q'
        
        for block in blocks:
            for i in range(len(newKey)):
                ciphertext += block[int(newKey[i]) - 1]
    else:
        print("Error (e_permutation): invalid mode")

    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key(key,mode)
# Return:       plaintext (str)
# Description:  Decryption using permutation cipher
#               mode 0: stream cipher --> columnar transposition
#               mode 1: block cipher --> block permutation
#               a padding of 'q' is to be removed
#-----------------------------------------------------------
def d_permutation(ciphertext,key):
    plaintext = ''
    tmpKey = key[0]
    newKey = ''

    if key[1] == 0:
        for i in range(len(tmpKey)):
            newKey += chr(ord(tmpKey[i]) + 65)

        plaintext = d_columnarTrans(ciphertext, newKey)

    elif key[1] == 1:
        newKey = str(tmpKey)
        blocks = utilities_A3.text_to_blocks(ciphertext, len(newKey))

        for block in blocks:
            for i in range(len(newKey)):
                plaintext += block[newKey.index(str(i + 1))]
    else:
        print("Error (e_permutation): invalid mode")

    return plaintext

#---------------------------------
#       Q3: ADFGVX Cipher        #
#---------------------------------
#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using ADFGVX cipher
#--------------------------------------------------------------
def e_adfgvx(plaintext, key):
    square = utilities_A3.get_adfgvx_square()
    adfgvx = 'adfgvx'
    tmpCipher = ''

    for char in plaintext:
        index2D = utilities_A3.index_matrix(char.upper(), square)
        
        if char.isalpha():
            for index in index2D:
                if char.isupper():
                    tmpCipher += adfgvx[index].upper()
                
                else:
                    tmpCipher += adfgvx[index]
        else:
            tmpCipher += char

    ciphertext = e_columnarTrans(tmpCipher, key)
    return ciphertext

#--------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using ADFGVX cipher
#--------------------------------------------------------------
def d_adfgvx(ciphertext, key):
    square = utilities_A3.get_adfgvx_square()
    adfgvx = 'adfgvx'
    plaintext = ''

    tmpPlain = d_columnarTrans(ciphertext, key)
    i = 0
    while i < len(tmpPlain):
        index2D = [0, 0]
        if tmpPlain[i].isalpha():
            index2D[0] = adfgvx.index(tmpPlain[i].lower())
            index2D[1] = adfgvx.index(tmpPlain[i + 1].lower())
            if(tmpPlain[i].isupper()):
                plaintext += square[index2D[0]][index2D[1]]
            
            else:
                plaintext += square[index2D[0]][index2D[1]].lower()
            i += 2

        else:
            plaintext += tmpPlain[i]
            i += 1
            
    return plaintext

#---------------------------------
#       Q4: One Time Pad         #
#---------------------------------
#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using One Time Pad
#               Result is shifted by 32
#--------------------------------------------------------------
def e_otp(plaintext,key):
    ciphertext = ''
    for i in range(len(key)):
        ciphertext += chr(ord(xor_otp(plaintext[i], key[i])) + 32)

    return ciphertext

#--------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using One Time Pad
#               Input is shifted by 32
#--------------------------------------------------------------
def d_otp(ciphertext,key):
    plaintext = ''
    for i in range(len(key)):
        plaintext += xor_otp(chr(ord(ciphertext[i]) - 32), key[i])
        
    return plaintext
#--------------------------------------------------------------
# Parameters:   char1 (str)
#               char2 (str)
# Return:       result (str)
# Description:  Takes two characters. Convert their corresponding
#               ASCII value into binary (8-bits), then performs xor
#               operation. The result is treated as an ASCII value
#               which is converted to a character
#--------------------------------------------------------------
def xor_otp(char1,char2):
    return chr(ord(char1) ^ ord(char2))

#---------------------------------
#    Q5: Myszkowski Cipher      #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   key (string)           
# Return:       keyOrder (list)
# Description:  checks if given key is a valid Myszkowski key 
#               Returns key order, e.g. [meeting] --> [3,0,0,5,2,4,1]
#               The key should have some characters that are repeated
#               and some characters that are non-repeated. 
#               if invalid key --> return [1,1,0]
#               Upper and lower case characters are considered of same order
#               non-alpha characters sould be ignored
#-----------------------------------------------------------
def get_keyOrder_myszkowski(key):
    keyOrder = []
    visited = []
    if type(key) != str:
        keyOrder = [1, 1, 0]
        return "Error: Columar Transposition Key " + str(keyOrder)
    
    elif len(key) == 0:
        keyOrder = [1, 1, 0]
        return "Error: Columar Transposition Key " + str(keyOrder)

    else:
        key = key.lower()
        for char in key:
            if char.lower() not in visited and char.isalpha():
                visited.append(char)

        if len(visited) < 2 or len(visited) == len(key):
            keyOrder = [1, 1, 0]
            return "Error: Columar Transposition Key " + str(keyOrder)

        visited = sorted(visited)
        for char in key:
            if char.isalpha():
                 keyOrder.append(visited.index(char))

    return keyOrder

#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using Myszkowsi Transposition
#--------------------------------------------------------------
def e_myszkowski(plaintext,key):
    keyOrder = get_keyOrder_myszkowski(key)
    c = len(keyOrder)
    r = math.ceil(len(plaintext) / c)
    cipherMatrix = utilities_A3.new_matrix(r, c, "")
    counter = 0

    for i in range(r):
        for j in range(c):
            cipherMatrix[i][j] = plaintext[counter] if counter < len(plaintext) else 'q'
            counter += 1

    ciphertext = ''
    count = [0] * len(keyOrder)

    for i in keyOrder:
        count[i] += 1
    
    for i in range(len(keyOrder)):
        if count[i] > 1:
            for k in range(r):
                for j in range(len(keyOrder)):
                    if keyOrder[j] == i:
                        ciphertext += cipherMatrix[k][j]

        elif count[i] == 1:
            for j in range(r):
                ciphertext += cipherMatrix[j][keyOrder.index(i)]

    return ciphertext

#--------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using Myszkowsi Transposition
#--------------------------------------------------------------
def d_myszkowski(ciphertext,key):
    keyOrder = get_keyOrder_myszkowski(key)
    c = len(keyOrder)
    r = math.ceil(len(ciphertext) / c)
    cipherMatrix = utilities_A3.new_matrix(r, c, "")
    counter = 0
    count = [0] * len(keyOrder)

    for i in keyOrder:
        count[i] += 1

    for i in range(len(keyOrder)):
        if count[i] > 1:
            for k in range(r):
                for j in range(len(keyOrder)):
                    if keyOrder[j] == i:
                        cipherMatrix[k][j] = ciphertext[counter]
                        counter += 1

        elif count[i] == 1:
            for j in range(r):
                cipherMatrix[j][keyOrder.index(i)] = ciphertext[counter]
                counter += 1
    
    plaintext = ''
    for i in range(r):
        for j in range(c):
            plaintext += cipherMatrix[i][j]

    while plaintext[len(plaintext) - 1] == 'q':
        plaintext = plaintext[:-1]
        
    return plaintext
