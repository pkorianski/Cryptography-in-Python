# Practicing Caesar cipher implementation in Python 3
# This program was created to help go through the book 'Hacking Secret Ciphers with Python' by Al Sweigart
# Programmer: Patrick M Korianski

# initializing variables
alphaStraight = dict()
alphaReverse = dict()
alphaList = 'abcdefghijklmnopqrstuvwxyz'

# Creating the Caesar cipher wheel w/ a dictionary
for i, letter in enumerate(alphaList, 0):
    alphaStraight[letter] = i
    alphaReverse[i] = letter

# Encryption method that takes a key 1-25 and a plaintext
def encrypt(key, plaintext):
    eWord = ''
    for i in plaintext:
        if i == ' ':
            eWord += ' '
            continue
        elif i.lower() not in alphaList:
            eWord += i
            continue
        letterSum = int(key) + int(alphaStraight[i.lower()])
        if letterSum >= 26:
            letterSum = letterSum - 26
            eWord += alphaReverse[letterSum]
            continue
        eWord += alphaReverse[letterSum]
    return(eWord)

# Decryption method that takes a key 1-25 and a ciphertext
def decrypt(key, ciphertext):
    dWord = ''
    for i in ciphertext:
        if i == ' ':
            dWord += ' '
            continue
        elif i.lower() not in alphaList:
            dWord += i
            continue
        letterSub = int(alphaStraight[i.lower()]) - int(key)
        if letterSub < 0:
            letterSub = 26 + letterSub
            dWord += alphaReverse[letterSub]
            continue
        dWord += alphaReverse[letterSub]
    return(dWord)

# User input & testing of encryption and decryption
# Allows the user to decide to either encrypt or decrypt a plaintext
while(True):
    options = input('Do you want to Encrypt(E) or Decrypt(D): ')
    if options.lower() == 'e' or options.lower() == 'encrypt':
        uKey = input('Enter a encryption key(1-25): ')
        uSent = input('Enter a sentence to encrypt: ')
        print('-------------\n')
        e = encrypt(int(uKey), uSent)
        print('Encrypted sentence=',e)
        print('---------------------')
    elif options.lower() == 'd' or options.lower() == 'decrypt':
        uKey = input('Enter a encryption key(1-25): ')
        uSent = input('Enter a ciphertext: ')
        print('-------------\n')
        d = decrypt(int(uKey), uSent)
        print('Decrypted sentence ->', d)
        print('---------------------')
    else:
        print('Please retry. Your input was invalid')
        print('---------------------')
        continue
    qt = input('Would you like to quit(y/n): ')
    print('\n')
    print('---------------------')
    if qt.lower() == 'y' or qt.lower() == 'yes':
        quit()
