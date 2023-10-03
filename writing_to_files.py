fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        line = f"{fruit}\n"
        fruits_out.write(line)   # write string to file

MINIMUM_LENGTH = 22

with open('DATA/words.txt') as words_in:
    with open('longwords.txt', 'w') as longwords_out:
        for raw_word in words_in:
            word = raw_word.rstrip()
            if len(word) >= MINIMUM_LENGTH:
                longwords_out.write(raw_word)


