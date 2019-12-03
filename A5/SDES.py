#--------------------------
# Nicolas Ross 151703880
# CP460 (Fall 2019)
# Assignment 5
#--------------------------

import math
import string
import mod
import utilities

configFile = 'SDES_config.txt'
sbox1File = 'sbox1.txt'
sbox2File = 'sbox2.txt'
primeFile = 'primes.txt'

#-----------------------
# Q1: Coding Scheme
#-----------------------
#-----------------------------------------------------------
# Parameters:   c (str): a character
#               codeType (str)
# Return:       b (str): corresponding binary number
# Description:  Generic function for encoding
#               Current implementation supports only ASCII and B6 encoding
# Error:        If c is not a single character:
#                   print('Error(encode): invalid input'), return ''
#               If unsupported encoding type:
#                   print('Error(encode): Unsupported Coding Type'), return '' 
#-----------------------------------------------------------
def encode(c,codeType):
    b = ''
    if type(c) is str and len(c) == 1:
        if codeType == 'ASCII':
            b = format(ord(c), '08b')

        elif codeType == 'B6':
            b = encode_B6(c)
            
        else:
            print('Error(encode): Unsupported Coding Type', end='')
    else:
        print('Error(encode): invalid input', end='')

    return b

#-----------------------------------------------------------
# Parameters:   b (str): a binary number
#               codeType (str)
# Return:       c (str): corresponding character
# Description:  Generic function for decoding
#               Current implementation supports only ASCII and B6 encoding
# Error:        If c is not a binary number:
#                   print('Error(decode): invalid input',end =''), return ''
#               If unsupported encoding type:
#                   print('Error(decode): Unsupported Coding Type',end =''), return '' 
#-----------------------------------------------------------
def decode(b,codeType):
    c= ''
    if utilities.is_binary(b):
        if codeType == 'ASCII':
            c = chr(utilities.bin_to_dec(b))

        elif codeType == 'B6':
            c = decode_B6(b)
            
        else:
            print("Error(decode): Unsupported Coding Type",end='')
    else:
        print("Error(decode): invalid input",end='')

    return c

#-----------------------------------------------------------
# Parameters:   c (str): a character
# Return:       b (str): 6-digit binary code
# Description:  Encodes any given symbol in the B6 Encoding scheme
#               If given symbol is one of the 64 symbols, the function returns
#               the binary representation, which is the equivalent binary number
#               of the decimal value representing the position of the symbol in the B6Code
#               If the given symbol is not part of the B6Code --> return empty string (no error msg)
# Error:        If given input is not a single character -->
#                   print('Error(encode_B6): invalid input',end =''), return ''
#-----------------------------------------------------------
def encode_B6(c):
    b = ''
    b6 = utilities.get_B6Code()
    if type(c) is str and len(c) == 1:
        if c in b6:
            b = format(b6.find(c),"06b")
    
    else:
        print("Error(encode_B6): invalid input",end='')

    return b

#-----------------------------------------------------------
# Parameters:   b (str): binary number
# Return:       c (str): a character
# Description:  Decodes any given binary code in the B6 Coding scheme
#               Converts the binary number into integer, then get the
#               B6 code at that position
# Error:        If given input is not a valid 6-bit binary number -->
#                   print('Error(decode_B6): invalid input',end =''), return ''
#-----------------------------------------------------------
def decode_B6(b):
    c = ''
    b6 = utilities.get_B6Code()
    if utilities.is_binary(b):
        if len(b) == 6:
            num = utilities.bin_to_dec(b)
            c = b6[num].rstrip("\n")
        
        else:
            print("Error(decode_B6): invalid input",end='')

    else:
        print("Error(decode_B6): invalid input",end='')

    return c

#-----------------------
# Q2: SDES Configuration
#-----------------------
#-----------------------------------------------------------
# Parameters:   None
# Return:       paramList (list)
# Description:  Returns a list of parameter names which are used in
#               Configuration of SDES
# Error:        None
#-----------------------------------------------------------
def get_SDES_parameters():
    return ['encoding_type','block_size','key_size','rounds','p','q']

