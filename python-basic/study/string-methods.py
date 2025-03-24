sentence = "vishal is just brushing python skills"
sentence = sentence.upper() # upper method return string type
print(sentence)

lower_sentence = sentence.lower()
print(lower_sentence)

print(sentence.capitalize()) # upper case the 1st character of string and lowercase everything

digit_sentence = "123456"
print(digit_sentence.isdigit()) # return True
print(lower_sentence.isdigit()) # return False
print(digit_sentence.isnumeric()) # return True

print("########")
alphanum = "1st is the winner"
print(alphanum.isalnum()) # only letter and number i.e no special character (like space, _, -, %

alphanum = "1st"
print(alphanum.isalnum())

print(digit_sentence.startswith("123"))
print(digit_sentence.endswith("8")) # return False
print(digit_sentence.startswith("45", 3)) # string at index 3 starts with 45
