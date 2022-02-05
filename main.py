#!/usr/bin/env python3

import pyperclip


morse_alpha = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

morse_numeric = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

morse_symbol = {
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    "¿": "..-.-",
    "¡": "--...-"
}

def ischar(ch) -> bool:
    if ch.isalpha() == False and ch.isnumeric() == False:
        return True
    return False

def text_to_morse(text: str) -> str:
    morse_code = []
    for letter in text:
        if letter.isalpha():
            for code in morse_alpha:
                if letter.lower() == code:
                    # print(f"{letter} {morse_alpha[code]}") ## debugging line
                    morse_code.append(f" {morse_alpha[code]} ")
        elif letter.isnumeric():
            for code in morse_numeric:
                if letter.lower() == code:
                    # print(f"{letter} {morse_numeric[code]}") ## debugging line
                    morse_code.append(f" {morse_numeric[code]} ")
        elif ischar(letter):
            if letter == " ":
                # print(f"{letter}") ## debugging line 'just showing space character'
                morse_code.append(' / ')
            for code in morse_symbol:
                if letter.lower() == code:
                    # print(f"{letter} {morse_symbol[code]}") ## debugging line
                    morse_code.append(f" {morse_symbol[code]} ")
        else:
            raise Exception(f"{__file__}: {letter} is not supported.")

    return ''.join(morse_code)
if __name__ == "__main__":
    text: str = input("Enter Your Text: ")
    converted = text_to_morse(text)
    print(f"Your Morse Code: {converted}")
    pyperclip.copy(converted)
    print("Copied to clipboard !")

