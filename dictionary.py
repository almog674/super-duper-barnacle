class Dictionary:
    """
    An English-Hebrew dictionary with 5 default option
    1. add new word to the dictionary
    2. find the meaning of a word
    3. delete a word
    4. print the whole dictionary
    5. stop the running of the dictionary

    It has also a dynamic option system which you can use to add your own functions with the method "add_new_option"

    To start using the dictionary -> please call the "start" method
    """
    def __init__(self):
        self.words_dict = {}
        self.option_file = open('options.txt', 'r')
        self.options = []  
        self.run = False

    def insert_new_word(self):
        word, existing_meaning = self._get_word()
        if not existing_meaning: 
            # the word does not in the dict -> takes the meaning and add it
            meaning = input("what is the meaning of this word? ")
            self.words_dict[word] = meaning
            return f"[Success]: The word {word} with the meaning {meaning} has added to the dictionary"
        else:
            # the word does in the dict -> return a message to the user
            return f"[Failed]: The word {word} is already exists and has the meaning {existing_meaning}"

    def find_meaning(self):
        word, meaning = self._get_word()
        if meaning:
            # the word does in the dict -> return it's meaning
            return f"[Success]: The meaning of the word {word} is {meaning}"
        else:
            # the word does not in the dict -> return a message to the user
            return f"[Failed]: The word {word} is does not exist in the dictionary"

    def delete_word(self):
        word, meaning = self._get_word()
        if meaning:
            # the word does in the dict -> delete it
            self.words_dict.pop(word)
            return f"[Success]: The meaning of the word {word} has deleted seccessfuly"
        else:
            # the word does not in the dict -> return a message to the user
            return f"[Failed]: The word {word} is does not exist in the dictionary"

    def print_all_dict(self):
        # Printing the menu in the foramt -> index: word - meaning
        print("printing all the dictionary")
        for i, word in enumerate(self.words_dict):
            print(f"{i}: {word} - {self.words_dict[word]}")
        print("\n")
    
    def exit(self):
        # Stops the running of the dictionary loop
        self.option_file.close()
        self.run = False

    def _get_word(self):
        # Takes a word from the user and checks if it exist in the dictionary -> return the word & it's meaning
        word = input("what is the word: ")
        if word in self.words_dict:
            return word, self.words_dict[word]
        else:
            return word, None

    def print_menu(self):
        # Printing the menu in the foramt -> command_number: function_description
        print("\t  Options Menu\n")
        for option in self.options:
            print(f"{option[0]}: {option[2]}")

    def add_new_option(self, option_name, option_function, option_des, mode = 'a'):
        """
        This function adds a new option to the menu

        Parameters:
        option_name: what is the name of this option
        option_function: the function his option use
        option_des: description which will be shown in the menu
        mode: the mode which we use in the file "options.txt"

        1) Open the file and wrie the new option
        2) Set the option as a new attribute for this class
        """
        with open('options.txt', mode) as f:
            f.write(f"{option_name}: {option_des}\n")
        setattr(self, option_name, option_function)

    def _initialize_options(self):
        # Adds the 5 default options for our dictionary
        self.add_new_option('add_word', self.insert_new_word, 'Insert new word to the dictionary', mode = 'w')
        self.add_new_option('get_meaning', self.find_meaning, 'Get the meaning of a word')
        self.add_new_option('delete_word', self.delete_word, 'Delete a word from the dictionary')
        self.add_new_option('print_dict', self.print_all_dict, 'Print all the dictionary')
        self.add_new_option('exit', self.exit, 'Exit_the program')

    def _format_option(self, index, option):
        # Format every option to be a tuple of (index, function, description)
        option = option.split(':')
        option[1] = option[1].replace('\n', '')
        option = (index, option[0], option[1])
        return option

    def _read_options(self):
        # Reads the option file
        self.option_lines = self.option_file.readlines()
        # Format the options and store it in the array
        self.options = [self._format_option(index, option) for index, option in enumerate(self.option_lines)]

    def start(self):
        # initialize the options
        self._initialize_options()
        self._read_options()

        self.run = True
        while self.run:
            self.print_menu()
            # takes a command from the user
            command = input("command: ")
            print("\n")
            # get the function assosiated with this command
            our_function = self.options[int(command)][1]

            # if there any results -> prints them
            result = getattr(self, our_function)()
            if result:
                print(result)