#--------------------------
# Nicolas Ross 151703880
# CP460 (Fall 2019)
# Assignment 4
#--------------------------

import math
import string

#-----------------------------------------------------------
# Parameters:   mod (a positive integer)
# Return:       residueSet (list)
# Description:  Returns set of numbers in the given mod
#               which are residues of all other numbers
# Example:      residueSet for mod 5 --> [0,1,2,3,4]
# Errors:       mod has to be positive integer
#               return 'Error (residue_set): Invalid mod'
#-----------------------------------------------------------
def residue_set(mod):
    if type(mod) is int:
        if mod > 0:
            return [i for i in range(mod)]
    
    return 'Error (residue_set): Invalid mod'
    

#-----------------------------------------------------------
# Parameters:   num (any integer)
#               mod (a positive integer)
# Return:       residue
# Description:  Returns the smallest poisitive integer that is
#               congruent to num mod m
# Example:      residue 16 mod 5 --> 1
# Errors:       mod has to be positive integer
#                   return 'Error (residue): Invalid mod'
#               num should be integer
#                   return 'Error (residue): Invalid num'
#-----------------------------------------------------------
def residue(num, mod):
    if type(mod) is int and type(num) is int:
        if mod > 0:
            return num % mod
        
        return 'Error (residue): Invalid mod'
    return 'Error (residue): Invalid num'

#-----------------------------------------------------------
# Parameters:   a (any integer)
#               b (any integer)
#               m (a positive integer)
# Return:       True/False
# Description:  Returns True if a is congruent b mod m
#               return False otherwise
# Example:      isCongruent(22,33,11) --> True
#               isCongruent(7,9,3) --> False
# Errors:       mod has to be positive integer
#                   return 'Error (is_congruent): Invalid mod'
#               a and b should be integer
#                   return 'Error (is_congruent): Invalid input num'
#-----------------------------------------------------------
def is_congruent(a,b,m):
    if type(m) is int and type(b) is int and type(a) is int:
        if m > 0:
            if b % m == a % m:
                return True
            
            return False
        return 'Error (is_congruent): Invalid mod'
    return 'Error (is_congruent): Invalid input num'

#-----------------------------------------------------------
# Parameters:   a (any integer)
#               b (any integer)
#               m (positive integer)
# Return:       result (integer)
# Description:  Returns (a + b) mod m
#               result is an integer in residueSet mod m
# Example:      11 + 3 mod 5 = 4
# Errors:       a and b should be integers
#                   return 'Error (add): Invalid input num'
#               m should be positive integer
#                   return 'Error (add): Invalid mod'
#-----------------------------------------------------------
def add(a,b,m):
    if type(m) is int and type(b) is int and type(a) is int:
        if m > 0:
            return (a + b) % m

        return 'Error (add): Invalid mod'
    return 'Error (add): Invalid input num'

#-----------------------------------------------------------
# Parameters:   a (any integer)
#               b (any integer)
#               m (positive integer)
# Return:       result (integer)
# Description:  Returns (a - b) mod m
#               result is an integer in residueSet mod m
# Example:      11 - 2 mod 5 = 4
# Errors:       a and b should be integers
#                   return 'Error (sub): Invalid input num'
#               m should be positive integer
#                   return 'Error (sub): Invalid mod'
#-----------------------------------------------------------
def sub(a,b,m):
    if type(m) is int and type(b) is int and type(a) is int:
        if m > 0:
            return (a - b) % m

        return 'Error (sub): Invalid mod'
    return 'Error (sub): Invalid input num'

#-----------------------------------------------------------
# Parameters:   a (any integer)
#               m (positive integer)
# Return:       result (integer)
# Description:  Returns additive inverse of a mod m
#               result is an integer in residueSet mod m
# Example:      additive inverse of 7 mod 5 is
# Errors:       a and b should be integers
#                   return 'Error (add_inv): Invalid input num'
#               m should be positive integer
#                   return 'Error (add_inv): Invalid mod'
#-----------------------------------------------------------
def add_inv(a, m):
    if type(m) is int and type(a) is int:
        if m > 0:
            res_set = residue_set(m)

            for b in res_set:
                if add(a, b, m) == 0:
                    return b

        return 'Error (add_inv): Invalid mod'
    return 'Error (add_inv): Invalid input num'

