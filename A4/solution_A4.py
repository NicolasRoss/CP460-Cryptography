#--------------------------
# CP460 (Fall 2019)
# Assignment 4
# Solution by Nicolas Ross 151703880
#--------------------------

import math
import string
import mod
import matrix
import utilities_A4

#---------------------------------
# Q1: Modular Arithmetic Library #
#---------------------------------

# solution is available in mod.py

#---------------------------------
#     Q2: Decimation Cipher      #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str,int)
# Return:       ciphertext (str)
# Description:  Encryption using Decimation Cipher
#               key is tuple (baseString,k)
#               Does not encrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key has no multiplicative inverse -->
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_decimation(plaintext,key):
    ciphertext = ''
    baseString = key[0]

    if mod.has_mul_inv(key[1], len(baseString)):
        for c in plaintext:
            if c.lower() in baseString:
                b = baseString.find(c.lower())

                if c.isupper():
                    x = mod.mul(key[1], b, len(baseString))
                    ciphertext += baseString[x].upper()
                
                else:
                    x = mod.mul(key[1], b, len(baseString))
                    ciphertext += baseString[x]
            
            else:
                ciphertext += c
        
        return ciphertext
    
    return 'Error (e_decimation): Invalid key'

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str,int)
# Return:       plaintext (str)
# Description:  Decryption using Decimation Cipher
#               key is tuple (baseString,k)
#               Does not decrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key has no multiplicative inverse -->
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_decimation(ciphertext,key):
    plaintext = ''
    baseString = key[0]

    if mod.has_mul_inv(key[1], len(baseString)):
        key = (key[0], mod.mul_inv(key[1], len(key[0])))
        plaintext = e_decimation(ciphertext, key)
        return plaintext
    
    return 'Error (d_decimation): Invalid key'

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
# Return:       plaintext,key
# Description:  Cryptanalysis of Decimation Cipher
#-----------------------------------------------------------
def cryptanalysis_decimation(ciphertext):
    plaintext = ''
    baseString = utilities_A4.get_baseString()
    dictList = utilities_A4.load_dictionary('engmix.txt')
    count = 0
    
    for i in range(0, len(baseString) - 26 + 1):
        base = baseString[:26 + i]
        table = mod.mul_inv_table(26 + i)

        for x in table[1]:
            if x != 'NA':
                key = (base, table[0][x])
                plaintext = d_decimation(ciphertext, key)
                count += 1
                
                if utilities_A4.is_plaintext(plaintext.lower(), dictList, 0.9):
                    print("Key found after:", count, "attemps")
                    return plaintext, key[1]

    return '',''

#---------------------------------
#      Q3: Affine Cipher         #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str,[int,int])
# Return:       ciphertext (str)
# Description:  Encryption using Affine Cipher
#               key is tuple (baseString,[alpha,beta])
#               Does not encrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key can not be used for decryption
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_affine(plaintext,key):
    ciphertext = ''
    baseString = key[0]
    key = key[1]

    if mod.has_mul_inv(key[0], len(baseString)):
        for c in plaintext:
            if c.lower() in baseString:
                x = baseString.find(c.lower())
                k = (key[0] * x + key[1]) % len(baseString)

                if c.isupper():
                    ciphertext += baseString[k].upper()
                
                else:
                    ciphertext += baseString[k]
            
            else:
                ciphertext += c

        return ciphertext
    
    return 'Error (e_affine): Invalid key'

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str,[int,int])
# Return:       plaintext (str)
# Description:  Decryption using Affine Cipher
#               key is tuple (baseString,[alpha,beta])
#               Does not decrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key can not be used for decryption
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_affine(ciphertext,key):
    plaintext = ''
    baseString = key[0]
    key = key[1]

    if mod.has_mul_inv(key[0], len(baseString)):
        for c in ciphertext:
            if c.lower() in baseString:
                ci = baseString.find(c.lower())
                a_inv = mod.mul_inv(key[0], len(baseString))
                x = (a_inv * (ci - key[1])) % len(baseString)

                if c.isupper():
                    plaintext += baseString[x].upper()
                
                else:
                    plaintext += baseString[x]
            
            else:
                plaintext += c

        return plaintext
    
    return 'Error (d_affine): Invalid key'

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
# Return:       plaintext,key
# Description:  Cryptanalysis of Affine Cipher
#-----------------------------------------------------------
def cryptanalysis_affine(ciphertext):
    plaintext = ''
    baseString = utilities_A4.get_baseString()
    dictList = utilities_A4.load_dictionary('engmix.txt')
    count = 0

    for i in range(0, len(baseString) - 26 + 1):
        base = baseString[:26 + i]
        table = mod.mul_inv_table(26 + i)

        for x in table[1]:
            for y in table[1]:
                if x != 'NA' and y != 'NA':
                    key = (base, [y, x])
                    plaintext = d_affine(ciphertext, key)
                    count += 1
                    
                    if utilities_A4.is_plaintext(plaintext.lower(), dictList, 0.9):
                        print("Key found after:", count, "attemps")
                        return plaintext, key[1]

    return '',''

