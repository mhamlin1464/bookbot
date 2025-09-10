import sys
from stats import get_amount_of_words, get_amount_of_characters, sort_dictionary
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    number_words = get_amount_of_words(text)
    number_characters = get_amount_of_characters(text)
    #print(f"{number_words} words found in the document")
    #print(f"{number_characters}")
    my_list = sort_dictionary(number_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
    for x in my_list:
        if x["char"].isalpha():
            print(f"{x["char"]}: {x["num"]}")
    print("============= END ===============")
main()