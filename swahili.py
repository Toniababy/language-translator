swahili_dict = {
    "hello": "jambo",
    "thank you": "asante",
    "water": "maji",
    "food": "chakula",
    "friend": "rafiki",
    "love": "upendo",
    "sun": "jua",
    "moon": "mwezi",
    "home": "nyumbani",
    "school": "shule",
    "child": "mtoto",
    "man": "mwanaume",
    "woman": "mwanamke",
    "book": "kitabu",
    "earth": "dunia",
    "peace": "amani",
    "good": "nzuri",
    "bad": "mbaya",
    "one": "moja",
    "two": "mbili"
}

if __name__ == "__main__":
    word = input("Enter an English word for Swahili translation: ").strip().lower()

    if word in swahili_dict:
        print(f"✅ The Swahili translation is: {swahili_dict[word]}")
    else:
        print(f"❌ Error: The word '{word}' is not in the Swahili dictionary.")
