
Yoruba_Dictionary = {
    "good morning": "e kaaro",
    "good afternoon": "e kaasan",
    "good evening": "e kaale",
    "how are you": "bawo ni?",
    "i am fine": "mo wa daadaa",
    "thank you": "o se",
    "please": "jowo",
    "sorry": "ma binu",
    "yes": "beeni",
    "no": "rara",
    "water": "omi",
    "food": "ounje",
    "house": "ile",
    "money": "owo",
    "man": "okunrin",
    "woman": "obinrin",
    "child": "omo",
    "friend": "ore",
    "father": "baba",
    "mother": "mama",
    "come": "wa",
    "go": "lo",
    "eat": "jeun",
    "drink": "mu",
    "sleep": "sun",
    "keep quiet": "dake",
    "what is your name": "ki ni oruko re",
    "my name is": "oruko mi ni",
    "do you understand me": "se o ye mi",
    "goodbye": "odabo"
}

english_to_yoruba = {v: k for k, v in Yoruba_Dictionary.items()}
def translate(word, direction="yoruba_to_english"):
    if direction == "yoruba_to_english":
        return Yoruba_Dictionary.get(word.lower(), "Not found")
    elif direction == "english_to_yoruba":
        return english_to_yoruba.get(word.lower(), "Not found")
    else:
        return "Invalid direction"


if __name__ == "__main__":
    while True:
        print("\nYoruba ↔ English Dictionary")
        print("1. Yoruba → English")
        print("2. English → Yoruba")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            word = input("Enter Yoruba word: ")
            print("English:", translate(word, "yoruba_to_english"))
        elif choice == "2":
            word = input("Enter English word: ")
            print("Yoruba:", translate(word, "english_to_yoruba"))
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")