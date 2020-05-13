def palindrome(word):
 #Removing spaces and punctuations
    word = word.lower()
    word = word.replace(" ","")
    word = word.replace(",","")
    word = word.replace(".","")
    word = word.replace("!","")
    word = word.replace("?","")
    word = word.replace("/","")
    word = word.replace("\'","")
    word_list = []
    for i in word:
        word_list.append(i)
    print word_list
    reversed_list = word_list[::-1]
    print reversed_list

    if word_list == reversed_list:
        return True
    else:
        return False

word_input = raw_input('Please Key in a word: ')

print palindrome(word_input)
