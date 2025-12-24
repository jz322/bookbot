import sys
from stats import count_words, number_of_characters, sort_dict
book = "books/frankenstein.txt"
def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    option = sys.argv
    if len(option) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    full_text = (get_book_text(option[1]))
    num_words = count_words(full_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {option[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    unsorted_dict = number_of_characters(full_text)
    
    sorted_list = sort_dict(unsorted_dict)
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        if item['char'].isalpha() == True:
            print(f"{char}: {num}")           

main()