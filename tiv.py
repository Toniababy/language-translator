
tiv_translator = {
    "hello": "msugh",
    "thank you": "msugh kpa",
    "water": "mnger",
    "food": "kwaghyan",
    "house": "iou",
    "come": "va",
    "go": "yem",
    "eat": "ya kwaghyan",
    "drink": "ma",
    "man": "nomsoor",
    "woman": "kwase",
    "child": "wan",
    "sun": "iyange",
    "moon": "wer",
    "God": "Aondo",
    "money": "inyaregh",
    "market": "kasua",
    "road": "gbenda",
    "one": "môm",
    "two": "uhaar"
}
if __name__ == "__main__":
    word = input("Enter an English word for Tiv translation: ").strip().lower()

    if word in tiv_translator:
        print(f"✅ The Tiv translation is: {tiv_translator[word]}")
    else:
        print(f"❌ Error: The word '{word}' is not in the Tiv dictionary.")