#-----------------------------------------------------------
# Parameters:   m (positive integer)
# Return:       table (2D List)
# Description:  Returns addition table mod m
#               element [r][c] represent r+c mod m
# Example:      add table for mod 2 --> [[0,1],[1,0]]
# Errors:       m should be positive integer
#                   return 'Error (add_table): Invalid mod'
#-----------------------------------------------------------
def add_table(m):
    if type(m) is int:
        if m > 0:
            table = []

            for r in range(m):
                row = []
                for c in range(m):
                    row.append(add(r, c, m))

                table.append(row)

            return table

    return 'Error (add_table): Invalid mod'

#-----------------------------------------------------------
# Parameters:   m (positive integer)
# Return:       table (2D List)
# Description:  Returns subtraction table mod m
#               element [r][c] represent r-c mod m
# Example:      subtraction table for mod 3 --> [[[0,2,1],[1,0,2],[2,1,0]]
# Errors:       m should be positive integer
#                   return 'Error (sub_table): Invalid mod'
#-----------------------------------------------------------
def sub_table(m):
    if type(m) is int:
        if m > 0:
            table = []

            for r in range(m):
                row = []
                for c in range(m):
                    row.append(sub(r, c, m))

                table.append(row)

            return table

    return 'Error (sub_table): Invalid mod'

#-----------------------------------------------------------
# Parameters:   m (positive integer)
# Return:       table (2D List)
# Description:  Returns additive Inverse table mode m
#               Top row is num, bottom row is additive inverse
# Example:      Additive Inverse table mod 5 --> [[0,1,2,3,4],[0,4,3,2,1]]
# Errors:       m should be positive integer
#                   return 'Error (add_inv_table): Invalid mod'
#-----------------------------------------------------------
def add_inv_table(m):
    if type(m) is int:
        if m > 0:
            table = []
            table.append(residue_set(m))
            table.append([add_inv(b, m) for b in range(m)])

            return table

    return 'Error (add_inv_table): Invalid mod'

#-----------------------------------------------------------
# Parameters:   a (any integer)
#               b (any integer)
#               m (positive integer)
# Return:       result (integer)
# Description:  Returns (a * b) mod m
#               result is an integer in residueSet mod m
# Example:      11 * 2 mod 5 = 2
# Errors:       a and b should be integers
#                   return 'Error (mul): Invalid input num'
#               m should be positive integer
#                   return 'Error (mul): Invalid mod'
#-----------------------------------------------------------
def mul(a,b,m):
    if type(m) is int and type(b) is int and type(a) is int:
        if m > 0:
            return (a * b) % m

        return 'Error (mul): Invalid mod'
    return 'Error (mul): Invalid input num'

#-----------------------------------------------------------
# Parameters:   m (positive integer)
# Return:       table (2D List)
# Description:  Returns multiplication table mod m
#               element [r][c] represent r*c mod m
# Example:      mul table for mod 4 -->
#                       [0, 0, 0, 0]
#                       [0, 1, 2, 3]
#                       [0, 2, 0, 2]
#                       [0, 3, 2, 1]
# Errors:       m should be positive integer
#                   return 'Error (mul_table): Invalid mod'
#-----------------------------------------------------------
def mul_table(m):
    if type(m) is int:
        if m > 0:
            table = []

            for r in range(m):
                row = []
                for c in range(m):
                    row.append(mul(r, c, m))

                table.append(row)

            return table

    return 'Error (mul_table): Invalid mod'

