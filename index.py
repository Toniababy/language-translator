from hausa_translator import hausa_dict
from yoruba_translator import Yoruba_Dictionary
from swahili import swahili_dict
from igbo_dictionary import igbo_words
# from tiv import tiv_translator

print("Welcome to the African Language Translator")
print("Choose a language:")
print("1. Hausa")
print("2. Yoruba")
print("3. igbo")
print("4. Swahili")
print("5. Tiv")

choice = input("Enter number (1-5): ")
word = input("Enter an English word: ").lower()

if choice == "1":
    print(hausa_dict(word))
elif choice == "2":
    print(Yoruba_Dictionary(word))
elif choice == "3":
    print(igbo_words(word))
elif choice == "4":
    print(swahili_dict(word))
# elif choice == "5":
#     print(translate_to_tiv(word))
else:
    print("Invalid language choice.")
