
Yoruba_Dictionary = {
    "e kaaro": "good morning",
    "e kaasan": "good afternoon",
    "e kaale": "good evening",
    "bawo ni?": " how are you",
    "mo wa daadaa":"i am fine",
    "o se": "thank you",
    "jowo": "please",
    "ma binu": "sorry",
    "beeni": "yes",
    "rara": "no",
    "omi": "water",
    "ounje": "food",
    "ile": "house",
    "owo": "money",
    "okunrin": "man",
    "obinrin": "woman",
    "omo": "child",
    "ore": "friend",
    "baba": "father",
    "mama": "mother",
    "wa": "come",
    "lo": "go",
    "jeun": "eat",
    "mu": "drink",
    "sun": "sleep",
    "dake": "keep quiet",
    "ki ni oruko re": "what is your name",
    "oruko mi ni": "my name is",
    "se o ye mi": "do you understand me",
    "odabo": "goodbye"
}
print("e káàrọ̀ – good morning")
print("e káàsán – good afternoon")
print("e káalẹ́ – good evening")
print("báwo ni? – how are you?")
print("mo wa dáadáa – i am fine")
print("o ṣe – thank you")
print("jọwọ – please")
print("má bínú – sorry")
print("beẹ̀ni – yes")
print("rárá – no")
print("omi – Water")
print("ounjẹ – food")
print("ilé – house")
print("owó – money")
print("Ọkùnrin – man")
print("obìnrin – woman")
print("omọ – child")
print("orẹ – friend")
print("baba – father")
print("mama – mother")
print("wá – come")
print("lọ – go")
print("jẹun – eat")
print("mu – drink")
print("sùn – sleep")
print("dákẹ́ – keep quiet")
print("kí ni orúkọ rẹ? – what is your name?")
print("orúkọ mi ni… – my name is...")
print("Ṣé o ye mi? – do you understand me?")
print("odàbọ̀ – goodbye")
english_to_yoruba = {v: k for k, v in Yoruba_Dictionary.items()}
def translate(word, direction="yoruba_to_english"):
    if direction == "yoruba_to_english":
        return Yoruba_Dictionary.get(word.lower(), "Not found")
    elif direction == "english_to_yoruba":
        return english_to_yoruba.get(word.lower(), "Not found")
    else:
        return "Invalid direction"
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
            print("Invalid choice. Try again.")