#-----------------------------------------------------------
# Parameters:   None
# Return:       configList (2D List)
# Description:  Returns the current configuraiton of SDES
#               configuration list is formatted as the following:
#               [[parameter1,value],[parameter2,value2],...]
#               The configurations are read from the configuration file
#               If configuration file is empty --> return []
# Error:        None
#-----------------------------------------------------------
def get_SDES_config():
    configList = []
    f = open(configFile, 'r')

    for line in f:
        configList.append(line.rstrip('\n').split(","))
    
    f.close()
    return configList

#-----------------------------------------------------------
# Parameters:   parameter (str)
# Return:       value (str)
# Description:  Returns the value of the parameter based on the current
# Error:        If the parameter is undefined in get_SDES_parameters() -->
#                   print('Error(get_SDES_value): invalid parameter',end =''), return ''
#-----------------------------------------------------------
def get_SDES_value(parameter):
    value = ''

    if parameter in get_SDES_parameters():
        config = get_SDES_config()

        for item in config:
            if item[0] == parameter:
                if len(item) != 1:
                    value = item[1]
    else:
        print("Error(get_SDES_value): invalid parameter",end='')

    return value

#-----------------------------------------------------------
# Parameters:   parameter (str)
#               value (str)
# Return:       True/False
# Description:  Sets an SDES parameter to the given value and stores
#               the output in the configuration file
#               if the configuration file contains previous value for the parameter
#               the function overrides it with the new value
#               otherwise, the new value is appended to the configuration file
#               Function returns True if set value is successful and False otherwise
# Error:        If the parameter is undefined in get_SDES_parameters() -->
#                   print('Error(cofig_SDES): invalid parameter',end =''), return False
#               If given value is not a string or is an empty string:
#                   print('Error(config_SDES): invalid value',end =''), return 'False
#-----------------------------------------------------------
def config_SDES(parameter,value):
    if parameter not in get_SDES_parameters():
        print('Error(cofig_SDES): invalid parameter',end ='')
        return False
    
    if type(value) is not str or value == '':
        print("Error(config_SDES): invalid value",end='')
        return False
    
    config = get_SDES_config()
    inFile = False

    for x, v in enumerate(config):
        if v[0] == parameter:
            inFile = True

            if len(v) != 1:
                config[x][1] = value
            
            else:
                config[v] = [parameter, value]

    if not inFile:
        inFile = True
        f = open(configFile, 'a')
        f.write(parameter + ',' + value + '\n')
        f.close()
        
    
    else:
        f = open(configFile, 'w')
        
        for val in config:
            f.write(val[0] + ',' + val[1] + '\n')
        
        f.close()

    return inFile

#-----------------------
# Q3: Key Generation
#-----------------------
#-----------------------------------------------------------
# Parameters:   p (int)
#               q (int)
#               m (int): number of bits
# Return:       bitStream (str)
# Description:  Uses Blum Blum Shub Random Generation Algorithm to generates
#               a random stream of bits of size m
#               The seed is the nth prime number, where n = p*q
#               If the nth prime number is not relatively prime with n,
#               the next prime number is selected until a valid one is found
#               The prime numbers are read from the file primeFile (starting n=1)
# Error:        If number of bits is not a positive integer -->
#                   print('Error(blum): Invalid value of m',end =''), return ''
#               If p or q is not an integer that is congruent to 3 mod 4:
#                   print('Error(blum): Invalid values of p,q',end =''), return ''
#-----------------------------------------------------------
def blum(p,q,m):
    if type(m) is not int or m <= 0:
        print("Error(blum): Invalid value of m",end="")
        return ''
    
    if mod.is_congruent(p, 3, 4) is not True or mod.is_congruent(q, 3, 4) is not True:
        print("Error(blum): Invalid values of p,q",end="")
        return ''
    
    bitStream = ''
    n = p * q
    count = p * q
    f = open(primeFile, 'r')
    primes = f.readlines()
    
    prime = False
    while not prime:
        if mod.is_relatively_prime(n, primes[count - 1]):
            num = int(primes[count - 1])
            prime = True
    
        else:
            count += 1

    temp = [num]
    for i in range(0, m + 1):
        temp.append((temp[i] * temp[i]) % count)
        bitStream += "" + str(temp[i + 1] % 2)

    return bitStream[1:]

