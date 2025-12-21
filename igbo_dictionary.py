igbo_words = {
    "Hello":"Ndewo",
    "Thank you":"Daalu",
    "Person":"Onye",
    "House":"Ulo",
    "Children":"Umu",
    "Food":"Nri",
    "Water":"Mmiri",
    "Hand":"Aka",
    "Head":"ise",
    "Restaurant":"Ulo Oriri",
    "Vegetable":"Akwukwo",
    "Market":"Ulo ahia",
    "Tooth":"Eze",
    "Onion":"Yabasi",
    "Leg":"Ukwu",
    "Ear":"Nti",
    "Aeroplane":"Ugboelu",
    "Fish":"Azu",
    "Rice":"Osikapa"
}
if __name__ == "__main__":
    word = input("enter an igbo word: ")
    if word in igbo_words:
        print(word, "means:", igbo_words[word])
    else:
        print("word not found.")