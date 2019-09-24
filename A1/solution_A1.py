#--------------------------
# Nicolas Ross 151703880
# CP460 (Fall 2019)
# Assignment 1
#--------------------------


import math
import string

#---------------------------------
#       Given Functions          #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   fileName (string)
# Return:       contents (string)
# Description:  Utility function to read contents of a file
#               Can be used to read plaintext or ciphertext
#-----------------------------------------------------------
def file_to_text(fileName):
    inFile = open(fileName,'r')
    contents = inFile.read()
    inFile.close()
    return contents

#-----------------------------------------------------------
# Parameters:   text (string)
#               filename (string)            
# Return:       none
# Description:  Utility function to write any given text to a file
#               If file already exist, previous content will be over-written
#-----------------------------------------------------------
def text_to_file(text, filename):
    outFile = open(filename,'w')
    outFile.write(text)
    outFile.close()
    return

#-----------------------------------------------------------
# Parameters:   r: #rows (int)
#               c: #columns (int)
#               pad (str,int,double)
# Return:       empty matrix (2D List)
# Description:  Create an empty matrix of size r x c
#               All elements initialized to pad
#               Default row and column size is 2
#-----------------------------------------------------------
def new_matrix(r,c,pad):
    r = r if r >= 2 else 2
    c = c if c>=2 else 2
    return [[pad] * c for i in range(r)]

#-----------------------------------------------------------
# Parameters:   marix (2D List)
# Return:       None
# Description:  prints a matrix each row in a separate line
#               Assumes given parameter is a valid matrix
#-----------------------------------------------------------
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end='\t')
        print()
    return
#-----------------------------------------------------------
# Parameters:   marix (2D List)
# Return:       text (string)
# Description:  convert a 2D list of characters to a string
#               left to right, then top to bottom
#               Assumes given matrix is a valid 2D character list
#-----------------------------------------------------------
def matrix_to_string(matrix):
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            text+=matrix[i][j]
    return text

#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using Scytale Cipher
#               Key is the diameter, i.e. # rows
#               Assume infinte length rod (infinte #columns)
#--------------------------------------------------------------
def e_scytale(plaintext, key):
    # By definition, number of rows is key
    r = int(key)
    # number of columns is the length of ciphertext/# rows    
    c = int(math.ceil(len(plaintext)/key))
    # create an empty matrix for ciphertext rxc
    cipherMatrix = new_matrix(r,c,"")

    # fill matrix horizontally with characers, pad empty slots with -1
    counter = 0
    for i in range(r):
        for j in range(c):
            cipherMatrix[i][j] = plaintext[counter] if counter < len(plaintext) else -1
            counter+=1

    #convert matrix into a string (vertically)
    ciphertext = ""
    for i in range(c):
        for j in range(r):
            if cipherMatrix[j][i]!=-1:
                ciphertext+=cipherMatrix[j][i]
    return ciphertext


#---------------------------------
#       Problem 1                #
#---------------------------------
      
#----------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using Scytale Cipher
#               Assumes key is a valid integer in string format             
#---------------------------------------------------
def d_scytale(ciphertext, key):
    r = int(key)
    c = int(math.ceil(len(ciphertext) / key))
    L = int((r * c) - len(ciphertext))
    matrix = new_matrix(r, c, "")
    plaintext = ""

    if L > c:
        return plaintext
    
    check = r
    count = len(ciphertext) - 1
    for col in range(c - 1, -1, -1):
        for row in range(r - 1, -1, -1):
            if ((check == r) and L > 0):
                matrix[row][col] = -1
                check = 0
                L-=1

            else:
                matrix[row][col] = ciphertext[count]
                count-=1

            check+=1

    for i in range(r):
        for j in range(c):
            if matrix[i][j] != -1:
                plaintext+=matrix[i][j] 

    return plaintext

#---------------------------------
#       Problem 2                #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   dictFile (string): filename
# Return:       list of words (list)
# Description:  Reads a given dictionary file
#               dictionary file is assumed to be formatted: each word in a separate line
#               Returns a list of strings, each pertaining to a dictionary word
#-----------------------------------------------------------
def load_dictionary(dictFile):
    dictList = []

    with open(dictFile, 'r', encoding="mbcs") as file:
        for line in file:
            dictList.append(line.strip())
    
    return dictList

