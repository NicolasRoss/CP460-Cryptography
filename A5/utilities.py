import random
import string
import math

# 1- get_lower()
# 2- shift_string(s,n,d)
# 3- get_B6Code()
# 4- bin_to_dec(b)
# 5- is_binary(b)
# 6- dec_to_bin(decimal,size)
# 7- xor(a,b)
# 8- get_undefined(text,base)
# 9- insert_undefinedList(text, undefinedList)
# 10- remove_undefined(text,base)
#-----------------------------------------------------------
# Parameters:   None 
# Return:       alphabet (string)
# Description:  Return a string of lower case alphabet
#-----------------------------------------------------------
def get_lower():
    return "".join([chr(ord('a')+i) for i in range(26)])

#-------------------------------------------------------------------
# Parameters:   s (string): input string
#               n (int): number of shifts
#               d (str): direction ('l' or 'r')
# Return:       s (after applying shift
# Description:  Shift a given string by n shifts (circular shift)
#               as specified by direction, l = left, r= right
#               if n is negative, multiply by 1 and change direction
#-------------------------------------------------------------------
def shift_string(s,n,d):
    if d != 'r' and d!= 'l':
        print('Error (shift_string): invalid direction')
        return ''
    if n < 0:
        n = n*-1
        d = 'l' if d == 'r' else 'r'
    n = n%len(s)
    if s == '' or n == 0:
        return s

    s = s[n:]+s[:n] if d == 'l' else s[-1*n:] + s[:-1*n]
    return s

#-----------------------------------------------------------
# Parameters:   None
# Return:       B6Code (str)
# Description:  Generates all symbols in the B6 Encoding Scheme
#               This includes 64 symbols arranged as follows:
#               Digits 0 to 9
#               26 lower case alphabet
#               26 upper case alphabet
#               space
#               newline, i.e. '\n'
#               All punctuations and special sybmols are not represented in this encoding
# Error:        None
#-----------------------------------------------------------
def get_B6Code():
    nums = ''.join([str(i) for i in range(10)]) #10 sybmols
    alphabet = get_lower() # 26 symbols
    return nums+ alphabet + alphabet.upper() + ' ' + '\n' #64 symbols

#-----------------------------------------------------------
# Parameters:   b (str): binary number
# Return:       decimal (int)
# Description:  Converts any binary number into corresponding integer
# Error:        if not a valid binary number: 
#                   print('Error(bin_to_dec): invalid input'), return ''
#-----------------------------------------------------------
def bin_to_dec(b):
    if not is_binary(b):
        print('Error(bin_to_dec): invalid input')
        return ''
    value = 0
    exponent = len(b)-1
    for i in range(len(b)):
        if b[i] == '1':
            value+= 2**exponent
        exponent-=1
    return value

#-----------------------------------------------------------
# Parameters:   b (str): binary number
# Return:       True/False
# Description:  Checks if given input is a string that represent a valid
#               binary number
#               An empty string, or a string that contains other than 0 or 1
#               should return False
# Error:        None
#-----------------------------------------------------------
def is_binary(b):
    if not isinstance(b,str) or b == '':
        return False
    for i in range(len(b)):
        if b[i]!= '0' and b[i]!='1':
            return False
    return True

#-----------------------------------------------------------
# Parameters:   decimal (int)
#               size (int)
# Return:       binary (str)
# Description:  Converts any integer to binary and fit in size bits
#               if number is too small to occupy size bits --> pre-pad with 0's 
# Error:        if decimal or size is not integer:
#                   print('Error(dec_to_binary): invalid input'), return ''
#               if size is too small to fit binary number:
#                   print('Error(dec_to_binary): integer overflow'), return ''
#-----------------------------------------------------------
def dec_to_bin(decimal,size):
    if not isinstance(decimal,int) or not isinstance(size,int):
        print('Error(dec_to_binary): invalid input')
        return ''
    if size <1:
        print('Error(dec_to_binary): invalid size')
        return ''
    binary = ''
    q = 1
    r = 0
    while q!=0:
        q = decimal//2
        r = decimal%2
        decimal = q
        binary = str(r)+binary
    if len(binary) > size:
        print('Error(dec_to_binary): integer overflow')
        return ''
    while len(binary)!= size:
        binary = '0'+binary
    return binary

#-----------------------------------------------------------
# Parameters:   a (str): binary number
#               b (str): binary number
# Return:       decimal (int)
# Description:  Apply xor operation on a and b
# Error:        if a or b is not a valid binary number 
#                   print('Error(xor): invalid input'), return ''
#               if a and b have different lengths:
#                    print('Error(xor): size mismatch'), return ''
#-----------------------------------------------------------
def xor(a,b):
    if not is_binary(a) or not is_binary(b):
        print('Error(xor): invalid input')
        return ''
    if len(a)!= len(b):
        print('Error(xor): size mismatch')
        return ''
    c = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            c+='0'
        else:
            c+='1'
    return c

#-----------------------------------
# Parameters:   text (str)
#               base (str)
# Return:       undefinedList (2D List)
# Description:  Analyzes a given text
#               Returns a list of all characters of text which are undefined
#               in base, along with their positions
#               Format: [[char1, pos1],[char2,post2],...]
#-----------------------------------
def get_undefined(text,base):
    undefinedList = []
    for i in range(len(text)):
        if text[i] not in base:
            undefinedList.append([text[i],i])
    return undefinedList

#-----------------------------------
# Parameters:   text (str)
#               2D list: [[char1,pos1], [char2,pos2],...]
# Return:       modifiedText (string)
# Description:  inserts a list of nonalpha characters in the positions
#-----------------------------------
def insert_undefinedList(text, undefinedList):
    modifiedText = text
    for item in undefinedList:
        modifiedText = modifiedText[:item[1]]+item[0]+modifiedText[item[1]:]
    return modifiedText

#-----------------------------------
# Parameters:   text (string)
#               base (string)
# Return:       modifiedText (string)
# Description:  Removes all characters in text which are not found in base
#-----------------------------------
def remove_undefined(text,base):
    modifiedText = ''
    for c in text:
        if c in base:
            modifiedText += c
    return modifiedText