#-----------------------------------------------------------
# Parameters:   None
# Return:       key (str)
# Description:  Generates an SDES key based on preconfigured values
#               The key size is fetched from the SDES configuration
#               If no key size is available, an error message is printed
#               Also, the values of p and q are fetched as per SDES configuration
#               If no values are found, the default values p = 383 and q = 503 are used
#               These values should be updated in the configuration file
#               The function calls the blum function to generate the key
# Error:        if key size is not defined -->
#                           print('Error(generate_key_SDES):Unknown Key Size',end=''), return ''
#-----------------------------------------------------------
def generate_key_SDES():
    size = get_SDES_value("key_size")
    if size == '':
        print("Error(generate_key_SDES): Unkown Key Size",end="")
        return ''
    
    p = get_SDES_value('p')
    q = get_SDES_value('q')

    if p == '':
        p = 383
        config_SDES('p', "383")
    
    if q == '':
        q = 503
        config_SDES('q', "503")
    
    return blum(int(p), int(q), int(size))

#-----------------------------------------------------------
# Parameters:   key (str)
#               i (int)
# Return:       key (str)
# Description:  Generates a subkey for the ith round in SDES
#               The sub-key is one character shorter than original key size
#               Sub-key is generated by circular shift of key with value 1,
#               where i=1 means no shift
#               The least significant bit is dropped after the shift
# Errors:       if key is not a valid binary number or its length does not match key_size: -->
#                   print('Error(get_subKey): Invalid key',end='')
#               if i is not a positive integer:
#                   print('Error(get_subKey): invalid i',end=''), return ''
#-----------------------------------------------------------
def get_subKey(key,i):
    size = get_SDES_value("key_size")
    if not utilities.is_binary(key) or len(key) != int(size):
        print("Error(get_subKey): Invalid key",end="")
        return ''
    
    if type(i) is not int or i <= 0:
        print("Error(get_subKey): invalid i",end="")
        return ''
    
    subKey = ''
    if i == 1:
        subKey = key[:-1]
    
    else:
        subKey = utilities.shift_string(key, i - 1, "l")
        subKey = subKey[:-1].rstrip("\n")
    
    return subKey

#-----------------------
# Q4: Fiestel Network
#-----------------------
#-----------------------------------------------------------
# Parameters:   R (str): binary number of size (block_size/2)
# Return:       output (str): expanded binary
# Description:  Expand the input binary number by adding two digits
#               The input binary number should be an even number >= 6
#               Expansion works as the following:
#               If the index of the two middle elements is i and i+1
#               From indices 0 up to i-1: same order
#               middle becomes: R(i+1)R(i)R(i+1)R(i)
#               From incides R(i+2) to the end: same order
# Error:        if R not a valid binary number or if it has an odd length
#               or is of length smaller than 6
#                   print('Error(expand): invalid input',end=''), return ''
#-----------------------------------------------------------
def expand(R):
    if utilities.is_binary(R) and len(R) >= 6 and (len(R) % 2) == 0:
        i = int((len(R) / 2) - 1)
        start = R[:i]
        middle =  R[i + 1] + R[i] + R[i + 1] + R[i]
        end = R[i + 2:]
        output = start + middle + end
    
    else:
        print("Error(expand): invalid input",end="")
        output = ''

    return output

