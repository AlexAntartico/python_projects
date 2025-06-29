#!/usr/bin/python3

def main():
    word = input("Type the word you want to check and press enter\n")
    word = list(word)

    if word == word[::-1]:
        word = "".join(word)
        print(f"The word {word} is a palindrome")
    else:
        word = "".join(word)
        print(f"The word {word} is not a palindrome")

if __name__ == "__main__":
    main()