#---------------------------------
#      Q4: Matrix Library        #
#---------------------------------

# solution is available in matrix.py

#---------------------------------
#       Q5: Hill Cipher          #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str)
# Return:       ciphertext (str)
# Description:  Encryption using Hill Cipher, 2x2 (mod 26)
#               key is a string consisting of 4 characters
#                   if key is too short, make it a running key
#                   if key is too long, use first 4 characters
#               Encrypts only alphabet
#               Case of characters can be ignored --> cipher is upper case
#               If necessary pad with 'Q'
# Errors:       if key is not inveritble or if plaintext is empty
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_hill(plaintext,key):
    ciphertext = ''
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if len(plaintext) == 0:
        print('Error(e_hill): invalid plaintext')
        return ciphertext

    if len(key) > 4:
        key = key[:4]
    
    elif len(key) < 4:
        x = len(key)
        count = 0

        while len(key) != 4:
            if count == x:
                count = 0
            
            key += key[count]
            count += 1
    
    alpha = utilities_A4.get_nonalpha(plaintext)
    text = utilities_A4.remove_nonalpha(plaintext)
    text = text.upper()

    if len(text) % 2 != 0:
        text += 'Q'
    
    indx1 = 0
    indx2 = 0
    textMatrix = matrix.new_matrix(2, int(len(text) / 2), 0)
    for i in range(len(text)):
        if i % 2 == 0:
            textMatrix[0][indx1] = base.find(text[i])
            indx1 += 1
        
        else:
            textMatrix[1][indx2] = base.find(text[i])
            indx2 += 1
    
    keyMatrix = matrix.new_matrix(2, 2, 0)
    count = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = base.find(key[count].upper())
            count += 1

    inverse = matrix.inverse(keyMatrix, 26)
    if type(inverse) == str:
        print('Error(e_hill): key is not invertible')
        return ciphertext
    
    for i in range(int(len(text) / 2)):
        a = textMatrix[0][i] * keyMatrix[0][0] + textMatrix[1][i] * keyMatrix[0][1] 
        b = textMatrix[0][i] * keyMatrix[1][0] + textMatrix[1][i] * keyMatrix[1][1]
        ciphertext += base[a % 26]
        ciphertext += base[b % 26]

    ciphertext = utilities_A4.insert_nonalpha(ciphertext, alpha)

    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str)
# Return:       plaintext (str)
# Description:  Decryption using Hill Cipher, 2x2 (mod 26)
#               key is a string consisting of 4 characters
#                   if key is too short, make it a running key
#                   if key is too long, use first 4 characters
#               Decrypts only alphabet
#               Case of characters can be ignored --> plain is lower case
#               Remove padding of q's
# Errors:       if key is not inveritble or if ciphertext is empty
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_hill(ciphertext,key):
    plaintext = ''
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if len(ciphertext) == 0:
        print('Error(d_hill): invalid ciphertext')
        return plaintext

    if len(key) > 4:
        key = key[:4]
    
    elif len(key) < 4:
        x = len(key)
        count = 0

        while len(key) != 4:
            if count == x:
                count = 0
            
            key += key[count]
            count += 1
    
    alpha = utilities_A4.get_nonalpha(ciphertext)
    text = utilities_A4.remove_nonalpha(ciphertext)
    text = text.upper()

    if len(text) % 2 != 0:
        text += 'Q'
    
    indx1 = 0
    indx2 = 0
    textMatrix = matrix.new_matrix(2, int(len(text) / 2), 0)
    for i in range(len(text)):
        if i % 2 == 0:
            textMatrix[0][indx1] = base.find(text[i])
            indx1 += 1
        
        else:
            textMatrix[1][indx2] = base.find(text[i])
            indx2 += 1
    
    keyMatrix = matrix.new_matrix(2, 2, 0)
    count = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = base.find(key[count].upper())
            count += 1
    
    inverse = matrix.inverse(keyMatrix, 26)

    for i in range(int(len(text) / 2)):
        a = textMatrix[0][i] * inverse[0][0] + textMatrix[1][i] * inverse[0][1]
        b = textMatrix[0][i] * inverse[1][0] + textMatrix[1][i] * inverse[1][1]
        plaintext += base[a % 26]
        plaintext += base[b % 26]
        
    plaintext = utilities_A4.insert_nonalpha(plaintext, alpha)
    plaintext = plaintext.lower()

    while plaintext[len(plaintext) - 1] == 'q':
        plaintext = plaintext[:-1]

    return plaintext
