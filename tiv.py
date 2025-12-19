# # Tiv Dictionary for Button Phone
# # Optimized for keypad navigation (Nokia-style phones)
#
# import json
# import os
# from datetime import datetime
#
#
# class TivDictionaryButtonPhone:
#     def _init_(self):
#         self.dictionary = {
#             'greeting': [
#                 ('hello', 'mngu', 'm-n-gu'),
#                 ('good morning', 'ula', 'u-la'),
#                 ('how are you?', 'kwagh u?', 'kwagh u'),
#                 ('I am fine', 'm sha', 'm sha'),
#                 ('thank you', 'u doo', 'u doo'),
#                 ('please', 'biko', 'bi-ko'),
#                 ('goodbye', 'nahan', 'na-han'),
#                 ('welcome', 'ngum', 'ngum'),
#             ],
#             'family': [
#                 ('father', 'ter', 'ter'),
#                 ('mother', 'ngoh', 'ngoh'),
#                 ('child', 'wan', 'wan'),
#                 ('brother', 'nyityo', 'nyi-tyo'),
#                 ('sister', 'kristyol', 'kris-tyol'),
#                 ('husband', 'or', 'or'),
#                 ('wife', 'sha', 'sha'),
#                 ('grandfather', 'torgishi', 'tor-gi-shi'),
#                 ('grandmother', 'ngorgishi', 'ngor-gi-shi'),
#             ],
#             'food': [
#                 ('food', 'nyin', 'nyin'),
#                 ('water', 'mba', 'mba'),
#                 ('meat', 'inyam', 'in-yam'),
#                 ('fish', 'ingough', 'in-gogh'),
#                 ('rice', 'sha', 'sha'),
#                 ('beans', 'agwa', 'ag-wa'),
#                 ('yam', 'ji', 'ji'),
#                 ('salt', 'mnyian', 'm-nyi-an'),
#                 ('oil', 'mav', 'mav'),
#             ],
#             'animals': [
#                 ('dog', 'avange', 'a-van-ge'),
#                 ('cat', 'mwa', 'mwa'),
#                 ('goat', 'tiv', 'tiv'),
#                 ('cow', 'na', 'na'),
#                 ('bird', 'ikyev', 'i-kyev'),
#                 ('chicken', 'kogh', 'kogh'),
#                 ('fish', 'ingough', 'in-gogh'),
#                 ('snake', 'ikura', 'i-ku-ra'),
#             ],
#             'numbers': [
#                 ('one', 'mọn', 'mon'),
#                 ('two', 'har', 'har'),
#                 ('three', 'tat', 'tat'),
#                 ('four', 'nyiin', 'nyiin'),
#                 ('five', 'tan', 'tan'),
#                 ('six', 'teratar', 'te-ra-tar'),
#                 ('seven', 'tumbul', 'tum-bul'),
#                 ('eight', 'ninis', 'ni-nis'),
#                 ('nine', 'sesew', 'se-sew'),
#                 ('ten', 'puu', 'puu'),
#             ],
#             'nature': [
#                 ('sun', 'yough', 'yogh'),
#                 ('moon', 'ngii', 'ngi-i'),
#                 ('star', 'kyegh', 'kyegh'),
#                 ('rain', 'yav', 'yav'),
#                 ('tree', 'ityo', 'i-tyo'),
#                 ('stone', 'ikyura', 'i-kyu-ra'),
#                 ('river', 'afa', 'a-fa'),
#                 ('mountain', 'gba', 'gba'),
#                 ('road', 'kunya', 'ku-nya'),
#             ],
#             'verbs': [
#                 ('go', 'yange', 'yan-ge'),
#                 ('come', 'timen', 'ti-men'),
#                 ('eat', 'yam', 'yam'),
#                 ('drink', 'na', 'na'),
#                 ('see', 'hono', 'ho-no'),
#                 ('hear', 'nor', 'nor'),
#                 ('speak', 'ngohol', 'ngo-hol'),
#                 ('give', 'ngee', 'ngee'),
#                 ('take', 'mba', 'mba'),
#                 ('sleep', 'tindi', 'tin-di'),
#             ]
#         }
#
#         self.categories = list(self.dictionary.keys())
#         self.current_category_index = 0
#         self.current_word_index = 0
#         self.history = []
#         self.favorites = []
#         self.load_data()
#
#     def load_data(self):
#         """Load saved data if available"""
#         try:
#             if os.path.exists('tiv_data.json'):
#                 with open('tiv_data.json', 'r') as f:
#                     data = json.load(f)
#                     self.favorites = data.get('favorites', [])
#                     self.history = data.get('history', [])
#         except:
#             pass
#
#     def save_data(self):
#         """Save user data"""
#         data = {
#             'favorites': self.favorites,
#             'history': self.history
#         }
#         with open('tiv_data.json', 'w') as f:
#             json.dump(data, f)
#
#     def clear_screen(self):
#         """Clear screen (simulated for button phone)"""
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print("=" * 20)
#
#     def display_menu(self):
#         """Main menu display"""
#         self.clear_screen()
#         print("TIV DICTIONARY")
#         print("=" * 20)
#         print("1. Browse by Category")
#         print("2. Search Word")
#         print("3. History")
#         print("4. Favorites")
#         print("5. Quiz Mode")
#         print("6. Settings")
#         print("7. Exit")
#         print("=" * 20)
#         print("Press 1-7 to select")
#
#     def browse_category_menu(self):
#         """Display categories for browsing"""
#         self.clear_screen()
#         print("BROWSE CATEGORIES")
#         print("=" * 20)
#
#         for i, category in enumerate(self.categories, 1):
#             if i == 10:
#                 print("0. " + category.capitalize())
#             else:
#                 print(f"{i}. {category.capitalize()}")
#
#         print("=" * 20)
#         print("* Back   # Next Page")
#
#     def display_words_in_category(self, category_index):
#         """Display words in selected category"""
#         category = self.categories[category_index]
#         words = self.dictionary[category]
#
#         self.clear_screen()
#         print(f"CATEGORY: {category.upper()}")
#         print("=" * 20)
#
#         # Display 5 words at a time for button phone screen
#         start_idx = self.current_word_index
#         end_idx = min(start_idx + 5, len(words))
#
#         for i in range(start_idx, end_idx):
#             eng, tiv, pron = words[i]
#             print(f"{i - start_idx + 1}. {eng}")
#             print(f"   Tiv: {tiv}")
#             print(f"   Pron: {pron}")
#             print()
#
#         print(f"Words {start_idx + 1}-{end_idx} of {len(words)}")
#         print("=" * 20)
#         print("1-5: Select word")
#         print("8: Up    2: Down")
#         print("*: Back  #: Fav")
#
#     def search_menu(self):
#         """Search interface for button phone"""
#         self.clear_screen()
#         print("SEARCH WORD")
#         print("=" * 20)
#         print("Type word (use keypad):")
#         print()
#         print("2:abc 3:def 4:ghi 5:jkl")
#         print("6:mno 7:pqrs 8:tuv 9:wxyz")
#         print("0:space  *:clear  #:search")
#         print("=" * 20)
#
#         # Keypad mapping
#         keypad = {
#             '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
#             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
#             '0': ' '
#         }
#
#         search_word = ""
#         while True:
#             print(f"\nSearch: {search_word}")
#             key = input("Press key: ").strip()
#
#             if key == '#':
#                 # Search
#                 if search_word:
#                     self.perform_search(search_word)
#                     break
#             elif key == '*':
#                 # Clear/Back
#                 if search_word:
#                     search_word = search_word[:-1]
#                     self.clear_screen()
#                     print("SEARCH WORD")
#                     print("=" * 20)
#                     print("Type word (use keypad):")
#                     print()
#                     print("2:abc 3:def 4:ghi 5:jkl")
#                     print("6:mno 7:pqrs 8:tuv 9:wxyz")
#                     print("0:space  *:backspace  #:search")
#                     print("=" * 20)
#                 else:
#                     break
#             elif key in keypad:
#                 # Handle multi-tap
#                 if key in '23456789':
#                     letters = keypad[key]
#                     print(f"Press {key} for: {letters}")
#                     # For simplicity, just take first letter
#                     # In real implementation, handle multi-tap timing
#                     search_word += letters[0]
#                     self.clear_screen()
#                     print("SEARCH WORD")
#                     print("=" * 20)
#                     print("Type word (use keypad):")
#                     print()
#                     print("2:abc 3:def 4:ghi 5:jkl")
#                     print("6:mno 7:pqrs 8:tuv 9:wxyz")
#                     print("0:space  *:backspace  #:search")
#                     print("=" * 20)
#                 elif key == '0':
#                     search_word += ' '
#             else:
#                 print("Invalid key!")
#
#     def perform_search(self, search_term):
#         """Search through dictionary"""
#         search_term = search_term.lower()
#         results = []
#
#         for category in self.categories:
#             for eng, tiv, pron in self.dictionary[category]:
#                 if (search_term in eng.lower() or
#                         search_term in tiv.lower() or
#                         search_term in pron.lower()):
#                     results.append((eng, tiv, pron, category))
#
#         self.display_search_results(results)
#
#     def display_search_results(self, results):
#         """Display search results"""
#         if not results:
#             self.clear_screen()
#             print("SEARCH RESULTS")
#             print("=" * 20)
#             print("No results found")
#             input("\nPress any key to continue...")
#             return
#
#         self.clear_screen()
#         print("SEARCH RESULTS")
#         print("=" * 20)
#
#         # Show first 3 results
#         for i, (eng, tiv, pron, cat) in enumerate(results[:3], 1):
#             print(f"{i}. {eng}")
#             print(f"   Tiv: {tiv}")
#             print(f"   Cat: {cat}")
#             print()
#
#         if len(results) > 3:
#             print(f"... and {len(results) - 3} more")
#
#         print("=" * 20)
#         print("1-3: Select result")
#         print("*: New search")
#         print("#: Main menu")
#
#         choice = input("Select: ").strip()
#         if choice in ['1', '2', '3']:
#             idx = int(choice) - 1
#             if idx < len(results):
#                 eng, tiv, pron, cat = results[idx]
#                 self.display_word_detail(eng, tiv, pron, cat)
#                 # Add to history
#                 self.history.insert(0, {
#                     'english': eng,
#                     'tiv': tiv,
#                     'time': datetime.now().strftime("%H:%M")
#                 })
#                 if len(self.history) > 10:
#                     self.history = self.history[:10]
#                 self.save_data()
#         elif choice == '*':
#             self.search_menu()
#
#     def display_word_detail(self, english, tiv, pronunciation, category):
#         """Display detailed view of a word"""
#         while True:
#             self.clear_screen()
#             print("WORD DETAIL")
#             print("=" * 20)
#             print(f"English: {english}")
#             print(f"Tiv: {tiv}")
#             print(f"Pronunciation: {pronunciation}")
#             print(f"Category: {category}")
#             print("=" * 20)
#
#             # Check if in favorites
#             is_fav = any(fav['english'] == english for fav in self.favorites)
#
#             print("Options:")
#             print("1. Hear pronunciation")
#             print(f"2. {'Remove from' if is_fav else 'Add to'} Favorites")
#             print("3. Similar words")
#             print("4. Back")
#             print("=" * 20)
#
#             choice = input("Select (1-4): ").strip()
#
#             if choice == '1':
#                 self.clear_screen()
#                 print(f"Pronunciation: {pronunciation}")
#                 print("\nSay: " + pronunciation.replace('-', ' '))
#                 input("\nPress any key...")
#             elif choice == '2':
#                 if is_fav:
#                     self.favorites = [f for f in self.favorites if f['english'] != english]
#                     print("Removed from favorites!")
#                 else:
#                     self.favorites.append({
#                         'english': english,
#                         'tiv': tiv,
#                         'pronunciation': pronunciation,
#                         'category': category
#                     })
#                     print("Added to favorites!")
#                 self.save_data()
#                 input("\nPress any key...")
#             elif choice == '3':
#                 self.show_similar_words(english, category)
#             elif choice == '4':
#                 break
#
#     def show_similar_words(self, current_word, category):
#         """Show other words in same category"""
#         words = self.dictionary.get(category, [])
#         similar = [w for w in words if w[0] != current_word][:5]
#
#         self.clear_screen()
#         print(f"MORE {category.upper()} WORDS")
#         print("=" * 20)
#
#         for i, (eng, tiv, pron) in enumerate(similar, 1):
#             print(f"{i}. {eng}")
#             print(f"   Tiv: {tiv}")
#             print()
#
#         print("=" * 20)
#         print("1-5: Select word")
#         print("*: Back")
#
#         choice = input("Select: ").strip()
#         if choice in ['1', '2', '3', '4', '5']:
#             idx = int(choice) - 1
#             if idx < len(similar):
#                 eng, tiv, pron = similar[idx]
#                 self.display_word_detail(eng, tiv, pron, category)
#
#     def view_history(self):
#         """View search history"""
#         if not self.history:
#             self.clear_screen()
#             print("HISTORY")
#             print("=" * 20)
#             print("No history yet")
#             input("\nPress any key...")
#             return
#
#         self.clear_screen()
#         print("RECENT HISTORY")
#         print("=" * 20)
#
#         for i, item in enumerate(self.history[:5], 1):
#             print(f"{i}. {item['english']}")
#             print(f"   Tiv: {item['tiv']}")
#             print(f"   Time: {item['time']}")
#             print()
#
#         print("=" * 20)
#         print("1-5: Select item")
#         print("*: Clear history")
#         print("#: Main menu")
#
#         choice = input("Select: ").strip()
#
#         if choice in ['1', '2', '3', '4', '5']:
#             idx = int(choice) - 1
#             if idx < len(self.history):
#                 item = self.history[idx]
#                 # Find complete word info
#                 for category in self.categories:
#                     for eng, tiv, pron in self.dictionary[category]:
#                         if eng == item['english']:
#                             self.display_word_detail(eng, tiv, pron, category)
#                             break
#         elif choice == '*':
#             self.history = []
#             self.save_data()
#             print("History cleared!")
#             input("\nPress any key...")
#
#     def view_favorites(self):
#         """View favorite words"""
#         if not self.favorites:
#             self.clear_screen()
#             print("FAVORITES")
#             print("=" * 20)
#             print("No favorites yet")
#             input("\nPress any key...")
#             return
#
#         self.clear_screen()
#         print("FAVORITE WORDS")
#         print("=" * 20)
#
#         for i, fav in enumerate(self.favorites[:5], 1):
#             print(f"{i}. {fav['english']}")
#             print(f"   Tiv: {fav['tiv']}")
#             print(f"   Cat: {fav['category']}")
#             print()
#
#         print("=" * 20)
#         print("1-5: Select favorite")
#         print("*: Remove all")
#         print("#: Main menu")
#
#         choice = input("Select: ").strip()
#
#         if choice in ['1', '2', '3', '4', '5']:
#             idx = int(choice) - 1
#             if idx < len(self.favorites):
#                 fav = self.favorites[idx]
#                 self.display_word_detail(fav['english'], fav['tiv'],
#                                          fav['pronunciation'], fav['category'])
#         elif choice == '*':
#             self.favorites = []
#             self.save_data()
#             print("All favorites removed!")
#             input("\nPress any key...")
#
#     def quiz_mode(self):
#         """Simple quiz game"""
#         self.clear_screen()
#         print("QUIZ MODE")
#         print("=" * 20)
#         print("Test your Tiv knowledge!")
#         print()
#         print("1. English → Tiv")
#         print("2. Tiv → English")
#         print("3. Pronunciation")
#         print("4. Back")
#         print("=" * 20)
#
#         choice = input("Select (1-4): ").strip()
#
#         if choice == '1':
#             self.quiz_english_to_tiv()
#         elif choice == '2':
#             self.quiz_tiv_to_english()
#         elif choice == '3':
#             self.quiz_pronunciation()
#
#     def quiz_english_to_tiv(self):
#         """English to Tiv quiz"""
#         score = 0
#         total = 5
#
#         for i in range(total):
#             # Pick random word from any category
#             import random
#             category = random.choice(self.categories)
#             eng, tiv, pron = random.choice(self.dictionary[category])
#
#             # Generate 3 wrong options + correct
#             options = [tiv]
#             while len(options) < 4:
#                 wrong_cat = random.choice(self.categories)
#                 wrong_word = random.choice(self.dictionary[wrong_cat])
#                 if wrong_word[1] not in options:
#                     options.append(wrong_word[1])
#
#             random.shuffle(options)
#             correct_idx = options.index(tiv)
#
#             self.clear_screen()
#             print(f"QUIZ {i + 1}/{total}")
#             print("=" * 20)
#             print(f"What is '{eng}' in Tiv?")
#             print()
#
#             for j, opt in enumerate(options, 1):
#                 print(f"{j}. {opt}")
#
#             print("=" * 20)
#             print(f"Score: {score}/{i}")
#
#             try:
#                 answer = int(input("Your answer (1-4): ").strip())
#                 if answer == correct_idx + 1:
#                     print("✓ Correct!")
#                     score += 1
#                 else:
#                     print(f"✗ Wrong! Correct: {tiv}")
#                 input("\nPress any key...")
#             except:
#                 break
#
#         self.clear_screen()
#         print("QUIZ COMPLETE!")
#         print("=" * 20)
#         print(f"Your score: {score}/{total}")
#         print(f"Percentage: {(score / total) * 100:.0f}%")
#         input("\nPress any key...")
#
#     def settings_menu(self):
#         """Settings menu"""
#         self.clear_screen()
#         print("SETTINGS")
#         print("=" * 20)
#         print("1. Reset History")
#         print("2. Reset Favorites")
#         print("3. About")
#         print("4. Back")
#         print("=" * 20)
#
#         choice = input("Select (1-4): ").strip()
#
#         if choice == '1':
#             self.history = []
#             self.save_data()
#             print("History reset!")
#             input("\nPress any key...")
#         elif choice == '2':
#             self.favorites = []
#             self.save_data()
#             print("Favorites reset!")
#             input("\nPress any key...")
#         elif choice == '3':
#             self.clear_screen()
#             print("TIV DICTIONARY")
#             print("=" * 20)
#             print("Version: 1.0")
#             print("For Button Phones")
#             print("Designed for Tiv")
#             print("language learners")
#             print()
#             print("Kaa nahan! (Goodbye!)")
#             input("\nPress any key...")
#
#     def run(self):
#         """Main application loop"""
#         while True:
#             self.display_menu()
#             choice = input("Select: ").strip()
#
#             if choice == '1':
#                 # Browse by category
#                 self.browse_category_menu()
#                 cat_choice = input("Select c