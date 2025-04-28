import sys

arg_lenght = len(sys.argv)
if arg_lenght != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_book_text 

