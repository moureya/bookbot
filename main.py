import sys
print(sys.argv)

from stats import get_book_text 
from stats import character_sort

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_book_text(sys.argv[1])
    sorted_chars = character_sort(sys.argv[1])
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
main()

