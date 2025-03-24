sentence = "I'm coming home"
print(sentence)

sentence = "I'm coming\nhome"
print(sentence)

sentence = "This is a sentence"
print(sentence[0])
print(sentence[17])
print(sentence[-2])   #print second last character

#example of slicing - print 1st four character follow non-inclusive i.e character at index 4 not included
print(sentence[0:4])
print(sentence[0:3]) #hence index3 is not included

#assignment print is using slicing
print(sentence[5:7])

characters = "abcdefg"
print(characters[0:7:2]) # 3rd value is step function, it skips the character at index 2,4,6,8 hence aceg

#assignment print characters from d
print(characters[3:])
print(characters[-4:])
