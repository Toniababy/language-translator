igbo_words = {
    "hello":"Ndewo",
    "thank you":"Daalu",
    "person":"Onye",
    "house":"Ulo",
    "children":"Umu",
    "food":"Nri",
    "water":"Mmiri",
    "hand":"Aka",
    "head":"ise",
    "restaurant":"Ulo_Oriri",
    "vegetable":"Akwukwo",
    "market":"Ulo ahia",
    "tooth":"Eze",
    "onion":"Yabasi",
    "leg":"Ukwu",
    "ear":"Nti",
    "aeroplane":"Ugboelu",
    "fish":"Azu",
    "rice":"Osikapa"
}
if __name__ == "__main__":
    word = input("enter an igbo word: ")
    if word in igbo_words:
        print(word, "means:", igbo_words[word])
    else:
        print("word not found.")