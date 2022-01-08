from array import *
import math
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import string

def encrypt(message):
    
    if len(message) % 3 != 0:
        message += ' '
        
    if len(message) % 3 != 0:
        message += ' '
    l1 = [] 
    l2 = []
    
    all_letters= string.ascii_letters
        
    for c in message:
        ascii = ord(c)
        l2.append(f'{ascii:03}')
        if len(l2) == 3:
            print(l2)
            l1.append(l2)
            l2 = [];
    
    if len(l2) > 0:
        l1.append(l2)
    
    #print(l1)
    cipherText1 = ''
    
    for i in range(3):
        for j in range(len(l1)):
            try:
                cipherText1 += l1[j][i]
            except:
                print('j',j,i)
                
    cipherText = ''
    for i in cipherText1:
        cipherText += all_letters[int(i)]
        
    return cipherText

def decrypt(cipherText1):
    
    all_letters= string.ascii_letters
    
    letters = {}
    for l in range(len(all_letters)):
        letters[all_letters[l]] = l;
        
    cipherText = ''
    for c in cipherText1:
        cipherText += str(letters[c])
        
    #print(cipherText)
    n = 3
    split_string = [cipherText[i:i+n] for i in range(0, len(cipherText), n)]
    
    rows, cols = (math.ceil(len(split_string)/3),3)
    l2 = [[0 for i in range(cols)] for j in range(rows)]

    #l2[0][0] = 'df'
    i = j = 0;
    for c in split_string:
        try:
            l2[i][j] = c
            # print(i,j,c)
            i += 1
            if (i == rows):
                i = 0
                j +=1
        except:
            print("exp",i,j)
    #print(l2)
    
    plainText = ''
    for i in range(len(l2)):
        for j in range(3):
            plainText += chr(int(l2[i][j]))
            #print(chr(int(l2[i][j])))
            
    return plainText


message = 'We are studying Cryptography'

print("\n\n Message : ",message)
cipherText = encrypt(message)

print("Cipher Text",cipherText)
print(decrypt(cipherText))
