import sys #used for opening and reading book files
from stats import get_word_count, sort_char #defs imported from stats.py

#main structure of terminal output and variable holders
def main():  
    text = get_book_text()
    word_count = get_word_count(text)
    char_num = sort_char(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_num:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

#bookpath found and files opened using sys
def get_book_text(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(book_path, 'r') as file:
        content = file.read()
    return content

#main callback and false start protection
if __name__ == "__main__":
    main()