#-------------------------------------------------------------------
# Parameters:   text (string)
# Return:       list of words (list)
# Description:  Reads a given text
#               Each word is saved as an element in a list. 
#               Returns a list of strings, each pertaining to a word in file
#               Gets rid of all punctuation at the start and at the end 
#-------------------------------------------------------------------
def text_to_words(text):
    wordList = []

    words = text.strip().split()

    for word in words:
        wordList.append(word.strip(string.punctuation))
        
    return wordList

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
# Return:       (#matches, #mismatches)
# Description:  Reads a given text, checks if each word appears in dictionary
#               Returns a tuple of number of matches and number of mismatches.
#               Words are compared in lowercase.
#-----------------------------------------------------------
def analyze_text(text, dictFile):
    matches = 0
    mismatches = 0

    wordList = text_to_words(text)
    dictList = load_dictionary(dictFile)
    lowercase = []

    for word in dictList:
        lowercase.append(word.lower())

    for word in wordList:
        if word.lower() in lowercase:
            matches+=1

        else:
            mismatches+=1
        
    return(matches, mismatches)

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
#               threshold (float): number between 0 to 1
# Return:       True/False
# Description:  Check if a given file is a plaintext
#               If #matches/#words >= threshold --> True
#                   otherwise --> False
#               If invalid threshold given, default is 0.9
#               An empty string is assumed to be non-plaintext.
#-----------------------------------------------------------
def is_plaintext(text, dictFile, threshold):
    if (threshold <= 0 and threshold >= 1):
        threshold = 0.9

    matches, mismatches = analyze_text(text, dictFile)

    if (matches > 0 and mismatches >= 0):
        if ((matches/(matches + mismatches)) >= threshold):
            return True
    
    return False

#---------------------------------
#       Problem 3                #
#---------------------------------
      
#----------------------------------------------------
# Parameters:   cipherFile (string)
#               dictFile (string)
#               startKey (int)
#               endKey (int)
#               threshold (float)
# Return:       key (string)
# Description:  Apply brute-force to break scytale cipher
#               Valid key range: 2-100 (if invalid --> print error msg and return '')
#               Valid threshold: 0-1 (if invalid --> print error msg and return '')
#               If decryption is successful --> print plaintext and return key
#               If decrytpoin fails: print error msg and return ''
#---------------------------------------------------
def cryptanalysis_scytale(cipherFile, dictFile, startKey, endKey, threshold):

    if (startKey >= 2 and endKey <= 100):
        if (threshold >= 0 and threshold <= 1):
            ciphertext = file_to_text(cipherFile)

            for key in range(startKey, endKey):
                plaintext = d_scytale(ciphertext, key)

                if (is_plaintext(plaintext, dictFile, threshold)):
                    return plaintext

                else:
                    print("Key ", key, " was invalid.")

        else:
            print("Invalid threshold value. Operation aborted!")

    else:
        print("Invalid key range. Operation aborted!")
            
    return ''

#---------------------------------
#       Problem 4                #
#---------------------------------
      
#----------------------------------------------------
# Parameters:   None
# Return:       polybius_square (string)
# Description:  Returns the following polybius square
#               as a sequential string:
#               [1] [2]  [3] [4] [5] [6] [7] [8]
#           [1]      !    "   #   $   %   &   '
#           [2]  (   )    *   +   '   -   .   /
#           [3]  0   1    2   3   4   5   6   7
#           [4]  8   9    :   ;   <   =   >   ?
#           [5]  @   A    B   C   D   E   F   G
#           [6]  H   I    J   K   L   M   N   O
#           [7]  P   Q    R   S   T   U   V   W
#           [8]  X   Y    Z   [   \   ]   ^   _
#---------------------------------------------------
def get_polybius_square():
    polybius_square = ''

    polybius_square = "".join([chr(ord(' ')+i) for i in range(64)])
    
    return polybius_square

#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (none)
# Return:       ciphertext (string)
# Description:  Encryption using Polybius Square
#--------------------------------------------------------------
def e_polybius(plaintext, key):
    ciphertext = ''

    poly = get_polybius_square()

    for c in plaintext:
        if (c != '\n'):
            x = int((ord(c) - ord(' ')) / 8) + 1
            y = ((ord(c) - ord(' ')) % 8) + 1

            ciphertext+=str(x)
            ciphertext+=str(y)

        else:
            ciphertext+='\n'
    
    return ciphertext

#---------------------------------
#       Problem 5                #
#---------------------------------

#-------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (none)
# Return:       plaintext (string)
# Description:  Decryption using Polybius Square Cipher
#               Detects invalid ciphertext --> print error msg and return ''
#               Case 1: #of chars (other than \n) is not even
#               Case 2: the ciphertext contains non-numerical chars (except \n')
#-------------------------------------------------------
def d_polybius(ciphertext, key):
    plaintext = ''

    poly_string = get_polybius_square()
    poly_matrix = new_matrix(8, 8, "")

    counter = 0
    for i in range (8):
        for j in range(8):
            poly_matrix[i][j] = poly_string[counter]
            counter+=1

    numLines = ciphertext.count('\n')
    if (((len(ciphertext) - numLines) % 2) > 0):
        return 'Invalid ciphertext! Decryption Failed!\n'

    for c in ciphertext:
        if (c.isalpha()):
            return 'Invalid ciphertext! Decryption Failed!\n'

    count = 0
    while (count < len(ciphertext)):
        if (ciphertext[count] != '\n'):
            x = int(ciphertext[count]) - 1
            y = int(ciphertext[count + 1]) - 1
            plaintext+=poly_matrix[x][y]
            count+=2

        else:
            plaintext+='\n'
            count+=1
        
    return plaintext
