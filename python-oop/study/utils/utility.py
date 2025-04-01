class Shortner:
    def __init__(self, items):
        self.original_items = items

    def print_original_items(self):
        print(self.original_items)

# This child class can shorten the string & list, not dictionary
class ListAndCharShortner(Shortner):
    def print_shortened_items(self):
        print(self.original_items[0:3])

# hence dictionary class
class DictionaryShortner(Shortner):
    def print_shortened_items(self):
        new_dict = {}
        dict = self.original_items
        for (key, value) in dict.items():
            if key <= 3:
                new_dict[key] = value
        print(new_dict)

