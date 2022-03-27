class Dictionary:
    def __init__(self):
        self.words_dict = {}
        self.options_dict = {
                             "1": ("Add a word to the dict", self.insert_new_word),
                             "2": ("find meaning of a word", self.find_meaning),
                             "3": ("delete word", self.delete_word),
                             "4": ("print dictionary", self.print_all_dict),
                             "5": ("exit program", self.exit)
                             }
        self.run = False

    def insert_new_word(self):
        word, existing_meaning = self._get_word()
        if  not word:
            meaning = input("what is the meaning of this word")
            return f"The word {word} with the meaning {meaning} has added to the dictionary"
        else:
            return f"The word {word} is already exists and has the meaning {existing_meaning}"

    def find_meaning(self):
        # This function find the meaning of a word
        word, meaning = self._get_word()
        if word:
            return True, f"The meaning of the word {word} is {meaning}"
        else:
            return False, f"The word {word} is does not exist in the dictionary"

    def delete_word(self):
        word, meaning = self._get_word()
        if word:
            self.words_dict.pop(word)
            return True, f"The meaning of the word {word} has deleted seccessfuly"
        else:
            return False, f"The word {word} is does not exist in the dictionary"

    def print_all_dict(self):
        for i, (word, meaning) in enumerate(self.words_dict):
            print(f"{i}: {word} - {meaning}")

    def _get_word(self):
        word = input("what is the word: ")
        if self.words_dict[word]:
            return word, self.words_dict[word]
        else:
            return None, None

    def exit(self):
        self.run = False

    def print_menu(self):
        print("---Not implemented yet---")

    def add_new_option(self):
        pass

    def start(self):
        while self.run:
            self.print_menu()
            command = input("What is your command? ")
            lambda: self.options_dict[command][1]()