#-----------------------------------------------------------
# Parameters:   R (str): binary number of size (block_size//4)
# Return:       output (str): binary number
# Description:  Validates that R is of size block_size//4 + 1
#               Retrieves relevant structure of sbox1 from sbox1File
#               Most significant bit of R is row number, other bits are column number
# Error:        if undefined block_size:
#                   print('Error(sbox1): undefined block size',end=''), return ''
#               if invalid R:
#                   print('Error(sbox1): invalid input',end=''),return ''
#               if no sbox1 structure exist:
#                   print('Error(sbox1): undefined sbox1',end=''),return ''
#-----------------------------------------------------------       
def sbox1(R):
    size = get_SDES_value("block_size")
    if size == '':
        print("Error(sbox1): undefined block size",end="")
        return ''
    
    if len(R) != ((int(size) // 4) + 1):
        print("Error(sbox1): invalid input",end="")
        return ''
    
    f = open(sbox1File, 'r')
    found = False
    output = ''

    for line in f:
        if line[0] == str(len(R)):
            found = True
            output = line
            break
    
    f.close()

    if found:
        output = output.split(':')
        output = output[1].split(',')
        col = utilities.bin_to_dec(R)
        output = output[col].strip()

    else:
        print("Error(sbox1): undefined sbox1",end="")

    return output

#-----------------------------------------------------------
# Parameters:   R (str): binary number of size (block_size//4)
# Return:       output (str): binary
# Description:  Validates that R is of size block_size//4 + 1
#               Retrieves relevant structure of sbox2 from sbox2File
#               Most significant bit of R is row number, other bits are column number
# Error:        if undefined block_size:
#                   print('Error(sbox2): undefined block size',end=''), return ''
#               if invalid R:
#                   print('Error(sbox2): invalid input',end=''),return ''
#               if no sbox1 structure exist:
#                   print('Error(sbox2): undefined sbox1',end=''),return ''
#-----------------------------------------------------------
def sbox2(R):
    size = get_SDES_value("block_size")
    if size =="":
        print("Error(sbox2): undefined block size",end="")
        return ''

    if len(R) != ((int(size) // 4) + 1):
        print("Error(sbox1): invalid input",end="")
        return ''
    
    f = open(sbox2File, 'r')
    found = False
    output = ''

    for line in f:
        if line[0] == str(len(R)):
            found = True
            output = line
            break
    
    f.close()

    if found:
        output = output.split(':')
        output = output[1].split(',')
        col = utilities.bin_to_dec(R)
        output = output[col].strip()
    
    else:
        print("Error(sbox2): undefined sbox1",end="")

    return output

#-----------------------------------------------------------
# Parameters:   Ri (str): block of binary numbers
#               ki (str): binary number representing subkey
# Return:       Ri2 (str): block of binary numbers
# Description:  Performs the following five tasks:
#               1- Pass the Ri block to the expander function
#               2- Xor the output of [1] with ki
#               3- Divide the output of [2] into two equal sub-blocks
#               4- Pass the most significant bits of [3] to Sbox1
#                  and least significant bits to sbox2
#               5- Conactenate the output of [4] as [sbox1][sbox2]
# Error:        if ki is an invalid binary number:
#                   print('Error(F): invalid key',end=''), return ''
#               if invalid Ri:
#                   print('Error(F): invalid input',end=''),return ''
#-----------------------------------------------------------   
def F(Ri,ki):
    if not utilities.is_binary(ki):
        print("Error(F): invalid key",end="")
        return ''
    
    exp = ''
    if utilities.is_binary(Ri) and len(Ri) >= 6 and (len(Ri) % 2) == 0:
        exp = expand(Ri)

        if len(exp) == len(ki):
            xor = utilities.xor(exp, ki)
            m = len(xor) // 2
            A = sbox1(xor[:m])
            B = sbox2(xor[m:])
            Ri2 = (A + B).strip()
        
        else:
            print("Error(F): invalid key",end="")
            Ri2 = ''

    else:
        print("Error(F): invalid input",end="")
        return ''

    return Ri2

#-----------------------------------------------------------
# Parameters:   bi (str): block of binary numbers
#               ki (str): binary number representing subkey
# Return:       bi2 (str): block of binary numbers
# Description:  Applies Fiestel Cipher on a block of binary numbers
#               L(current) = R(previous)
#               R(current) = L(previous)xor F(R(previous), subkey)
# Error:        if ki is an invalid binary number or of invalid size
#                   print('Error(feistel): Invalid key',end=''), return ''
#               if invalid Ri:
#                   print('Error(feistel): Invalid block',end=''),return ''
#----------------------------------------------------------- 
def feistel(bi,ki):
    bi2 = ''
    if len(bi) >= 12 and (len(bi) % 2) == 0:
        if len(ki) >= 6 and (len(ki) % 2) == 0:
            m = len(bi) // 2
            currLeft = bi[m:]
            prevLeft = bi[:m]
            temp = F(currLeft, ki).replace('\n', '')
            currRight = utilities.xor(temp, prevLeft)
            bi2 = currLeft + currRight
        
        else:
            print("Error(feistel): Invalid key",end="")

    else:
        print("Error(feistel): Invalid block",end="")
    return bi2

#----------------------------------
# Q5: SDES Encryption/Decryption
#----------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str)
# Return:       ciphertext (str)
# Description:  Encryption using Simple DES
#----------------------------------------------------------- 
def e_SDES(plaintext,key):
    ciphertext = ''
    if plaintext == '':
        print("Error(e_SDES): Invalid input", end="")
        return ciphertext

    size = get_SDES_value("key_size")
    if key == '': 
        if size == '':
            print("Error(e_SDES): Invalid input",end="")
            return ciphertext

        key = generate_key_SDES()

    else:
        if get_SDES_value("encoding_type") == '' or get_SDES_value("block_size") == '' or get_SDES_value("key_size") == '' or get_SDES_value("rounds") == '':
            print("Error(e_SDES): Invalid configuration",end="")
            return ciphertext
        
        if int(size) != len(key):
            print("Error(e_SDES): Invalid key",end="")
            return ciphertext
    
    b6 = utilities.get_B6Code()
    undefined = utilities.get_undefined(plaintext, b6)
    defined = utilities.remove_undefined(plaintext, b6)

    if (len(defined) % 2) != 0:
        defined += 'Q'
    
    for i in range(0, len(defined), 2):
        left = encode_B6(defined[i])
        right = encode_B6(defined[i + 1])
        subKey = get_subKey(key, 1)
        feis = feistel(left + right, subKey)
        subKey = get_subKey(key, 2)
        feis = feistel(right + feis[6:], subKey)
        ciphertext += decode_B6(feis[6:])
        ciphertext += decode_B6(feis[:6])
    
    ciphertext = utilities.insert_undefinedList(ciphertext, undefined)

    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str)
# Return:       plaintext (str)
# Description:  Decryption using Simple DES
#----------------------------------------------------------- 
def d_SDES(ciphertext,key):
    plaintext = ''
    if ciphertext == '':
        print("Error(d_SDES): Invalid input", end="")
        return plaintext

    size = get_SDES_value("key_size")
    if key == '': 
        if size == '':
            print("Error(d_SDES): Invalid input",end="")
            return plaintext

        key = generate_key_SDES()

    else:
        if get_SDES_value("encoding_type") == '' or get_SDES_value("block_size") == '' or get_SDES_value("key_size") == '' or get_SDES_value("rounds") == '':
            print("Error(d_SDES): Invalid configuration",end="")
            return plaintext
        
        if int(size) != len(key):
            print("Error(d_SDES): Invalid key",end="")
            return plaintext
    
    b6 = utilities.get_B6Code()
    undefined = utilities.get_undefined(ciphertext, b6)
    defined = utilities.remove_undefined(ciphertext, b6)

    for i in range(0, len(defined), 2):
        left = encode_B6(defined[i])
        right = encode_B6(defined[i + 1])
        subKey = get_subKey(key, 2)
        feis = feistel(left + right, subKey)
        subKey = get_subKey(key, 1)
        feis = feistel(right + feis[6:], subKey)
        plaintext += decode_B6(feis[6:])
        plaintext += decode_B6(feis[:6])
    
    while plaintext[len(plaintext) - 1] == 'Q':
        plaintext = plaintext[:-1]

    plaintext = utilities.insert_undefinedList(plaintext,undefined)
 
    return plaintext
