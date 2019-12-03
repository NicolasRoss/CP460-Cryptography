#--------------------------
# CP460 (Fall 2019)
# Assignment 4 Testing File
#--------------------------

import SDES
import utilities
import mod

#----------------------------------------------------
# Test Q1: Coding Scheme
#---------------------------------------------------
def test_q1():
    print("-------------------------------------------")
    print('Testing Encoding:')
    print("encode('A','ASCII') = ",SDES.encode('A','ASCII'))
    print("encode('\\n','ASCII') = ",SDES.encode('\n','ASCII'))
    print("encode('A','B6') = ",SDES.encode('A','B6'))
    print("encode('\\n','B6') = ",SDES.encode('\n','B6'))
    print("encode('','B6') = ",end ='')
    print(SDES.encode('','B6'))
    print("encode(1,'B6') = ",end ='')
    print(SDES.encode(1,'B6'))
    print("encode('A','Unicode') = ",end ='')
    print(SDES.encode('A','Unicode'))
    print("encode_B6('a') = ",SDES.encode_B6('a'))
    print("encode_B6('AB') = ",end = '')
    print(SDES.encode_B6('AB'))
    print()
    print('Testing Decoding:')
    print("decode('01000001','ASCII') = ",SDES.decode('01000001','ASCII'))
    print("decode('100100','B6') = ",SDES.decode('100100','B6'))
    print("decode(1000001,'ASCII') = ",end ='')
    print(SDES.decode(1000001,'ASCII'))
    print("decode('01000001','Unicode') = ",end ='')
    print(SDES.decode('01000001','Unicode'))
    print("decode('','ASCII') = ",end ='')
    print(SDES.decode('','ASCII'))
    print("decode_B6('000001') = ",SDES.decode_B6('000001'))
    print("decode_B6(100000) = ",end='')
    print(SDES.decode_B6(100000))
    print("decode_B6('0100000') = ",end='')
    print(SDES.decode_B6('0100000'))

    print()
    print("-------------------------------------------")
    return

#----------------------------------------------------
# Test Q2: SDES Configuration
#---------------------------------------------------
def test_q2():
    print("-------------------------------------------")
    print("Testing Q2: SDES Configuration")
    print()

    print('SDES Parameters:')
    print(SDES.get_SDES_parameters())
    print()
    outFile = open(SDES.configFile,'w')
    outFile.close()
    print('An empty configuration file is created')
    print('Get current configuration:',end=' ')
    print(SDES.get_SDES_config())
    print('Get value of parameter block_size:' ,end =' ')
    print(SDES.get_SDES_value('block_size'))
    print('Get value of parameter SDES_version:' ,end =' ')
    print(SDES.get_SDES_value('SDES_version'))
    print("config_SDES('block_size',12):", end = ' ')
    result = SDES.config_SDES('block_size',12)
    print(' ',result)
    print("config_SDES('block_bits',12):", end = ' ')
    result = SDES.config_SDES('block_bits','12')
    print(' ',result)
    print()

    print("config_SDES('block_size','12'):", end = ' ')
    result = SDES.config_SDES('block_size','12')
    print(' ',result)
    print("config_SDES('key_size','9'):", end = ' ')
    result = SDES.config_SDES('key_size','9')
    print(' ',result)
    print("config_SDES('q','503'):", end = ' ')
    result = SDES.config_SDES('q','503')
    print(' ',result)
    print('Get current configuration:',end=' ')
    print(SDES.get_SDES_config())
    print("get_SDES_value('key_size'): ",SDES.get_SDES_value('key_size'))
    print("get_SDES_value('p'): ",SDES.get_SDES_value('p'))
    print('Update value of q to 403')
    SDES.config_SDES('q','403')
    print('Get current configuration:',end=' ')
    print(SDES.get_SDES_config())

    print()
    print("-------------------------------------------")
    return