#-----------------------------------------------------------
# Parameters:   n (an integer)
# Return:       True/False
# Description:  Returns True if n is a prime
#               False otherwise
# Errors        None
#-----------------------------------------------------------
def is_prime(n):
    if n > 1:
        for i in range(2, n // 2):
            if (n % i) == 0:
                return False

        return True 

    return False

#-----------------------------------------------------------
# Parameters:   a (an integer)
#               b (an integer)
# Return:       gcd of a and b (int)
# Description:  Returns greatest common divider using standard
#               Euclidean Algorithm
#               Implementation can be recursive or iterative
# Errors:       a and b should be positive integers
#                   return 'Error (gcd): Invalid input value'
#-----------------------------------------------------------
def gcd(a,b):
    if type(a) is int and type(b) is int and a is not 0 and b is not 0:
        a = (a * -1) if a < 0 else a
        b = (b * -1) if b < 0 else b

        while b:
            a, b = b, a % b

        return a

    return 'Error (gcd): Invalid input value'

#-----------------------------------------------------------
# Parameters:   a (an integer)
#               b (an integer)
# Return:       True/False
# Description:  Checks if two numbers are relatively prime
#               which is when gcd(a,b) equals 1
# Errors:       a and b should be integers
#                   return 'Error(is_relatively_prime): Invalid input num'
#-----------------------------------------------------------
def is_relatively_prime(a,b):
    if type(a) is int and type(b) is int:
        if gcd(a, b) is 1:
            return True

        return False
    return 'Error(is_relatively_prime): Invalid input num'

#-----------------------------------------------------------
# Parameters:   a (an integer)
#               m (a positive integer)
# Return:       True/False
# Description:  Checks if number 'a' has a multiplicative inverse
#               in mod m. Returns True if such number exist
#               Returns False otherwise
# Errors:       a should be an integer
#                   return 'Error (has_mul_inv)" Invalid input num'
#               m should be a positive integer
#                   return 'Error (has_mul_inv): Invalid mod'
#-----------------------------------------------------------
def has_mul_inv(a,m):
    if type(m) is int and type(a) is int:
        if m > 0:
            for b in range(m):
                if mul(a, b, m) == 1:
                    return True
            
            return False
        return 'Error (has_mul_inv): Invalid mod'
    return 'Error (has_mul_inv)" Invalid input num'

#-----------------------------------------------------------
# Parameters:   a (an integer)
#               b (an integer)
# Return:       [gcd(a,b) , s , t]
# Description:  Uses Extended Euclidean Algorithm to find
#               gcd of (a,b) but also numbers s and t such that
#               as + bt = gcd(a,b)
# Errors:       a and b should be integers not equal to 0
#                   return 'Error(eea): Invalid input num'
#-----------------------------------------------------------
def eea(a,b):
    if a is not 0 and b is not 0:
        a = (a * -1) if a < 0 else a
        b = (b * -1) if b < 0 else b

        x = gcd(a, b)
        s, s1, t, t1, = 0, 1, 1, 0
        while a != 0:
            q, b, a = b // a, a, b % a
            t, t1 = t1, t - q * t1
            s, s1 = s1, s - q * s1

        return [x, s, t]
    
    return 'Error(eea): Invalid input num'

#-----------------------------------------------------------
# Parameters:   a (an integer)
#               m (positive integer)
# Return:       multiplicative inverse of a mod m
# Description:  Computes multiplicative inverse of 'a' mod m
#               If such number does not exist, the function
#               return 'NA'
# Errors:       a should be an integers
#                   return 'Error (mul_inv)" Invalid input num'
#               m should be a positive integer
#                   return 'Error (mul_inv): Invalid mod
#-----------------------------------------------------------
def mul_inv(a,m):
    if type(m) is int and m > 0:
        if type(a) is int:
            res_set = residue_set(m)

            for b in res_set:
                if mul(a, b, m) == 1:
                    return b
                    
            return 'NA'
        return 'Error (mul_inv)" Invalid input num'
    return 'Error (mul_inv): Invalid mod'

#-----------------------------------------------------------
# Parameters:   m (positive integer)
# Return:       table [2D list]
# Description:  Returns multiplicative Inverse table mode m
#               Top row is num, bottom row is multiplicative inverse
# Example:      Multiplicative Inverse table mod 5 -->
#                   [[0,1,2,3,4],['NA',1,3,2,4]]
# Errors:       m should be positive integer
#                   return 'Error (mul_inv_table): Invalid mod'
#-----------------------------------------------------------
def mul_inv_table(m):
    if type(m) is int:
        if m > 0:
            table = []
            table.append(residue_set(m))
            table.append([mul_inv(b, m) for b in range(m)])

            return table

    return 'Error (mul_inv_table): Invalid mod'

# ----- Testing Function -------------
# you may use this function to test your solution locally
def test_mod():
    print('1- Testing residue_set:')
    print('residue_set({}) =  {}'.format(10,residue_set(10)))
    print('residue_set({}) =   {}'.format(1,residue_set(1)))
    print('residue_set({}) =  '.format(-5),end = '')
    print('{}'.format(residue_set(-5)))
    print('residue_set({}) = '.format([5]),end = '')
    print('{}'.format(residue_set([5])))
    print()

    print('2- Testing residue:')
    print('residue({},{}) =  {}'.format(17,5,residue(17,5)))
    print('residue({},{}) = '.format(3.4,5),end = '')
    print('{}'.format(residue(3.4,5)))
    print('residue({},{}) = '.format(13,-5),end = '')
    print('{}'.format(residue(13,-5)))
    print()

    print('3- Testing is_congruent:')
    print('is_congruent({},{},{})= {}'.format(22,33,11,is_congruent(22,33,11)))
    print('is_congruent({},{},{}) =   {}'.format(7,9,3,is_congruent(7,9,3)))
    print('is_congruent({},{},{})=  '.format(3.4,5,9),end = '')
    print('{}'.format(is_congruent(3.4,5,9)))
    print('is_congruent({},{},{}) =  '.format(3,5,-9),end = '')
    print('{}'.format(is_congruent(3,5,-9)))
    print()

    print('4- Testing add:')
    print('add({},{},{}) =  {}'.format(17,23,7,add(17,23,7)))
    print('add({},{},{}) = {}'.format(-17,23,7,add(-17,23,7)))
    print('add({},{},{}) = {}'.format(17,-23,7,add(17,-23,7)))
    print('add({},{},{}) =   '.format(9,17,0),end = '')
    print('{}'.format(add(9,17,0)))
    print('add({},{},{}) = '.format([9],17,7),end = '')
    print('{}'.format(add([9],17,7)))
    print('add({},{},{}) = '.format(9,17.1,8),end = '')
    print('{}'.format(add(9,17.1,8)))
    print()

    print('5- Testing sub:')
    print('sub({},{},{}) =  {}'.format(17,23,7,sub(17,23,7)))
    print('sub({},{},{}) = {}'.format(-17,23,7,sub(-17,23,7)))
    print('sub({},{},{}) = {}'.format(17,-23,7,sub(17,-23,7)))
    print('sub({},{},{}) =   '.format(9,17,0),end = '')
    print('{}'.format(sub(9,17,0)))
    print('sub({},{},{}) = '.format([9],17,7),end = '')
    print('{}'.format(sub([9],17,7)))
    print('sub({},{},{}) = '.format(9,17.1,8),end = '')
    print('{}'.format(sub(9,17.1,8)))
    print()

    print('6- Testing additive inverse:')
    print('add_inv({},{}) =   {}'.format(3,5,add_inv(3,5)))
    print('add_inv({},{}) =   {}'.format(6,1,add_inv(6,1)))
    print('add_inv({},{})=  {}'.format(22,10,add_inv(22,10)))
    print('add_inv({},{}) =  '.format(6,-1),end= '')
    print('{}'.format(add_inv(6,-1)))
    print('add_inv({},{}) = '.format(6.2,6),end= '')
    print('{}'.format(add_inv(6.2,6)))
    a = 4
    b = 2
    m = 5
    result = sub(a,b,m) == add(a,add_inv(b,m),m)
    print('sub({0},{1},{2}) == add({0},add_inv({1},{2}),{2})? = {3}'.format(a,b,m,result))
    print()

    print('7- Testing Addition Table:')
    print('Addition Table for mode {} ='.format(5))
    addTab = add_table(5)
    for i in range(len(addTab)):
        print(addTab[i])
    print('Addition Table for mode {} ='.format(8))
    addTab = add_table(8)
    for i in range(len(addTab)):
        print(addTab[i])
    print('Addition Table for mode {} ='.format(0))
    add_table(0)
    print()
    print()

    print('8- Testing Subtraction Table:')
    print('Subtraction Table for mode {} ='.format(5))
    subTab = sub_table(5)
    for i in range(len(subTab)):
        print(subTab[i])
    print('Subtraction Table for mode {} ='.format(8))
    subTab = sub_table(8)
    for i in range(len(subTab)):
        print(subTab[i])
    print('Subtraction Table for mode {} ='.format([5]))
    sub_table([5])
    print()
    print()
    
    print('9- Testing Addition Inverse Table:')
    print('Addition Inverse Table for mode {} ='.format(5))
    addInvTab = add_inv_table(5)
    print(addInvTab[0])
    print(addInvTab[1])
    print('Addition Inverse Table for mode {} ='.format(26))
    addInvTab = add_inv_table(26)
    print(addInvTab[0])
    print(addInvTab[1])
    print('Addition Inverse Table for mode {} ='.format(-2))
    add_inv_table(-2)
    print()
    print()

    print('10- Testing mul:')
    print('mul({},{},{}) =    {}'.format(3,5,5,mul(3,5,5)))
    print('mul({},{},{}) =    {}'.format(8,3,7,mul(8,3,7)))
    print('mul({},{},{})=   {}'.format(17,-3,7,mul(17,-3,7)))
    print('mul({},{},{}) =   '.format(9,17,0),end = '')
    print('{}'.format(mul(9,17,0)))
    print('mul({},{},{}) = '.format([9],17,7),end = '')
    print('{}'.format(mul([9],17,7)))
    print('mul({},{},{}) = '.format(9,17.1,8),end = '')
    print('{}'.format(mul(9,17.1,8)))
    print()

    print('11- Testing Multiplication Table:')
    print('Multiplication Table for mode {} ='.format(4))
    mulTab = mul_table(4)
    for i in range(len(mulTab)):
        print(mulTab[i])
    print('Multiplication Table for mode {} ='.format(5))
    mulTab = mul_table(5)
    for i in range(len(mulTab)):
        print(mulTab[i])
    print('Multiplication Table for mode {} ='.format(-5))
    mul_table(-5)
    print()
    print()

    print('12- Testing is_prime:')
    print('is_prime({}) =  {}'.format(97,is_prime(97)))
    print('is_prime({}) = {}'.format(479,is_prime(479)))
    print('is_prime({})= {}'.format(1044,is_prime(1044)))
    print('is_prime({}) =   {}'.format(0,is_prime(0)))
    print('is_prime({}) = {}'.format(-17,is_prime(-17)))
    print()

    print('13- Testing gcd:')
    print('gcd({},{}) =  {}'.format(629,357,gcd(629,357)))
    print('gcd({},{}) =  {}'.format(440,700,gcd(440,700)))
    print('gcd({},{}) =  {}'.format(-30,700,gcd(-30,700)))
    print('gcd({},{}) = {}'.format(540,-539,gcd(540,-539)))
    print('gcd({},{})   = '.format(711,0),end=' ')
    print(gcd(711,0))
    print('gcd({},{})   = '.format(0,311),end=' ')
    print(gcd(0,311))
    print('gcd({},{})  = '.format([9],27),end=' ')
    print(gcd([9],27))
    print()
    
    print('14- Testing is_relatively_prime:')
    print('is_relatively_prime({},{}) =     {}'.format(4,5,is_relatively_prime(4,5)))
    print('is_relatively_prime({},{})=  {}'.format(540,539,is_relatively_prime(540,539)))
    print('is_relatively_prime({},{}) =   {}'.format(18,26,is_relatively_prime(18,26)))
    print('is_relatively_prime({},{}) =    {}'.format(0,26,is_relatively_prime(0,26)))
    print('is_relatively_prime({},{}) ='.format([1],26),end= '  ')
    print(is_relatively_prime([1],26))
    print()

    print('15- Testing has_mul_inv:')
    print('has_mul_inv({},{}) =     {}'.format(4,5,has_mul_inv(4,5)))
    print('has_mul_inv({},{}) =   {}'.format(17,26,has_mul_inv(17,26)))
    print('has_mul_inv({},{}) =   {}'.format(18,26,has_mul_inv(18,26)))
    print('has_mul_inv({},{}) =    {}'.format(0,26,has_mul_inv(0,26)))
    print('has_mul_inv({},{}) ='.format([1],26),end= '  ')
    print(has_mul_inv([1],26))
    print()

    print('16- Testing EEA:')
    print('eea({},{}) =   {}'.format(700,440,eea(700,440)))
    print('eea({},{}) =     {}'.format(88,35,eea(88,35)))
    print('eea({},{}) =     {}'.format(35,88,eea(35,88)))
    print('eea({},{}) =    {}'.format(-88,35,eea(-88,35)))
    print('eea({},{}) =    {}'.format(88,-35,eea(88,-35)))
    print('eea({},{}) =     '.format(0,777),end = '')
    print(eea(0,777))
    print()

    print('17- Testing mul_inv:')
    print('mul_inv({},{}) =   {}'.format(23,26,mul_inv(23,26)))
    print('mul_inv({},{}) =     {}'.format(5,6,mul_inv(5,6)))
    print('mul_inv({},{}) =   {}'.format(24,26,mul_inv(24,26)))
    print('mul_inv({},{}) = {}'.format(700,440,mul_inv(700,440)))
    print('mul_inv({},{}) =   {}'.format(0,777,mul_inv(700,440)))
    print('mul_inv({},{}) =  '.format(1,[99]),end = '')
    print(mul_inv(1,[99]))
    print('mul_inv({},{}) =  '.format([1],99),end = '')
    print(mul_inv([1],99))
    print()

    print('18- Testing Multiplicative Inverse Table:')
    print('Multiplicative Inverse Table for mode {} ='.format(5))
    mulInvTab = mul_inv_table(5)
    print(mulInvTab[0])
    print(mulInvTab[1])
    print('Multiplicative Inverse Table for mode {} ='.format(26))
    mulInvTab = mul_inv_table(26)
    print(mulInvTab[0])
    print(mulInvTab[1])
    print('Multiplicative Inverse Table for mode {} ='.format(-2))
    mul_inv_table(-2)
    print()
    print()
    return
