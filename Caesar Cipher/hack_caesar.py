# This is an easy hack to break the Caesar cipher
# Programmer: Patrick M Korianski

# initializing variables
alphaStraight = dict()
alphaReverse = dict()
alphaList = 'abcdefghijklmnopqrstuvwxyz'

# Creating the Caesar cipher wheel w/ a dictionary
for i, letter in enumerate(alphaList, 0):
    alphaStraight[letter] = i
    alphaReverse[i] = letter

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

# Hack that runs the decrypt method with all keys 1-25
# This allows the programmer to analyze which decryption is the correct plaintext
def runHack(ciphertext):
    for x in range(1,26):
        print(str(x) + ':', decrypt(int(x), ciphertext))

ui = input('Enter ciphertext: ')
runHack(ui)
