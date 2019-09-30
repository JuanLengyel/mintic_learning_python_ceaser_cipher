def generateKey(seed):
    cipherKey = {}
    asciiCharsRange = range(0, 255)

    for number in asciiCharsRange:
        cipherKey[chr(number)] = chr((number + seed) % 256)
    
    return cipherKey

CIPHER_KEY = generateKey(80)

def cipherMessage(message):
    
    cipheredMessage = ""

    for letter in message:
        cipheredMessage += CIPHER_KEY[letter]

    return cipheredMessage
    
def decipherMessage(message):
        
    decipheredMessage = ""

    for letter in message:
        for key, value in CIPHER_KEY.iteritems():
            if (value == letter):
                decipheredMessage += key
                break

    return decipheredMessage

def main():

    while (True):

        command = str(raw_input(
        "***-----Welcome to this Caesar Cipher program. Try it out using the following options-----***\n"
        "   [c]ipher message\n"
        "   [d]ecipher message\n"
        "   [e]xit\n"
        ))[0]

        if (command == "c"):
            message = str(raw_input("Input message to cipher: "))
            cipheredMessage = cipherMessage(message)
            print("This is your encrypted message: " + cipheredMessage)
        elif (command == "d"):
            message = str(raw_input("Input message to decipher: "))
            decipheredMessage = decipherMessage(message)
            print("This is your dencrypted message: " + decipheredMessage)
        elif (command == "e"):
            return 0
        else :
            print("Command not recognized")

if __name__ == "__main__":
    main()