from hausa import hausa_translator
from yoruba import yoruba_translator
# from igbo import translate_to_igbo
# from efik import translate_to_efik
# from tiv import translate_to_tiv

print("Welcome to the African Language Translator")
print("Choose a language:")
print("1. Hausa")
print("2. Yoruba")
print("3. Igbo")
print("4. Efik")
print("5. Tiv")

choice = input("Enter number (1-5): ")
word = input("Enter an English word: ").lower()

if choice == "1":
    print(hausa_translator(word))
elif choice == "2":
    print(yoruba_translator(word))
# elif choice == "3":
#     print(translate_to_igbo(word))
# elif choice == "4":
#     print(translate_to_efik(word))
# elif choice == "5":
#     print(translate_to_tiv(word))
else:
    print("Invalid language choice.")
