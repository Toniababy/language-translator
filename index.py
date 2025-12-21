from hausa_translator import hausa_dict
from yoruba_translator import Yoruba_Dictionary
from swahili import swahili_dict
from igbo_dictionary import igbo_words
from tiv import tiv_translator

print("Welcome to the African Language Translator")
print("1. Hausa | 2. Yoruba | 3. Igbo | 4. Swahili | 5. Tiv")

choice = input("Enter number (1-5): ")
word = input("Enter an English word: ").lower().strip()

# 1. HAUSA
if choice == "1":
    if word in hausa_dict:
        print(f"Hausa: {hausa_dict[word]}")
    else:
        print(f"Error: {word} not found in Hausa.")

# 2. YORUBA
elif choice == "2":
    if word in Yoruba_Dictionary:
        print(f"Yoruba: {Yoruba_Dictionary[word]}")
    else:
        print(f"Error: {word} not found in Yoruba.")

# 3. IGBO
elif choice == "3":
    if word in igbo_words:
        print(f"Igbo: {igbo_words[word]}")
    else:
        print(f"Error: {word} not found in Igbo.")

# 4. SWAHILI
elif choice == "4":
    if word in swahili_dict:
        print(f"Swahili: {swahili_dict[word]}")
    else:
        print(f"Error: {word} not found in Swahili.")

# 5. TIV
elif choice == "5":
    if word in tiv_translator:
        print(f"Tiv: {tiv_translator[word]}")
    else:
        print(f"Error: {word} not found in Tiv.")

else:
    print("Invalid language choice.")