#----------------------------------------------------
# Test Q3: Key Generation
#---------------------------------------------------
def test_q3():
    print("-------------------------------------------")
    print("Testing Q3: Key Generation")
    print()

    print("Testing Blum:")
    print('blum(383,503,8): ',SDES.blum(383,503,8))
    print('blum(11,19,4): ',SDES.blum(11,19,4))
    print('blum(383,503,0): ',end='')
    print(SDES.blum(383,503,0))
    print('blum(383,"503",1): ',end='')
    print(SDES.blum(383,"503",1))
    print('blum(384,503,1): ',end='')
    print(SDES.blum(384,503,1))
    print()

    print("Testing generate_key_SDES:")
    outFile = open(SDES.configFile,'w')
    outFile.close()
    print("key_size = '', p = '', q=''")
    print('generate_key_SDES(): ',end='')
    print(SDES.generate_key_SDES())
    SDES.config_SDES('key_size','9')
    print("key_size = 9, p = '', q=''")
    print('generate_key_SDES():',SDES.generate_key_SDES())
    print("key_size = 9, p = 19, q = ''")
    SDES.config_SDES('p','19')
    print('generate_key_SDES():',SDES.generate_key_SDES())
    print()

    print("Testing get_subKey:")
    key = '010011001'
    print('Key = ',key)
    print('Subkey 0 = ',end='')
    print(SDES.get_subKey(key,0))
    print('Subkey 1 = ',SDES.get_subKey(key,1))
    print('Subkey 2 = ',SDES.get_subKey(key,2))
    print('Subkey 3 = ',SDES.get_subKey(key,3))
    key = '308'
    print('Key = ',key)
    print('Subkey 1 = ',end='')
    print(SDES.get_subKey(key,1))
    print()

    print("-------------------------------------------")
    print()
    return

#----------------------------------------------------
# Test Q4: Feistel Cipher
#---------------------------------------------------
def test_q4():
    print("-------------------------------------------")
    print("Testing Q3: Key Generation")
    print()
    outFile = open(SDES.configFile,'w')
    outFile.close()
    SDES.config_SDES('block_size','12')
    SDES.config_SDES('key_size','9')

    print('Testing Expand:')
    R = '011001'
    print('expand({}) = {}'.format(R,SDES.expand(R)))
    R = '00001111'
    print('expand({}) = {}'.format(R,SDES.expand(R)))
    R = '0011'
    print('expand({}) = '.format(R),end='')
    print(SDES.expand(R))
    R = '0000111'
    print('expand({}) = '.format(R),end='')
    print(SDES.expand(R))
    print()

    print('Testing Sbox1:')
    Ri = '0110'
    print('Sbox1({}) = {}'.format(Ri,SDES.sbox1(Ri)))
    Ri = '1111'
    print('Sbox1({}) = {}'.format(Ri,SDES.sbox1(Ri)))
    Ri = '11110'
    print('Sbox1({}) = '.format(Ri),end='')
    print(SDES.sbox1(Ri))
    SDES.config_SDES('block_size','16')
    Ri = '00000'
    print('Sbox1({}) = {}'.format(Ri,SDES.sbox1(Ri)))
    print()

    print('Testing Sbox2:')
    SDES.config_SDES('block_size','12')
    Ri = '0110'
    print('Sbox2({}) = {}'.format(Ri,SDES.sbox1(Ri)))
    Ri = '1111'
    print('Sbox2({}) = {}'.format(Ri,SDES.sbox2(Ri)))
    Ri = '11110'
    print('Sbox2({}) = '.format(Ri),end='')
    print(SDES.sbox2(Ri))
    SDES.config_SDES('block_size','16')
    Ri = '00000'
    print('Sbox1({}) = {}'.format(Ri,SDES.sbox2(Ri)))
    print()

    print('Testing F function:')
    SDES.config_SDES('block_size','12')
    bi = '100110'
    ki = '01100101'
    print('F({},{}) = {}'.format(bi,ki,SDES.F(bi,ki)))
    print('F({},{}) = '.format(bi[:-1],ki),end='')
    print(SDES.F(bi[:-1],ki))
    print('F({},{}) = '.format(bi,ki[:-1]),end='')
    print(SDES.F(bi,ki[:-1]))
    print()

    print('Testing feistel:')
    SDES.config_SDES('rounds','2')
    bi = '011100100110'
    ki = '01100101'
    print('feistel({},{}) = {}'.format(bi,ki,SDES.feistel(bi,ki)))
    print('feistel({},{}) = '.format(bi[:-1],ki),end='')
    print(SDES.feistel(bi[:-1],ki))
    print('feistel({},{}) = '.format(bi,ki[:-1]),end='')
    print(SDES.feistel(bi,ki[:-1]))
    print()
    

    print("-------------------------------------------")
    return

