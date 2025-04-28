
def get_book_text():
    with open("books/frankenstein.txt") as book:
        file_contents = book.read()    
    return file_contents
    
def get_num_words(X):       
    words_in_book = X.split()
    num_words =len(words_in_book)
    return f"{num_words} words found in the document"

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
    print(letter_count)

            



book = get_book_text()
word_number = get_num_words(book)
char_counter(book)

