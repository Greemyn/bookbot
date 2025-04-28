import sys


def get_book_text(X):
    with open(X) as book:
        file_contents = book.read()    
    return file_contents
    
def get_num_words(X):       
    words_in_book = X.split()
    num_words =len(words_in_book)
    return num_words

def char_counter(X):
    letter_count ={}
    words_in_book = X.split()
    for word in words_in_book:
        for letter in word:
            lcase_letter = letter.lower()
            if lcase_letter in letter_count:
                letter_count[lcase_letter] += 1
            else:
                letter_count[lcase_letter] = 1
    return letter_count


def char_print(X):
    for key, value in X.items():
        print(f"{key}: {value}") 
    


book = get_book_text(sys.argv[1])
word_number = get_num_words(book)
char_dict = char_counter(book)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {word_number} total words")
print("--------- Character Count -------")
char_print(char_dict)
print("============= END ===============")

