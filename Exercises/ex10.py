def ex10():
    vowels = 0
    consonants = 0
    
    word = input("Enter string: ").lower()

    for letter in word:
        if vowelfind(letter):
            vowels += 1
        else:
            consonants += 1

    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")


def vowelfind(vowel) -> bool:
    match vowel:
        case "a":
            return True
        case "e":
            return True
        case "i":
            return True
        case "o":
            return True
        case "u":
            return True
    return False


if __name__ == '__main__':
    ex10()