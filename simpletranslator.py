
def translator(phrase):
    translation = ""
    for letters in phrase:
        if letters.upper() in "BCDFGHJKLMNPQRSTVWXYZ":
            if letters.islower():
                translation = translation + "#"
            else: 
                translation = translation + "@"
        elif letters.lower() in "aeiou":
            if letters.isupper():
                translation = translation + "$"
            else: 
               translation = translation + "?"
        else:
            translation = translation + letters
    return translation

print(translator(input("Enter words: ")))
#it is ok
