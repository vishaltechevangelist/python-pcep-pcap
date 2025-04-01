from utils.utility import ListAndCharShortner
from utils.utility import DictionaryShortner

myshortner = ListAndCharShortner("This is shortener")
myshortner.print_original_items()
myshortner.print_shortened_items()

mydictshortner = DictionaryShortner({1:"Vishal", 2:"Priyanka", 3:"Adharv", 4:"Advik"})
mydictshortner.print_original_items()
mydictshortner.print_shortened_items()