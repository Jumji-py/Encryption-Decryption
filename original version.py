x = ""
print ("Type in 'x' to exit the program when display is shown.")
while x != "x":
    print ("")
    print ("Please select the the process you would like to carry out from below:")
    print ("1. Encrypting data,")
    print ("2. Decrypting data.")
    check = int(input("Please enter the index number for the process you would like to execute from above here --> "))
    if check == 1:
        print ("")
        sentence = str(input("Input sentence here --> "))
        encryption = ""
        length = len(sentence)
        for count in range(length):
            letter = ""
            if sentence[count:count+1] == "a":
                letter = "p"
            elif sentence[count:count+1] == "b":
                letter = "u"
            elif sentence[count:count+1] == "c":
                letter = "x"
            elif sentence[count:count+1] == "d":
                letter = "z"
            elif sentence[count:count+1] == "e":
                letter = "r"
            elif sentence[count:count+1] == "f":
                letter = "q"
            elif sentence[count:count+1] == "g":
                letter = "o"
            elif sentence[count:count+1] == "h":
                letter = "y"
            elif sentence[count:count+1] == "i":
                letter = "v"
            elif sentence[count:count+1] == "j":
                letter = "w"
            elif sentence[count:count+1] == "k":
                letter = "s"
            elif sentence[count:count+1] == "l":
                letter = "g"
            elif sentence[count:count+1] == "m":
                letter = "d"
            elif sentence[count:count+1] == "n":
                letter = "a"
            elif sentence[count:count+1] == "o":
                letter = "t"
            elif sentence[count:count+1] == "p":
                letter = "l"
            elif sentence[count:count+1] == "q":
                letter = "c"
            elif sentence[count:count+1] == "r":
                letter = "j"
            elif sentence[count:count+1] == "s":
                letter = "i"
            elif sentence[count:count+1] == "t":
                letter = "n"
            elif sentence[count:count+1] == "u":
                letter = "e"
            elif sentence[count:count+1] == "v":
                letter = "b"
            elif sentence[count:count+1] == "w":
                letter = "k"
            elif sentence[count:count+1] == "x":
                letter = "h"
            elif sentence[count:count+1] == "y":
                letter = "f"
            elif sentence[count:count+1] == "z":
                letter = "m"
            elif sentence[count:count+1] == "A":
                letter = "P"
            elif sentence[count:count+1] == "B":
                letter = "U"
            elif sentence[count:count+1] == "C":
                letter = "X"
            elif sentence[count:count+1] == "D":
                letter = "Z"
            elif sentence[count:count+1] == "E":
                letter = "R"
            elif sentence[count:count+1] == "F":
                letter = "Q"
            elif sentence[count:count+1] == "G":
                letter = "O"
            elif sentence[count:count+1] == "H":
                letter = "Y"
            elif sentence[count:count+1] == "I":
                letter = "V"
            elif sentence[count:count+1] == "J":
                letter = "W"
            elif sentence[count:count+1] == "K":
                letter = "S"
            elif sentence[count:count+1] == "L":
                letter = "G"
            elif sentence[count:count+1] == "M":
                letter = "D"
            elif sentence[count:count+1] == "N":
                letter = "A"
            elif sentence[count:count+1] == "O":
                letter = "T"
            elif sentence[count:count+1] == "P":
                letter = "L"
            elif sentence[count:count+1] == "Q":
                letter = "C"
            elif sentence[count:count+1] == "R":
                letter = "J"
            elif sentence[count:count+1] == "S":
                letter = "I"
            elif sentence[count:count+1] == "T":
                letter = "N"
            elif sentence[count:count+1] == "U":
                letter = "E"
            elif sentence[count:count+1] == "V":
                letter = "B"
            elif sentence[count:count+1] == "W":
                letter = "K"
            elif sentence[count:count+1] == "X":
                letter = "H"
            elif sentence[count:count+1] == "Y":
                letter = "F"
            elif sentence[count:count+1] == "Z":
                letter = "M"
            elif sentence[count:count+1] == "-":
                letter = "-"
            elif sentence[count:count+1] == " ":
                letter = " "
            elif sentence[count:count+1] == ".":
                letter = "."
            elif sentence[count:count+1] == ",":
                letter = ","
            elif sentence[count:count+1] == "!":
                letter = "!"
            elif sentence[count:count+1] == "?":
                letter = "?"
            elif sentence[count:count+1] == ":":
                letter = ":"
            elif sentence[count:count+1] == "'":
                letter = "'"
            elif sentence[count:count+1] == "1":
                letter = "8"
            elif sentence[count:count+1] == "2":
                letter = "0"
            elif sentence[count:count+1] == "3":
                letter = "7"
            elif sentence[count:count+1] == "4":
                letter = "9"
            elif sentence[count:count+1] == "5":
                letter = "2"
            elif sentence[count:count+1] == "6":
                letter = "4"
            elif sentence[count:count+1] == "7":
                letter = "5"
            elif sentence[count:count+1] == "8":
                letter = "3"
            elif sentence[count:count+1] == "9":
                letter = "1"
            elif sentence[count:count+1] == "0":
                letter = "6"
    
            encryption = encryption + letter

        print ("")
        print ("=================================================")
        print ("")
        print (encryption)
        print ("")
        print ("=================================================")

    elif check == 2:
        print ("")
        sentence = str(input("Input sentence here --> "))
        decryption = ""
        length = len(sentence)
        for count in range (length):
            letter = ""
            if sentence[count:count+1] == "p":
                letter = "a"
            elif sentence[count:count+1] == "u":
                letter = "b"
            elif sentence[count:count+1] == "x":
                letter = "c"
            elif sentence[count:count+1] == "z":
                letter = "d"
            elif sentence[count:count+1] == "r":
                letter = "e"
            elif sentence[count:count+1] == "q":
                letter = "f"
            elif sentence[count:count+1] == "o":
                letter = "g"
            elif sentence[count:count+1] == "y":
                letter = "h"
            elif sentence[count:count+1] == "v":
                letter = "i"
            elif sentence[count:count+1] == "w":
                letter = "j"
            elif sentence[count:count+1] == "s":
                letter = "k"
            elif sentence[count:count+1] == "g":
                letter = "l"
            elif sentence[count:count+1] == "d":
                letter = "m"
            elif sentence[count:count+1] == "a":
                letter = "n"
            elif sentence[count:count+1] == "t":
                letter = "o"
            elif sentence[count:count+1] == "l":
                letter = "p"
            elif sentence[count:count+1] == "c":
                letter = "q"
            elif sentence[count:count+1] == "j":
                letter = "r"
            elif sentence[count:count+1] == "i":
                letter = "s"
            elif sentence[count:count+1] == "n":
                letter = "t"
            elif sentence[count:count+1] == "e":
                letter = "u"
            elif sentence[count:count+1] == "b":
                letter = "v"
            elif sentence[count:count+1] == "k":
                letter = "w"
            elif sentence[count:count+1] == "h":
                letter = "x"
            elif sentence[count:count+1] == "f":
                letter = "y"
            elif sentence[count:count+1] == "m":
                letter = "z"
            elif sentence[count:count+1] == "P":
                letter = "A"
            elif sentence[count:count+1] == "U":
                letter = "B"
            elif sentence[count:count+1] == "X":
                letter = "C"
            elif sentence[count:count+1] == "Z":
                letter = "D"
            elif sentence[count:count+1] == "R":
                letter = "E"
            elif sentence[count:count+1] == "Q":
                letter = "F"
            elif sentence[count:count+1] == "O":
                letter = "G"
            elif sentence[count:count+1] == "Y":
                letter = "H"
            elif sentence[count:count+1] == "V":
                letter = "I"
            elif sentence[count:count+1] == "W":
                letter = "J"
            elif sentence[count:count+1] == "S":
                letter = "K"
            elif sentence[count:count+1] == "G":
                letter = "L"
            elif sentence[count:count+1] == "D":
                letter = "M"
            elif sentence[count:count+1] == "A":
                letter = "N"
            elif sentence[count:count+1] == "T":
                letter = "O"
            elif sentence[count:count+1] == "L":
                letter = "P"
            elif sentence[count:count+1] == "C":
                letter = "Q"
            elif sentence[count:count+1] == "J":
                letter = "R"
            elif sentence[count:count+1] == "I":
                letter = "S"
            elif sentence[count:count+1] == "N":
                letter = "T"
            elif sentence[count:count+1] == "E":
                letter = "U"
            elif sentence[count:count+1] == "B":
                letter = "V"
            elif sentence[count:count+1] == "K":
                letter = "W"
            elif sentence[count:count+1] == "H":
                letter = "X"
            elif sentence[count:count+1] == "F":
                letter = "Y"
            elif sentence[count:count+1] == "M":
                letter = "Z"
            elif sentence[count:count+1] == "-":
                letter = "-"
            elif sentence[count:count+1] == " ":
                letter = " "
            elif sentence[count:count+1] == ".":
                letter = "."
            elif sentence[count:count+1] == ",":
                letter = ","
            elif sentence[count:count+1] == "!":
                letter = "!"
            elif sentence[count:count+1] == "?":
                letter = "?"
            elif sentence[count:count+1] == ":":
                letter = ":"
            elif sentence[count:count+1] == "'":
                letter = "'"
            elif sentence[count:count+1] == "8":
                letter = "1"
            elif sentence[count:count+1] == "0":
                letter = "2"
            elif sentence[count:count+1] == "5":
                letter = "7"
            elif sentence[count:count+1] == "9":
                letter = "4"
            elif sentence[count:count+1] == "2":
                letter = "5"
            elif sentence[count:count+1] == "4":
                letter = "6"
            elif sentence[count:count+1] == "7":
                letter = "3"
            elif sentence[count:count+1] == "3":
                letter = "8"
            elif sentence[count:count+1] == "1":
                letter = "9"
            elif sentence[count:count+1] == "6":
                letter = "0"

            decryption = decryption + letter

        print ("")
        print ("=================================================")
        print ("")
        print (decryption)
        print ("")
        print ("=================================================")

    print ("")
    x = str(input("If you would like to exit, type 'x'. If not and you would like to continue, press 'enter' --> "))