#----------------------------------------------------
# Test Q5: SDES Encryption & Decryption
#---------------------------------------------------
def test_q5():
    print("-------------------------------------------")
    print("Testing Q5: SDES Encryption & Decryption")
    print()
    
    outFile = open(SDES.configFile,'w')
    outFile.close()
    print('Testing for invalid input:')
    plaintext = ''
    key = ''
    print('e_SDES('',''): ',end='')
    SDES.e_SDES('','')
    print()
    print('d_SDES('',''): ',end='')
    SDES.d_SDES('','')
    print()
    plaintext = 123
    print('e_SDES(123,''): ',end='')
    SDES.e_SDES(123,'')
    print()
    print('d_SDES(123,''): ',end='')
    SDES.d_SDES(123,'')
    print()
    print()

    print('Testing when configuration file is empty:')
    plaintext = 'abc'
    key = '1101'
    print('e_SDES({},{}): '.format(plaintext,key),end='')
    SDES.e_SDES(plaintext,key)
    print()
    print('d_SDES({},{}): '.format(plaintext,key),end='')
    SDES.d_SDES(plaintext,key)
    print()
    print()
    
    print('Setting the Confgiruation File')
    SDES.config_SDES('rounds','2')
    SDES.config_SDES('key_size','9')
    SDES.config_SDES('block_size','12')
    SDES.config_SDES('encoding_type','B6')
    print('Configuration = ',SDES.get_SDES_config())
    key = '1101'
    print('e_SDES({},{}): '.format(plaintext,key),end='')
    SDES.e_SDES(plaintext,key)
    print()
    print('d_SDES({},{}): '.format(plaintext,key),end='')
    SDES.d_SDES(plaintext,key)
    print()
    print()

    print('Testing one block encryption/decryption:')
    plaintext = 'yR'
    key = '111000111'
    ciphertext = SDES.e_SDES(plaintext,key)
    print('e_SDES({},{}) = {}'.format(plaintext,key,ciphertext))
    plaintext2 = SDES.d_SDES(ciphertext,key)
    print('d_SDES({},{}) = {}'.format(ciphertext,key,plaintext2))
    print()

    print('Testing one block encryption/decryption with undefined characters:')
    plaintext = '(y--R)'
    key = '111000111'
    ciphertext = SDES.e_SDES(plaintext,key)
    print('e_SDES({},{}) = {}'.format(plaintext,key,ciphertext))
    plaintext2 = SDES.d_SDES(ciphertext,key)
    print('d_SDES({},{}) = {}'.format(ciphertext,key,plaintext2))
    print()

    print('Testing multiple blocks encryption/decryption:')
    plaintext = 'DES is a legacy Cipher'
    key = '111000111'
    ciphertext = SDES.e_SDES(plaintext,key)
    print('e_SDES({},{}) = {}'.format(plaintext,key,ciphertext))
    plaintext2 = SDES.d_SDES(ciphertext,key)
    print('d_SDES({},{}) = {}'.format(ciphertext,key,plaintext2))
    print()
    
    print('Testing padding and empty key:')
    plaintext = 'DES'
    key = ''
    SDES.config_SDES('p','103')
    SDES.config_SDES('q','199')
    ciphertext = SDES.e_SDES(plaintext,key)
    print('e_SDES({},{}) = {}'.format(plaintext,key,ciphertext))
    plaintext2 = SDES.d_SDES(ciphertext,key)
    print('d_SDES({},{}) = {}'.format(ciphertext,key,plaintext2))
    print()

    print('Wha happens when all blocks are the same?')
    plaintext = 'AAAAAAAA'
    key = '111000111'
    ciphertext = SDES.e_SDES(plaintext,key)
    print('e_SDES({},{}) = {}'.format(plaintext,key,ciphertext))
    plaintext2 = SDES.d_SDES(ciphertext,key)
    print('d_SDES({},{}) = {}'.format(ciphertext,key,plaintext2))
    print('I thought DES was safe!! The above repitition is a security concern')
    print('Answer: This is not about DES. It is about the Mode used, which is ECB')

    print("-------------------------------------------")
