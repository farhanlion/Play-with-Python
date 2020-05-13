#This is a PygLatin and English translator.

language =""
def language_input ():
  global language
  language = raw_input('Type "p" for PygLatin output, "e" for English output: ')
  language = language.lower()
  print "\n"

#Ask for a language input
language_input()

#Check if the input is valid
while language != "p" and language != "e":
  print "<<<Please choose \"p\" or \"e\".>>>"
  #If it is not p or e, ask for the language input again
  language_input()  

original = raw_input('Enter a word: ')

if len(original) > 0 and original.isalpha():
  print original 
else:
  print 'empty or invalid input'

word = original.lower()
first = word[0]

#Translation form PygLatin to English
if language ==  "e":
  ends_with_ay = word[-2:] == "ay"
  starts_with_vowel = first =='a' or first =='e' or first =='i' or first =='o' or first =='u'
#Check if it is PygLatin or not
  if ends_with_ay and starts_with_vowel:
    print "Looks like Pig Latin!"
    first_eng = word[-3]
    eng_word = word[:-3]
    eng_word = first_eng + eng_word
    print "\n" + eng_word
    
  else:
    print "This does not look like Pig Latin."
    
#Translation form English to PygLatin
elif language == "p":
  pyg = 'ay'
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print "\n" + new_word
