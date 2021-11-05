plaintext = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","-","+","="," ",",",";",":","'","%","#","!","$","(",")","&","*","_","[","]","{","}","/","?","<",">","£","`","¬","~"]
cyphertext = ["p","u","x","z","r","q","o","y","v","w","s","g","d","a","t","l","c","j","i","n","e","b","k","h","f","m","P","U","X","Z","R","Q","O","Y","V","W","S","G","D","A","T","L","C","J","I","N","E","B","K","H","F","M","8","0","7","9","2","4","5","3","1","6","-","+","="," ",",",";",":","'","%","#","!","$","(",")","&","*","_","[","]","{","}","/","?","<",">","£","`","¬","~"]

def encrypt(sentence):
    encryption = ""
    for letter in sentence:
        for i in range(len(plaintext)):
            if letter == plaintext[i]:
                encryption += cyphertext[i]

    return encryption

def decrypt(sentence):
    decryption = ""
    for letter in sentence:
        for i in range(len(cyphertext)):
            if letter == cyphertext[i]:
                decryption += plaintext[i]

    return decryption

x = ""
while x != "x":
    print ("Please select the the process you would like to carry out from below:")
    print ("1. Encrypting data,")
    print ("2. Decrypting data.")
    check = int(input("Please enter the index number for the process you would like to execute from above here --> "))

    if check == 1:
        sentence = str(input("\nInput sentence here --> "))
        encryption = encrypt(sentence)

        print ("\n=================================================\n")
        print (encryption)
        print ("\n=================================================\n")

    elif check == 2:
        print ("")
        sentence = str(input("Input sentence here --> "))
        decryption = decrypt(sentence)

        print ("\n=================================================\n")
        print (decryption)
        print ("\n=================================================\n")

    x = str(input("If you would like to exit, type 'x'. If not and you would like to continue, press 'enter' --> "))
