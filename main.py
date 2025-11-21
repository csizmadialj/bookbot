import sys
from stats import get_num_words, get_num_chars, get_sorted_list_of_dict

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = args[1]

    wordcount = get_num_words(book)
    charcount = get_num_chars(book)
    sorted_chars = get_sorted_list_of_dict(charcount)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
if __name__=="__main__":
    main()