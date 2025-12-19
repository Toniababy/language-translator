hausa_dict = {
    "water": "ruwa",
    "food": "abinci",
    "house": "gida",
    "school": "makaranta",
    "book": "littafi",
    "man": "namiji",
    "woman": "mace",
    "child": "yaro",
    "sun": "rana",
    "moon": "wata",
    "dog": "kare",
    "cat": "mage",
    "car": "mota",
    "road": "hanya",
    "market": "kasuwa",
    "teacher": "malami",
    "student": "dalibi",
    "money": "kudi",
    "work": "aiki",
    "love": "so"
}

def translate_to_hausa(word):
    if word in hausa_dict:
        return hausa_dict[word]
    else:
        return "Error: word not found in Hausa dictionary."
