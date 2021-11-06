#!/usr/bin/env python3

import json

# the previous functions were basically doing the same thing
def crypt(task, sentence, keys) -> str:
    # keys parameter is to allow changing decryption keys (pass a dictionary)
    result = ""
    for letter in sentence:
        for key in keys:
            if task == "encrypt":
                if letter == key:
                    result += keys[key]
            elif task == "decrypt":
                # inverse procedure of encrypting
                if letter == keys[key]:
                    result += key
            else:
                raise ValueError("Invalid encryption task assigned")

    return result


def main():
    # converts json-stored keys needed for decryption to a python dictionary
    with open("keys.json", "r") as f:
        keys = json.load(f)

    # boolean flags are more pythonic than x = ""
    active = True

    # main loop
    while active:
        print("\nPlease select the the process you would like to carry out from below:")
        print("1. Encrypting data,")
        print("2. Decrypting data.")

        # prompt till the option is valid, if the number isn't defined, skip
        try:
            usr_input = int(
                input(
                    "Please enter the index number for the process you would like to execute from above here --> "
                )
            )
        except ValueError:
            continue

        if usr_input == 1:
            sentence = str(input("\nInput sentence here --> "))
            encryption = crypt("encrypt", sentence, keys)

            print("\n=================================================\n")
            print(encryption)
            print("\n=================================================\n")

        elif usr_input == 2:
            sentence = str(input("\nInput sentence here --> "))
            decryption = crypt("decrypt", sentence, keys)

            print("\n=================================================\n")
            print(decryption)
            print("\n=================================================\n")

        keep_running = str(
            input(
                "If you would like to exit, type 'x'. If not and you would like to continue, press 'enter' --> "
            )
        )

        if keep_running == "x":
            active = False


if __name__ == "__main__":
    main()
